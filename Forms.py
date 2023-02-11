from wtforms import Form, TextAreaField, validators

class CreateFAQForm(Form):
    question = TextAreaField('Question', [validators.Length(min=1, max=200), validators.DataRequired()])
    answer = TextAreaField('Answer', [validators.Length(min=1, max=500), validators.DataRequired()])
