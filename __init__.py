from flask import Flask, render_template, request, redirect, url_for, g, session
from Forms import  CreatePaymentForm, CreateUserForm, CreateCustomerForm
import shelve, Payment
import stripe
app = Flask(__name__)


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    if request.method == 'POST':
        return redirect(url_for('/'))

    return render_template('thanks.html')



@app.route('/createPayment', methods=['GET', 'POST'])
def create_payment():
    create_payment_form = CreatePaymentForm(request.form)
    if request.method == 'POST' and create_payment_form.validate():
        payments_dict = {}
        db = shelve.open('payment.db', 'c')
        try:
            payments_dict = db['Payments']
        except:
            print("Error in retrieving Payments from payment.db.")

        payment = Payment.Payment(1, create_payment_form.cardholder_name.data, create_payment_form.card_number.data,
        create_payment_form.date_of_expiry.data)
        if len(payments_dict) == 0:
            payment.set_payment_id(1)
        else:
            payment.set_payment_id(max(payments_dict.keys()) +1)

        payments_dict[payment.get_payment_id()] = payment
        db['Payments'] = payments_dict

        db.close()
        return redirect(url_for('thanks'))
    return render_template('createPayment.html', form=create_payment_form)







@app.route('/retrievePayments')
def retrieve_payments():
    payments_dict = {}
    db = shelve.open('payment.db', 'r')
    payments_dict = db['Payments']
    db.close()

    payments_list = []
    for key in payments_dict:
        payment = payments_dict.get(key)
        payments_list.append(payment)


    return render_template('retrievePayments.html', count=len(payments_list), payments_list=payments_list)



@app.route('/updatePayment/<int:id>/', methods=['GET', 'POST'])
def update_payment(id):
    update_payment_form = CreatePaymentForm(request.form)
    if request.method == 'POST' and update_payment_form.validate():
        payments_dict = {}
        db = shelve.open('payment.db', 'w')
        payments_dict = db['Payments']

        payment = payments_dict.get(id)
        payment.set_cardholder_name(update_payment_form.cardholder_name.data)
        payment.set_card_number(update_payment_form.card_number.data)
        payment.set_date_of_expiry(update_payment_form.date_of_expiry.data)



        db['Payments'] = payments_dict
        db.close()

        return redirect(url_for('retrieve_payments'))
    else:
        payments_dict = {}
        db = shelve.open('payment.db', 'r')
        payments_dict = db['Payments']
        db.close()

        payment = payments_dict.get(id)
        update_payment_form.cardholder_name.data = payment.get_cardholder_name()
        update_payment_form.card_number.data = payment.get_card_number()
        update_payment_form.date_of_expiry.data = payment.get_date_of_expiry()



        return render_template('updatePayment.html', form=update_payment_form)



@app.route('/deletePayment/<int:id>', methods=['POST'])
def delete_payment(id):
    payments_dict = {}
    db = shelve.open('payment.db', 'w')
    payments_dict = db['Payments']
    payments_dict.pop(id)
    db['Payments'] = payments_dict
    db.close()
    return redirect(url_for('retrieve_payments'))

import shelve



@app.route('/add_to_cart', methods=['POST'])
def AddCart():
    try:
        pass
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)

# init_db()
@app.route('/store')
def store():

    return render_template('store.html')

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response

if __name__ == "__main__":
    app.run()


