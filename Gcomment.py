from wtforms import Form, TextAreaField, validators
import email_validator

class CreateCommentForm(Form):
    name = TextAreaField('Your name', [validators.Length(min=1, max=200), validators.DataRequired()], render_kw={"placeholder": "E.g. Alvin Tan"})
    number = TextAreaField('Your contact no.', [validators.Length(min=8, max=12), validators.DataRequired()], render_kw={"placeholder": "+65 12345678"})
    email = TextAreaField('Your email address', [validators.Email(message=None, granular_message=False, check_deliverability=False, allow_smtputf8=True, allow_empty_local=False), validators.DataRequired()], render_kw={"placeholder": "E.g. abc@gmail.com"})
    enquiry = TextAreaField('Your enquiry', [validators.Length(min=1, max=500), validators.DataRequired()], render_kw={"placeholder": "Question"})
