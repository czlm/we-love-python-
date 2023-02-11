from flask import Flask, render_template, request, redirect, url_for

import Comment
from Forms import CreateFAQForm
from Gcomment import CreateCommentForm
import shelve, FAQ
from flask_session.__init__ import Session

app = Flask(__name__)

@app.route('/') # first route you will be directed to
def home():
    return render_template('Ghome.html')

@app.route('/TcreateFAQ', methods=['GET', 'POST'])
def create_faq():
    create_faq_form = CreateFAQForm(request.form)
    if request.method == 'POST' and create_faq_form.validate():
        faqs_dict = {}
        db = shelve.open('faq.db', 'c')
        try:
            faqs_dict = db['FAQs']
        except:
            print("Error in retrieving FAQ from faq.db.")

        faq = FAQ.FAQ(create_faq_form.question.data, create_faq_form.answer.data)
        faqs_dict[faq.get_faq_id()] = faq
        db['FAQs'] = faqs_dict

        db.close()

        return redirect(url_for('retrieve_faqs'))
    return render_template('TcreateFAQ.html', form=create_faq_form)

@app.route('/TretrieveFAQ')
def retrieve_faqs():
    faqs_dict = {}
    db = shelve.open('faq.db', 'r')
    faqs_dict = db['FAQs']
    db.close()

    faqs_list = []
    for key in faqs_dict:
        faq = faqs_dict.get(key)
        faqs_list.append(faq)

    return render_template('TretrieveFAQ.html',count=len(faqs_list), faqs_list=faqs_list)

@app.route('/TupdateFAQ/<int:id>/', methods=['GET', 'POST'])
def update_faq(id):
    update_faq_form = CreateFAQForm(request.form)

    if request.method == 'POST' and update_faq_form.validate():
        faqs_dict = {}
        db = shelve.open('faq.db', 'w')
        faqs_dict = db['FAQs']

        faq = faqs_dict.get(id)
        faq.set_question(update_faq_form.question.data)
        faq.set_answer(update_faq_form.answer.data)

        db['FAQs'] = faqs_dict
        db.close()

        return redirect(url_for('retrieve_faqs'))
    else:
        faqs_dict = {}
        db = shelve.open('faq.db', 'r')
        faqs_dict = db['FAQs']
        db.close()

        faq = faqs_dict.get(id)
        update_faq_form.question.data = faq.get_question()
        update_faq_form.answer.data = faq.get_answer()

        return render_template('TupdateFAQ.html', form=update_faq_form)

@app.route('/deleteFAQ/<int:id>', methods=['POST'])
def delete_faq(id):
    faqs_dict = {}
    db = shelve.open('faq.db', 'w')
    faqs_dict = db['FAQs']

    faqs_dict.pop(id)

    faqs_list = []
    for key in faqs_dict:
        faq = faqs_dict.get(key)
        faqs_list.append(faq)

    faq_id = 1
    while (faq_id>1):
        faq.set_faq_id += 1

    db['FAQs'] = faqs_dict
    db.close()

    return redirect(url_for('retrieve_faqs'))

@app.route('/FAQdisplay')
def display_faqs():
    faqs_dict = {}
    db = shelve.open('faq.db', 'r')
    faqs_dict = db['FAQs']
    db.close()

    faqs_list = []
    for key in faqs_dict:
        faq = faqs_dict.get(key)
        faqs_list.append(faq)

    return render_template('FAQdisplay.html',count=len(faqs_list), faqs_list=faqs_list)

@app.route('/GChatbot') # first route you will be directed to
def chatbot():
    return render_template('GChatbot.html')

@app.route('/Gcreateqn', methods=['GET', 'POST'])
def create_comment():
    create_comment_form = CreateCommentForm(request.form)
    if request.method == 'POST' and create_comment_form.validate():
        comments_dict = {}
        db = shelve.open('comment.db', 'c')
        try:
            comments_dict = db['comments']
        except:
            print("Error in retrieving comments left from comment.db.")

        comment = Comment.Comment(create_comment_form.name.data, create_comment_form.number.data, create_comment_form.email.data, create_comment_form.enquiry.data)
        comments_dict[comment.get_cmt_id()] = comment
        db['comments'] = comments_dict

        db.close()

        return redirect(url_for('retrieve_comments'))
    return render_template('Gcreateqn.html', form=create_comment_form)

@app.route('/Tview')
def retrieve_comments():
    comments_dict = {}
    db = shelve.open('comment.db', 'r')
    comments_dict = db['comments']
    db.close()

    comments_list = []
    for key in comments_dict:
        comment = comments_dict.get(key)
        comments_list.append(comment)

    return render_template('Tview.html', count=len(comments_list), comments_list=comments_list)

@app.route('/deleteComment/<int:id>', methods=['POST'])
def delete_comment(id):
    comments_dict = {}
    db = shelve.open('comment.db', 'w')
    comments_dict = db['comments']

    comments_dict.pop(id)

    comments_list = []
    for key in comments_dict:
        comment = comments_dict.get(key)
        comments_list.append(comment)

    cmt_id = 1
    while (cmt_id>1):
        comment.set_cmt_id += 1

    db['comments'] = comments_dict
    db.close()

    return redirect(url_for('retrieve_comments'))

if __name__ == '__main__': #final piece of code
    app.run()
