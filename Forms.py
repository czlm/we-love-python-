from wtforms import Form, StringField, RadioField, EmailField, TextAreaField, SelectField, validators
from wtforms import DecimalField, IntegerField, TimeField, SelectMultipleField, DateField, SubmitField
from wtforms.fields import DateTimeField, DateTimeLocalField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf import FlaskForm


class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    level = SelectField('Choose your Level', [validators.DataRequired()], choices=[('', 'Select'), ('P1', 'Primary 1'), ('P2', 'Primary 2'), ('P3', 'Primary 3'), ('P4', 'Primary 4'), ('P5', 'Primary 5'), ('P6', 'Primary 6')], default='')
    subject = SelectMultipleField('Choose your Subject(s)', [validators.DataRequired()], choices=[('E', 'English'), ('M', 'Math'), ('S', 'Science'), ('C', 'Chinese')], default='')
    # announcement_descriptions = TextAreaField('Enter descriptions for announcement', [validators.Optional()])
    announcement_descriptions = StringField(default='nu')
    # grade = RadioField('Grade', choices=[(0, ''), (1, ''), (2, ''), (3, ''), (4, ''), (5, '')], default='0')
    grade = IntegerField('Grade for this class', [validators.NumberRange(max=0, message='Key either 1, 2, 3, 4 only'), validators.DataRequired()])


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


class CreateTeacherForm(Form):
    salutation = RadioField('Salutation', choices=[('Dr', 'Dr'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms')], default='Dr')
    first_name = StringField('First Name', [validators.length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender',
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],
                         default='')
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    date_joined = DateField('Date Joined',  [validators.DataRequired()])
    address = StringField('Address')
    subject = SelectMultipleField('Choose your Subject(s)', [validators.DataRequired()], choices=[('E', 'English'), ('M', 'Math'), ('S', 'Science'), ('C', 'Chinese')], default='')
    # announcement_descriptions = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    # announcement_descriptions = TextAreaField('Enter descriptions for announcement', [validators.Optional()])



class CreateQuizForm(FlaskForm):
    #studentid, teacherid, subjectid, quizid
    title = StringField('Title')
    description = StringField('Description')
    subject = SelectField('Subject', choices=[('','Select'),('1', 'English'), ('2','Math'), ('3','Science'), ('4','Chinese')])
    q1 = StringField('Question 1')
    q2 = StringField('Question 2')
    q3 = StringField('Question 3')
    q4 = StringField('Question 4')
    q5 = StringField('Question 5')
    ms1 = IntegerField('Question 1 Max Score')
    ms2 = IntegerField('Question 2 Max Score')
    ms3 = IntegerField('Question 3 Max Score')
    ms4 = IntegerField('Question 4 Max Score')
    ms5 = IntegerField('Question 5 Max Score')
    s1 = IntegerField('Question 1 Score')
    s2 = IntegerField('Question 2 Score')
    s3 = IntegerField('Question 3 Score')
    s4 = IntegerField('Question 4 Score')
    s5 = IntegerField('Question 5 Score')
    a1 = TextAreaField('Answer 1')
    a2 = TextAreaField('Answer 2')
    a3 = TextAreaField('Answer 3')
    a4 = TextAreaField('Answer 4')
    a5 = TextAreaField('Answer 5')
    r1 = TextAreaField('Remark 1')
    r2 = TextAreaField('Remark 2')
    r3 = TextAreaField('Remark 3')
    r4 = TextAreaField('Remark 4')
    r5 = TextAreaField('Remark 5')
    actualScore1 = IntegerField('Total Score')
    status = SelectField('Status', choices=["Pending","Completed"])
