# /project/tasks/views.py

from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint
import datetime

from forms import AddTaskForm, AddSearchForm

from ..app import db
from app.sample_workflow import run_workflow
from app.views import login_required
from app.models import Task, Search

################
#### config ####
################

tasks_blueprint = Blueprint(
        'tasks', __name__,
        url_prefix='/tasks',
        template_folder='templates',
        static_folder='static'
)


################
#### routes ####
################

@tasks_blueprint.route('/tasks/')
@login_required
def tasks( ):
    open_tasks = db.session.query(Task) \
        .filter_by(status='1').order_by(Task.due_date.asc())
    closed_tasks = db.session.query(Task) \
        .filter_by(status='0').order_by(Task.due_date.asc())
    return render_template(
            'tasks.html',
            form=AddTaskForm(request.form),
            open_tasks=open_tasks,
            closed_tasks=closed_tasks,
            username=session['name']
    )


# Add new tasks:
@tasks_blueprint.route('/add/', methods=['GET', 'POST'])
@login_required
def new_task( ):
    error = None
    form = AddTaskForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            task = Task(
                    form.name.data,
                    form.due_date.data,
                    form.priority.data,
                    datetime.datetime.utcnow(),
                    '1',
                    session['user_id']
            )
            db.session.add(task)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
            return redirect(url_for('tasks.tasks'))
        else:
            return render_template('tasks.html', form=form, error=error)


# Mark tasks as complete:
@tasks_blueprint.route('/complete/<int:task_id>/', )
@login_required
def complete( task_id ):
    new_id = task_id
    task = db.session.query(Task).filter_by(task_id=new_id)
    if session['user_id'] == task.first().user_id or session['role'] == "admin":
        task.update({"status": "0"})
        db.session.commit()
        flash('The task was marked as complete. Nice.')
        return redirect(url_for('tasks.tasks'))
    else:
        flash('You can only update tasks that belong to you.')
        return redirect(url_for('tasks.tasks'))


# Delete Tasks:
@tasks_blueprint.route('/delete/<int:task_id>/', )
@login_required
def delete_entry( task_id ):
    new_id = task_id
    task = db.session.query(Task).filter_by(task_id=new_id)
    if session['user_id'] == task.first().user_id or session['role'] == "admin":
        task.delete()
        db.session.commit()
        flash('The task was deleted. Why not add a new one?')
        return redirect(url_for('tasks.tasks'))
    else:
        flash('You can only delete tasks that belong to you.')
        return redirect(url_for('tasks.tasks'))


@tasks_blueprint.route('/searches/')
@login_required
def searches( ):
    completed_searches = db.session.query(Search).order_by(Search.posted_date.asc())
    
    return render_template(
            'searches.html',
            form=AddSearchForm(request.form),
            completed_searches=completed_searches,
            username=session['name']
    )


@tasks_blueprint.route('/add_search/', methods=['GET', 'POST'])
@login_required
def new_search( ):
    error = None
    form = AddSearchForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            search = Search(
                    form.name.data,
                    form.source.data,
                    form.data.data,
                    datetime.datetime.utcnow(),
                    session['user_id']
            )
            db.session.add(search)
            db.session.commit()
            flash('New search was successfully created.')
            
            # *** CRUCIAL
            # run_workflow(search.data)
            
            return redirect(url_for('tasks.searches'))
        else:
            return render_template('searches.html', form=form, error=error)


# Delete Tasks:
@tasks_blueprint.route('/delete_search/<int:search_id>/', )
@login_required
def delete_search( search_id ):
    new_id = search_id
    search = db.session.query(Search).filter_by(search_id=new_id)
    if session['user_id'] == search.first().user_id or session['role'] == "admin":
        search.delete()
        db.session.commit()
        flash('The search was deleted. Why not add a new one?')
        return redirect(url_for('tasks.searches'))
    else:
        flash('You can only delete searches that belong to you.')
        return redirect(url_for('tasks.searches'))
