from wtforms import Form, StringField, RadioField, TextAreaField, SelectField, validators
from wtforms import DecimalField, IntegerField, TimeField, SelectMultipleField, SubmitField
from wtforms.fields import DateTimeField,  DateTimeLocalField
from wtforms.validators import DataRequired, ValidationError

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    level = SelectField('Choose your Level', [validators.DataRequired()], choices=[('', 'Select'), ('P1', 'Primary 1'), ('P2', 'Primary 2'), ('P3', 'Primary 3'), ('P4', 'Primary 4'), ('P5', 'Primary 5'), ('P6', 'Primary 6')], default='')
    subject = SelectMultipleField('Choose your Subject(s)', [validators.DataRequired()], choices=[('E', 'English'), ('M', 'Math'), ('S', 'Science'), ('C', 'Chinese')], default='')
    announcement_descriptions = TextAreaField('Enter descriptions for announcement', [validators.Optional()])
    # announcement_descriptions = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    # grade = RadioField('Grade', choices=[(0, ''), (1, ''), (2, ''), (3, ''), (4, ''), (5, '')], default='0')
    grade = IntegerField('Grade for this class', [validators.NumberRange(min=0, max=1, message='Key either 1, 2, 3, 4 only'), validators.DataRequired()])


    overall_ratings = RadioField('Overall Ratings', choices=[(0, ''), (1, ''), (2, ''), (3, ''), (4, ''), (5, '')], default='0')


class CreateGradeForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    topic_no = IntegerField('Enter Topic No', [validators.NumberRange(min=1, max=10, message='1 to 10 only'), validators.DataRequired()])
    topic_title = StringField('Enter Title', [validators.Length(min=10, max=50), validators.DataRequired()])
    percentage = DecimalField('Percentage for this class(%)', [validators.NumberRange(min=1, max=100, message='Key in numbers only'), validators.DataRequired()])
    grade = IntegerField('Grade for this class', [validators.NumberRange(min=1, max=4, message='Key either 1, 2, 3, 4 only'), validators.DataRequired()])


class CreateAnnouncementForm(Form):
    announcement_descriptions = TextAreaField('Enter descriptions for announcement', [validators.Length(min=1, max=1000), validators.DataRequired()])
    salutation = RadioField('Salutation', choices=[('Dr', 'Dr'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms')], default='Dr')
    tutor_full_name = SelectField('Full name of Tutor', [validators.DataRequired()], choices=[('', 'Select'), ('BL', 'Bobby Liu'), ('AW', 'Andy Wong')], default='')
    created_datetime = DateTimeLocalField('Created date & time',  format="%Y-%m-%dT%H:%M", validators=[validators.DataRequired()])
    # default=datetime.today,

class CreateProgressreportForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    comments = TextAreaField('Comments', [validators.Length(min=3, max=400), validators.DataRequired()])
    overall_ratings = RadioField('Overall Ratings', choices=[(1, ''), (2, ''), (3, ''), (4, ''), (5, '')], render_kw={'class': 'star-icon'})


class CreateContentForm(Form):
    title = StringField("Title of the topic", [validators.Length(min=1, max=150), validators.DataRequired()])
    content = TextAreaField('Enter descriptions for this topic', [validators.Length(min=1, max=1000), validators.DataRequired()])
