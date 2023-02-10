from flask_wtf import FlaskForm
from wtforms import Form, StringField, RadioField, DateField, SelectField, TextAreaField, validators, BooleanField, IntegerField

class CreateSubjectForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=150), validators.DataRequired()])
    description = StringField('Description', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = IntegerField('Pricing',[validators.DataRequired()])
    level = SelectField('Level',
                         choices=[('', 'Select'), ('1', 'Primary 1'), ('2', 'Primary 2'), ('3', 'Primary 3'), ('4', 'Primary 4'),('5', 'Primary 5'), ('6', 'Primary 6')],
                         default='')


class CreateWithdrawalForm(Form):
    first_name = StringField('First Name', [validators.length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.length(min=1, max=150), validators.DataRequired()])
    level = SelectField('Level',
                        choices=[('', 'Select'), ('1', 'Primary 1'), ('2', 'Primary 2'), ('3', 'Primary 3'),
                                 ('4', 'Primary 4'), ('5', 'Primary 5'), ('6', 'Primary 6')],
                        default='')
    subject = SelectField('Subject', choices=[('', 'Select'), ('1', 'English'), ('2', 'Math'), ('3', 'Science'),
                                               ('4', 'Chinese')])
    reason = StringField('Reason', [validators.length(min=1, max=150), validators.DataRequired()])
    feedback = StringField('Feedback', [validators.length(min=1, max=150), validators.DataRequired()])
    ack = RadioField('I am the parent/guardian of the student. Parents will be notified for acknowledgement', choices=[('Yes', 'Yes')])


class CreateStudentForm(Form):
    first_name = StringField('First Name', [validators.length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender',
                         choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')],
                         default='')
    email = StringField('Email', [validators.length(min=1, max=150), validators.DataRequired()])
    date_joined = DateField('Date Joined',  [validators.DataRequired()])
    address = StringField('Address')
    level = SelectField('Level',
                        choices=[('', 'Select'), ('1', 'Primary 1'), ('2', 'Primary 2'), ('3', 'Primary 3'),
                                 ('4', 'Primary 4'), ('5', 'Primary 5'), ('6', 'Primary 6')],
                        default='')
    subject1 = SelectField('Subject',choices=[('','Select'),('1', 'English'), ('2','Math'), ('3','Science'), ('4','Chinese')])
    subject2 = SelectField('Subject', choices=[('','Select'),('1', 'English'), ('2','Math'), ('3','Science'), ('4','Chinese'), ('N','Not Applicable')])
    subject3 = SelectField('Subject', choices=[('','Select'),('1', 'English'), ('2','Math'), ('3','Science'), ('4','Chinese'),('','Not Applicable')])
    subject4 = SelectField('Subject', choices=[('','Select'),('1', 'English'), ('2','Math'), ('3','Science'), ('4','Chinese'),('','Not Applicable')])

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