# /project/tasks/forms.py


from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired


class AddTaskForm(Form):
    task_id = IntegerField()
    name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField(
            'Date Due (mm/dd/yyyy)',
            validators=[DataRequired()], format='%m/%d/%Y'
    )
    priority = SelectField(
            'Priority',
            validators=[DataRequired()],
            choices=[
                ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
            ]
    )
    status = IntegerField('Status')


class AddSearchForm(Form):
    search_id = IntegerField()
    name = StringField('Search Name', validators=[DataRequired()])
    source = SelectField(
            'Source',
            validators=[DataRequired()],
            choices=[
                ('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('FourSquare', 'Foursquare'),
                ('Google +', 'Google +'), ('Instagram', 'Instagram'), ('Yelp', 'Yelp')
            ]
    )
    data = TextAreaField('Data', validators=[DataRequired()])
