# /app/users/views.py


#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError

from app.views import login_required
from app.models import User
from app.app import db, bcrypt

from forms import RegisterForm, LoginForm

################
#### config ####
################

users_blueprint = Blueprint(
        'users', __name__,
        url_prefix='/users',
        template_folder='templates',
        static_folder='static'
)


################
#### routes ####
################

@users_blueprint.route('/logout/')
@login_required
def logout( ):
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('role', None)
    session.pop('username', None)
    flash('You are logged out.')
    return redirect(url_for('users.login'))


@users_blueprint.route('/', methods=['GET', 'POST'])
def login( ):
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()
            if user is None:
                error = 'Invalid username or password.'
                return render_template(
                        "login.html",
                        form=form,
                        error=error
                )
            elif bcrypt.check_password_hash(
                    user.password, request.form['password']
            ):
                session['logged_in'] = True
                session['user_id'] = user.id
                session['role'] = user.role
                session['username'] = user.username
                flash('Welcome!')
                return redirect(url_for('tasks.tasks'))
        else:
            return render_template(
                    "login.html",
                    form=form,
                    error=error
            )
    if request.method == 'GET':
        return render_template('login.html', form=form)


@users_blueprint.route('/register/', methods=['GET', 'POST'])
def register( ):
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                    form.username.data,
                    form.email.data,
                    bcrypt.generate_password_hash(form.password.data)
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering. Please login.')
                return redirect(url_for('users.login'))
            except IntegrityError:
                error = 'Sorry that username and/or email error already exist.'
                return render_template('register.html', form=form, error=error)
        else:
            return render_template('register.html', form=form, error=error)
    if request.method == 'GET':
        return render_template('register.html', form=form)


@users_blueprint.route('/about/')
def about( ):
    return render_template('about.html')
