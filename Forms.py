from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, IntegerField
from wtforms.fields import EmailField, DateField


class CreatePaymentForm(Form):
    cardholder_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    card_number = StringField('Last Name', [validators.Length(min=1, max=150),  validators.DataRequired()])
    date_of_expiry = DateField('Sign Up Date',  format='%Y-%m-%d')


class CreateUserForm(Form):
    first_name = IntegerField('English', [validators.NumberRange(min=0, max=1)], default=0)
    last_name = IntegerField('Math', [validators.NumberRange(min=0, max=1)], default=0)
    gender = IntegerField('Chinese', [validators.NumberRange(min=0, max=1)], default=0)
    membership = IntegerField('Science', [validators.NumberRange(min=0, max=1)], default=0)
    remarks = IntegerField('Total', [validators.NumberRange(min=0, max=600)], default=0)

class CreateCustomerForm(Form):
    first_name = StringField('Cardholder Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = IntegerField('Card Number', [validators.NumberRange(min=1, max=9999999999999999), validators.DataRequired()])
    gender = DateField('Date Of Expiry', format='%Y-%m-%d')
    membership = RadioField('Bank', choices=[('DBS', 'DBS'), ('OCBC', 'OCBC'), ('UOB', 'UOB')], default='DBS')
    code = IntegerField('CVV Code', [validators.NumberRange(min=1, max=999), validators.DataRequired()])


