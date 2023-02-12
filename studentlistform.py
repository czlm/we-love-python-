from wtforms import Form, StringField, validators


class CreateStudentForm(Form):
    sname = StringField('Student Name', [validators.Length(min=1, max=30), validators.DataRequired()])
    snumber = StringField('Student Phone number', [validators.Length(min=8, max=8), validators.DataRequired()])
    pname = StringField('Parent Name', [validators.Length(min=1, max=30), validators.DataRequired()])
    pnumber = StringField('Student  Phone number', [validators.Length(min=8, max=8), validators.DataRequired()])

