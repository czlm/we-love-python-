from flask import Flask, render_template, request, redirect, url_for, session, g
from Forms import CreateUserForm, CreateGradeForm, CreateAnnouncementForm, CreateProgressreportForm, CreateTeacherForm, CreateQuizForm
import shelve, User, Grade, Announcement, Progressreport, Teacher, Quiz, FAQ, Comment, Subject, Payment
from datetime import datetime


from werkzeug.utils import secure_filename
from Forms1 import CreateFAQForm
from Gcomment import CreateCommentForm


import Student
import SubjectStudent
import SubjectTeacher
from Forms2 import *


from Forms3 import CreatePaymentForm
# import stripe


app = Flask(__name__)
app.secret_key = 'any_random_string'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def guest_home_page():
    return render_template('ghome.html')

@app.route('/english')
def english_page():
    return render_template('english.html')

@app.route('/math')
def math_page():
    return render_template('math.html')

@app.route('/chinese')
def chinese_page():
    return render_template('chinese.html')

@app.route('/science')
def science_page():
    return render_template('science.html')



@app.route('/studentHomePage')
def studentHomePage():
#Retrieve grades
    grades_dict = {}

    try:
        db = shelve.open('grade.db', 'r')
        if 'Grades' in db:
            grades_dict = db['Grades']
        else:
            db['Grades'] = grades_dict
        db.close()

    except:
        print('Error in opening grade.db')

#Counting the number of grades. Data for the graph
    gradecount = [0, 0, 0, 0] #1, 2, 3, 4
    grades_list = []
    for key in grades_dict:
        grade_object = grades_dict.get(key)
        grades_list.append(grade_object)
        if grade_object.get_grade() == 1:
            gradecount[0] += 1
        elif grade_object.get_grade() == 2:
            gradecount[1] += 1
        elif grade_object.get_grade() == 3:
            gradecount[2] += 1
        elif grade_object.get_grade() == 4:
            gradecount[3] += 1
    print(gradecount)
    print(grades_list)

#Counting the number of grades. Data for the graph
    predictedscore = [0, 0, 0, 0] # e.g. 18 + 13 + 15 + 10 = 56%
    predictedscore_list = []
    for key in grades_dict:
        predictedscore_object = grades_dict.get(key)
        predictedscore_list.append(predictedscore_object)
        if predictedscore_object.get_grade() == 1:
            predictedscore[0] = (91/100)*20
        elif predictedscore_object.get_grade() == 2:
            predictedscore[1] = (77/100)*20
        elif predictedscore_object.get_grade() == 3:
            predictedscore[2] = (60/100)*20
        elif predictedscore_object.get_grade() == 4:
            predictedscore[3] = (43/100)*20

    predictedscorecount = sum(predictedscore)
    predictedscorecountleft = 100 - sum(predictedscore)

    # print(predictedscore)
    # print(predictedscore_list)
    # print(predictedscorecount)


#Retrieve announcements
    announcements_dict = {}

    try:
        db = shelve.open('announcement.db', 'r')
        if 'Announcements' in db:
            announcements_dict = db['Announcements']
        else:
            db['Announcements'] = announcements_dict
        db.close()

    except:
        print('Error in opening announcement.db')


    announcements_list = []
    for key in announcements_dict:
        announcement = announcements_dict.get(key)
        announcements_list.append(announcement)

    #sort based on created_datetime in desending order
    announcements_list.sort(key=lambda x: x.get_created_datetime(), reverse=True)
    # print(announcements_list)

    return render_template('studentHomePage.html', announcements_list=announcements_list, grades_list=grades_list, gradecount=gradecount,
                           predictedscore=predictedscore, predictedscorecount=predictedscorecount, predictedscorecountleft=predictedscorecountleft)


@app.route('/teacherHomePage')
def teacherHomePage():
#Retrieve grade
    grades_dict = {}

    try:
        db = shelve.open('grade.db', 'r')
        if 'Grades' in db:
            grades_dict = db['Grades']
        else:
            db['Grades'] = grades_dict
        db.close()

    except:
        print('Error in opening grade.db')


    grades_list = []
    for key in grades_dict:
        grade = grades_dict.get(key)
        grades_list.append(grade)

#Retrieve progress report
    progressreports_dict = {}

    try:
        db = shelve.open('progressreport.db', 'r')
        if 'Progressreports' in db:
            progressreports_dict = db['Progressreports']
        else:
            db['Progressreports'] = progressreports_dict
        db.close()

    except:
        print('Error in opening progressreport.db')


    progressreports_list = []
    for key in progressreports_dict:
        progressreport = progressreports_dict.get(key)
        progressreports_list.append(progressreport)


#Create progress report
    create_progressreport_form = CreateProgressreportForm(request.form)
    if request.method == 'POST' and create_progressreport_form.validate():
        progressreports_dict = {}
        db = shelve.open('progressreport.db', 'c')
        print(datetime.now().strftime("%H:%M"))

        try:
            progressreports_dict = db['Progressreports']
        except:
            print("Error in retrieving Progressreports from progressreport.db.")
        last_progressreport_id = 1
        if len(progressreports_dict) > 0:
            progressreports_list = []
            for key in progressreports_dict:
                progressreport = progressreports_dict.get(key)
                progressreports_list.append(progressreport)

            last_progressreport_id = progressreports_list[-1].get_progressreport_id() + 1

        progressreport = Progressreport.Progressreport(last_progressreport_id, create_progressreport_form.first_name.data, create_progressreport_form.last_name.data,
                                                       create_progressreport_form.comments.data, create_progressreport_form.overall_ratings.data,
                                                       2)

        progressreports_dict[progressreport.get_progressreport_id()] = progressreport
        db['Progressreports'] = progressreports_dict
        db.close()

        return render_template('teacherHomePage.html')



#Retrieve users
    users_dict = {}
    db = shelve.open('user.db', 'c')

    if 'Users' in db:
        users_dict = db['Users']
    else:
        db['Users'] = users_dict

    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict. get(key)
        users_list.append(user)


#Retrieve announcements
    announcements_dict = {}

    try:
        db = shelve.open('announcement.db', 'r')
        if 'Announcements' in db:
            announcements_dict = db['Announcements']
        else:
            db['Announcements'] = announcements_dict
        db.close()

    except:
        print('Error in opening announcement.db')


    announcements_list = []
    for key in announcements_dict:
        announcement = announcements_dict.get(key)
        announcements_list.append(announcement)

    #sort based on created_datetime in desending order
    announcements_list.sort(key=lambda x: x.get_created_datetime(), reverse=True)
    # print(announcements_list)

    return render_template('teacherHomePage.html', grades_list=grades_list, progressreports_list=progressreports_list, form=create_progressreport_form, users_list=users_list,
                           announcements_list=announcements_list)




@app.route('/searchGrade', methods=['GET', 'POST'])
def searchGrade():
    if request.method == 'POST':
        keyword = request.form['keyword']

        # Open the shelve database
        with shelve.open('grade.db') as db:
            # Search for the keyword in the database
            results = []
            for key in db.keys():
                if keyword in db[key]:
                    results.append(db[key])

            # sort based on created_datetime in desending order
            # announcements_list.sort(key=lambda x: x.get_created_datetime(), reverse=True)


        return render_template('search_results.html', results=results)
    else:
        return 'Invalid request method'


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    subjects = ['English', 'Math', 'Science', 'Chinese']
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST':
        users_dict = {}
        # print(request.form.getlist('mycheckbox')) #returns subjects in a python list
        db = shelve.open('user.db', 'c')

        try:
            if 'Users' in db:
                users_dict = db['Users']
            else:
                db['Users'] = users_dict
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.level.data, request.form.getlist('mycheckbox'),
                         create_user_form.announcement_descriptions.data, create_user_form.grade.data, create_user_form.overall_ratings.data)
        users_dict[user.get_user_id()] = user

        db['Users'] = users_dict

        db.close()

        session['user_created'] = user.get_first_name() + ' ' + user.get_last_name()

        return redirect(url_for('studentHomePage'))
    return render_template('createUser2.html', form=create_user_form, subjects=subjects)


@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db', 'c')
    try:
        users_dict = db['Users']
    except:
        print("Error in retrieving Users from user.db.")
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict. get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)


@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_level(update_user_form.level.data)
        user.set_subject(update_user_form.subject.data)
        user.set_announcement_descriptions(update_user_form.announcement_descriptions.data)
        user.set_grade(update_user_form.grade.data)
        user.set_overall_ratings(update_user_form.overall_ratings.data)

        db['Users'] = users_dict
        db.close()

        session['user_updated'] = user.get_first_name() + ' ' + user.get_last_name()

        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.level.data = user.get_level()
        update_user_form.subject.data = user.get_subject()
        update_user_form.announcement_descriptions.data = user.get_announcement_descriptions()
        update_user_form.grade.data = user.get_grade()
        update_user_form.overall_ratings.data = user.get_overall_ratings()

        return render_template('updateUser.html', form=update_user_form)


@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}

    db = shelve.open('user.db', 'w')
    users_dict = db['Users']
    users_dict.pop(id)
    db['Users'] = users_dict
    db.close()
    # session['user_deleted'] = user.get_first_name() + ' ' + user.get_last_name()

    return redirect(url_for('retrieve_users'))



@app.route('/createGrade', methods=['GET', 'POST'])
def create_grade():
    create_grade_form = CreateGradeForm(request.form)
    if request.method == 'POST': # and create_grade_form.validate():
        grades_dict = {}
        db = shelve.open('grade.db', 'c')

        #get the user from db.
        users_dict = {}
        # the db change to user_db
        user_db = shelve.open('user.db', 'w')
        users_dict = user_db['Users']

        try:
            grades_dict = db['Grades']

        except:
            print("Error in retrieving Grades from grade.db.")

        try:
            users_dict = db['Users']

        except:
            print("Error in retrieving Users from user.db.")

        # calling the session (user id)
        user = users_dict.get(2)
        # updating the overall_ratings from user
        # originally, the user will have 0star so need to update the user's overall_ratings so it will move the user from incomplete to complete side
        user.set_grade(create_grade_form.grade.data)

        last_grade_id = 1
        if len(grades_dict) > 0:
            grades_list = []
            for key in grades_dict:
                grade = grades_dict.get(key)
                grades_list.append(grade)

            last_grade_id = grades_list[-1].get_grade_id() + 1

        grade = Grade.Grade(last_grade_id, create_grade_form.first_name.data, create_grade_form.last_name.data,
                                                       create_grade_form.topic_no.data, create_grade_form.topic_title.data, create_grade_form.percentage.data,
                                                       create_grade_form.grade.data, 2)

        #
        # put the session (user id) in the above area^
        #

        grades_dict[grade.get_grade_id()] = grade
        db['Grades'] = grades_dict
        db.close()

        # Close user_db
        user_db['Users'] = users_dict
        user_db.close()
        return redirect(url_for('teacherHomePage'))
    return render_template('createGrade.html', form=create_grade_form)



@app.route('/retrieveGrades')
def retrieve_grades():
    grades_dict = {}

    try:
        db = shelve.open('grade.db', 'r')
        if 'Grades' in db:
            grades_dict = db['Grades']
        else:
            db['Grades'] = grades_dict
        db.close()

    except:
        print('Error in opening grade.db')


    grades_list = []
    for key in grades_dict:
        grade = grades_dict.get(key)
        grades_list.append(grade)

    return render_template('retrieveGrades.html', count=len(grades_list), grades_list=grades_list)


@app.route('/updateGrade/<int:id>/', methods=['GET', 'POST'])
def update_grade(id):
    update_grade_form = CreateGradeForm(request.form)
    if request.method == 'POST' and update_grade_form.validate():
        grades_dict = {}
        db = shelve.open('grade.db', 'w')
        grades_dict = db['Grades']

        grade = grades_dict.get(id)
        grade.set_first_name(update_grade_form.first_name.data)
        grade.set_last_name(update_grade_form.last_name.data)
        grade.set_topic_no(update_grade_form.topic_no.data)
        grade.set_topic_title(update_grade_form.topic_title.data)
        grade.set_percentage(update_grade_form.percentage.data)
        grade.set_grade(update_grade_form.grade.data)

        db['Grades'] = grades_dict
        db.close()

        return redirect(url_for('retrieve_grades'))
    else:
        grades_dict = {}
        db = shelve.open('grade.db', 'r')
        grades_dict = db['Grades']
        db.close()

        grade = grades_dict.get(id)
        update_grade_form.first_name.data = grade.get_first_name()
        update_grade_form.last_name.data = grade.get_last_name()
        update_grade_form.topic_no.data = grade.get_topic_no()
        update_grade_form.topic_title.data = grade.get_topic_title()
        update_grade_form.percentage.data = grade.get_percentage()
        update_grade_form.grade.data = grade.get_grade()

        return render_template('updateGrade.html', form=update_grade_form)


@app.route('/deleteGrade/<int:id>', methods=['POST'])
def delete_grade(id):
    grades_dict = {}
    db = shelve.open('grade.db', 'w')
    grades_dict = db['Grades']
    grades_dict.pop(id)
    db['Grades'] = grades_dict
    db.close()
    return redirect(url_for('retrieve_grades'))


@app.route('/createAnnouncement', methods=['GET', 'POST'])
def create_announcement():
    create_announcement_form = CreateAnnouncementForm(request.form)
    if request.method == 'POST' and create_announcement_form.validate():
        announcements_dict = {}
        db = shelve.open('announcement.db', 'c')

        #get the user from db.
        users_dict = {}
        # the db change to user_db
        user_db = shelve.open('user.db', 'w')
        users_dict = user_db['Users']

        try:
            announcements_dict = db['Announcements']
        except:
            print("Error in retrieving Announcements from announcement.db.")

        try:
            users_dict = db['Users']

        except:
            print("Error in retrieving Users from user.db.")

        # calling the session (user id)
        user = users_dict.get(2)
        # updating the overall_ratings from user
        # originally, the user will have 0star so need to update the user's overall_ratings so it will move the user from incomplete to complete side
        user.set_announcement_descriptions(create_announcement_form.announcement_descriptions.data)

        last_announcement_id = 1
        if len(announcements_dict) > 0:
            announcements_list = []
            for key in announcements_dict:
                announcement = announcements_dict.get(key)
                announcements_list.append(announcement)

            last_announcement_id = announcements_list[-1].get_announcement_id() + 1

        announcement = Announcement.Announcement(last_announcement_id,
                                     create_announcement_form.announcement_descriptions.data, create_announcement_form.salutation.data, create_announcement_form.tutor_full_name.data,
                                     create_announcement_form.created_datetime.data, 2)
        announcements_dict[announcement.get_announcement_id()] = announcement
        db['Announcements'] = announcements_dict
        db.close()

        # Close user_db
        user_db['Users'] = users_dict
        user_db.close()
        return redirect(url_for('studentHomePage'))
    return render_template('createAnnouncement.html', form=create_announcement_form)


@app.route('/retrieveAnnouncements')
def retrieve_announcements():
    announcements_dict = {}

    try:
        db = shelve.open('announcement.db', 'r')
        if 'Announcements' in db:
            announcements_dict = db['Announcements']
        else:
            db['Announcements'] = announcements_dict
        db.close()

    except:
        print('Error in opening announcement.db')

    announcements_list = []
    for key in announcements_dict:
        announcement = announcements_dict.get(key)
        announcements_list.append(announcement)

    return render_template('retrieveAnnouncements.html', count=len(announcements_list), announcements_list=announcements_list)



@app.route('/updateAnnouncement/<int:id>/', methods=['GET', 'POST'])
def update_announcement(id):
    update_announcement_form = CreateAnnouncementForm(request.form)
    if request.method == 'POST' and update_announcement_form.validate():
        announcements_dict = {}
        db = shelve.open('announcement.db', 'w')
        announcements_dict = db['Announcements']

        announcement = announcements_dict.get(id)
        announcement.set_announcement_descriptions(update_announcement_form.announcement_descriptions.data)
        announcement.set_salutation(update_announcement_form.salutation.data)
        announcement.set_tutor_full_name(update_announcement_form.tutor_full_name.data)
        announcement.set_created_datetime(update_announcement_form.created_datetime.data)

        db['Announcements'] = announcements_dict
        db.close()

        return redirect(url_for('retrieve_announcements'))
    else:
        announcements_dict = {}
        db = shelve.open('announcement.db', 'r')
        announcements_dict = db['Announcements']
        db.close()

        announcement = announcements_dict.get(id)
        update_announcement_form.announcement_descriptions.data = announcement.get_announcement_descriptions()
        update_announcement_form.salutation.data = announcement.get_salutation()
        update_announcement_form.tutor_full_name.data = announcement.get_tutor_full_name()
        update_announcement_form.created_datetime.data = announcement.get_created_datetime()


        return render_template('updateAnnouncement.html', form=update_announcement_form)



@app.route('/deleteAnnouncement/<int:id>', methods=['POST'])
def delete_announcement(id):
    announcements_dict = {}
    db = shelve.open('announcement.db', 'w')
    announcements_dict = db['Announcements']
    announcements_dict.pop(id)
    db['Announcements'] = announcements_dict
    db.close()
    return redirect(url_for('retrieve_announcements'))

# did some alterations to include the user for incomplete to complete section
@app.route('/createProgressreport', methods=['GET', 'POST'])
def create_progressreport():
    create_progressreport_form = CreateProgressreportForm(request.form)
    if request.method == 'POST' and create_progressreport_form.validate():
        progressreports_dict = {}
        db = shelve.open('progressreport.db', 'c')

        #get the user from db.
        users_dict = {}
        # the db change to user_db
        user_db = shelve.open('user.db', 'w')
        users_dict = user_db['Users']

        try:
            progressreports_dict = db['Progressreports']

        except:
            print("Error in retrieving Progressreports from progressreport.db.")

        try:
            users_dict = db['Users']

        except:
            print("Error in retrieving Users from user.db.")

        # calling the session (user id)
        user = users_dict.get(2)
        # updating the overall_ratings from user
        # originally, the user will have 0star so need to update the user's overall_ratings so it will move the user from incomplete to complete side
        user.set_overall_ratings(create_progressreport_form.overall_ratings.data)

        last_progressreport_id = 1
        if len(progressreports_dict) > 0:
            progressreports_list = []
            for key in progressreports_dict:
                progressreport = progressreports_dict.get(key)
                progressreports_list.append(progressreport)

            last_progressreport_id = progressreports_list[-1].get_progressreport_id() + 1

        progressreport = Progressreport.Progressreport(last_progressreport_id, create_progressreport_form.first_name.data, create_progressreport_form.last_name.data,
                                                       create_progressreport_form.comments.data, create_progressreport_form.overall_ratings.data, 2)

        #
        # put the session (user id) in the above area^
        #

        progressreports_dict[progressreport.get_progressreport_id()] = progressreport
        db['Progressreports'] = progressreports_dict
        db.close()

        # Close user_db
        user_db['Users'] = users_dict
        user_db.close()
        return redirect(url_for('teacherHomePage'))
    return render_template('createProgressreport.html', form=create_progressreport_form)


@app.route('/retrieveProgressreports')
def retrieve_progressreports():
    progressreports_dict = {}

    try:
        db = shelve.open('progressreport.db', 'r')
        if 'Progressreports' in db:
            progressreports_dict = db['Progressreports']
        else:
            db['Progressreports'] = progressreports_dict
        db.close()

    except:
        print('Error in opening progressreport.db')


    progressreports_list = []
    for key in progressreports_dict:
        progressreport = progressreports_dict.get(key)
        progressreports_list.append(progressreport)

    return render_template('retrieveProgressreports.html', count=len(progressreports_list), progressreports_list=progressreports_list)


@app.route('/updateProgressreport/<int:id>/', methods=['GET', 'POST'])
def update_progressreport(id):
    update_progressreport_form = CreateProgressreportForm(request.form)
    if request.method == 'POST' and update_progressreport_form.validate():
        progressreports_dict = {}
        db = shelve.open('progressreport.db', 'w')
        progressreports_dict = db['Progressreports']

        progressreport = progressreports_dict.get(id)
        progressreport.set_first_name(update_progressreport_form.first_name.data)
        progressreport.set_last_name(update_progressreport_form.last_name.data)
        progressreport.set_comments(update_progressreport_form.comments.data)
        progressreport.set_overall_ratings(update_progressreport_form.overall_ratings.data)

        db['Progressreports'] = progressreports_dict
        db.close()

        return redirect(url_for('retrieve_progressreports'))
    else:
        progressreports_dict = {}
        db = shelve.open('progressreport.db', 'r')
        progressreports_dict = db['Progressreports']
        db.close()

        progressreport = progressreports_dict.get(id)
        update_progressreport_form.first_name.data = progressreport.get_first_name()
        update_progressreport_form.last_name.data = progressreport.get_last_name()
        update_progressreport_form.comments.data = progressreport.get_comments()
        update_progressreport_form.overall_ratings.data = progressreport.get_overall_ratings()

        return render_template('updateProgressreport.html', form=update_progressreport_form)


@app.route('/deleteProgressreport/<int:id>', methods=['POST'])
def delete_progressreport(id):
    progressreports_dict = {}
    db = shelve.open('progressreport.db', 'w')
    progressreports_dict = db['Progressreports']
    progressreports_dict.pop(id)
    db['Progressreports'] = progressreports_dict
    db.close()
    return redirect(url_for('retrieve_progressreports'))



from flask_wtf import FlaskForm
from flask_wtf.file import FileField

class UploadForm(FlaskForm):
    file = FileField()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/' + filename)
        return redirect(url_for('upload'))

    return render_template('upload1.html', form=form)



# @app.route('/createUpload', methods=['GET', 'POST'])
# def create_upload():
#     form = CreateUploadForm(request.form)
#
#     if form.validate_on_submit():
#         filename = secure_filename(form.file.data.filename)
#         form.file.data.save('uploads/' + filename)
#         return redirect(url_for('createUpload'))
#
#     return render_template('createUpload.html', form=form)

@app.route('/createQuiz', methods=['GET', 'POST'])
def create_quiz():
    create_quiz_form = CreateQuizForm(request.form)
    if request.method == 'POST':# and create_quiz_form.validate():
        quiz_dict = {}
        db = shelve.open('quiz.db', 'c')

        try:
            quiz_dict = db['Quizzes']

        except:
            print("Error in retrieving quizzes from quiz.db")

        import Quiz
        quiz = Quiz.Quiz(1, int(create_quiz_form.subject.data), 1, 1,create_quiz_form.title.data, create_quiz_form.description.data, create_quiz_form.q1.data,create_quiz_form.q2.data,create_quiz_form.q3.data,create_quiz_form.q4.data,create_quiz_form.q5.data,create_quiz_form.a1.data,create_quiz_form.a2.data,create_quiz_form.a3.data,create_quiz_form.a4.data,create_quiz_form.a5.data, create_quiz_form.ms1.data,create_quiz_form.ms2.data,create_quiz_form.ms3.data,create_quiz_form.ms4.data,create_quiz_form.ms5.data,create_quiz_form.s1.data,create_quiz_form.s2.data,create_quiz_form.s3.data,create_quiz_form.s4.data,create_quiz_form.s5.data,create_quiz_form.r1.data,create_quiz_form.r2.data,create_quiz_form.r3.data,create_quiz_form.r4.data,create_quiz_form.r5.data, create_quiz_form.actualScore1.data, create_quiz_form.status.data)
        if len(quiz_dict) != 0 and quiz.get_quiz_id() <= int(
                list(quiz_dict.keys())[-1]):
            quiz.set_quiz_id((int(list(quiz_dict.keys())[-1]) + 1))
            quiz_dict[quiz.get_quiz_id()] = quiz
        else:
            quiz_dict[quiz.get_quiz_id()] = quiz

        quiz_dict[quiz.get_quiz_id()] = quiz

        db['Quizzes'] = quiz_dict
        db.close()
        return redirect(url_for('teacherHomePage'))
    return render_template('createQuiz.html', form=create_quiz_form)


@app.route('/retrieveQuiz')
def retrieve_quiz():
    quiz_dict = {}
    db = shelve.open('quiz.db', 'r')
    quiz_dict = db['Quizzes']
    db.close()

    quiz_list = []
    for key in quiz_dict:
        quiz = quiz_dict.get(key)
        quiz_list.append(quiz)

    return render_template('retrieveQuiz.html', count=len(quiz_list), quiz_list=quiz_list)


@app.route('/retrieveQuiz2')
def retrieve_quiz2():
    quiz_dict = {}
    db = shelve.open('quiz.db', 'r')
    quiz_dict = db['Quizzes']
    db.close()

    quiz_list = []
    for key in quiz_dict:
        quiz = quiz_dict.get(key)
        quiz_list.append(quiz)

    return render_template('retrieveQuiz2.html', count=len(quiz_list), quiz_list=quiz_list)

@app.route('/updateQuiz/<int:id>/', methods=['GET', 'POST'])
def update_quiz(id):
    update_quiz_form = CreateQuizForm(request.form)
    if request.method == 'POST':# and update_quiz_form.validate():
        quiz_dict = {}
        db = shelve.open('quiz.db', 'w')
        quiz_dict = db['Quizzes']

        quiz = quiz_dict.get(id)
        quiz.set_title(update_quiz_form.title.data)
        quiz.set_description(update_quiz_form.description.data)
        quiz.set_q1(update_quiz_form.q1.data)
        quiz.set_q2(update_quiz_form.q2.data)
        quiz.set_q3(update_quiz_form.q3.data)
        quiz.set_q4(update_quiz_form.q4.data)
        quiz.set_q5(update_quiz_form.q5.data)
        quiz.set_ms1(update_quiz_form.ms1.data)
        quiz.set_ms2(update_quiz_form.ms2.data)
        quiz.set_ms3(update_quiz_form.ms3.data)
        quiz.set_ms4(update_quiz_form.ms4.data)
        quiz.set_ms5(update_quiz_form.ms5.data)

        db['Quizzes'] = quiz_dict
        db.close()
        return redirect(url_for('retrieve_quiz'))
    else:
        quiz_dict = {}
        db = shelve.open('quiz.db', 'r')
        quiz_dict = db['Quizzes']
        db.close()

        quiz = quiz_dict.get(id)
        quiz.set_title(update_quiz_form.title.data)
        quiz.set_description(update_quiz_form.description.data)
        quiz.set_q1(update_quiz_form.q1.data)
        quiz.set_q2(update_quiz_form.q2.data)
        quiz.set_q3(update_quiz_form.q3.data)
        quiz.set_q4(update_quiz_form.q4.data)
        quiz.set_q5(update_quiz_form.q5.data)
        quiz.set_ms1(update_quiz_form.ms1.data)
        quiz.set_ms2(update_quiz_form.ms2.data)
        quiz.set_ms3(update_quiz_form.ms3.data)
        quiz.set_ms4(update_quiz_form.ms4.data)
        quiz.set_ms5(update_quiz_form.ms5.data)

        return render_template('updateQuiz.html', form=update_quiz_form)

@app.route('/deleteQuiz/<int:id>', methods=['POST'])
def delete_quiz(id):
    quiz_dict = {}
    db = shelve.open('quiz.db', 'w')
    quiz_dict = db['Quizzes']
    quiz_dict.pop(id)
    db['Quizzes'] = quiz_dict
    db.close()

    return redirect(url_for('retrieve_quiz'))



@app.route('/takeQuiz/<int:id>', methods=['GET', 'POST'])
def take_quiz(id):
    quiz_dict = {}
    db = shelve.open('quiz.db', 'r')
    quiz_dict = db['Quizzes']
    db.close()

    quiz = quiz_dict.get(id)
    qn_list = []
    qn_list.append(quiz)

    create_ans_form = CreateQuizForm(request.form)
    if request.method == 'POST':  # and create_quiz_form.validate():
        answer_dict = {}
        db = shelve.open('answer.db', 'c')

        try:
            answer_dict = db['Answers']

        except:
            print("Error in retrieving answers from answer.db")

        import Answer
        answer = Answer.Answer(1, 1, 1, create_ans_form.a1.data, create_ans_form.a2.data, create_ans_form.a3.data,
                               create_ans_form.a4.data, create_ans_form.a5.data)
        if len(answer_dict) == 0:
            answer.set_answer_id(1)
        else:
            answer.set_answer_id(max(answer_dict.keys()) + 1)

        answer_dict[answer.get_answer_id()] = answer

        db['Answers'] = answer_dict
        db.close()
        return redirect(url_for('studentHomePage'))
    return render_template('takeQuiz.html', form=create_ans_form, qn_list=qn_list)



@app.route('/submitQuiz' , methods=['GET', 'POST'])
def submit_quiz():
    create_ans_form = CreateQuizForm(request.form)
    if request.method == 'POST':  # and create_quiz_form.validate():
        answer_dict = {}
        db = shelve.open('answer.db', 'c')

        try:
            answer_dict = db['Answers']

        except:
            print("Error in retrieving answers from answer.db")

        import Answer
        answer = Answer.Answer(1,1,1, create_ans_form.a1.data, create_ans_form.a2.data, create_ans_form.a3.data, create_ans_form.a4.data, create_ans_form.a5.data)
        if len(answer_dict) == 0:
            answer.set_answer_id(1)
        else:
            answer.set_answer_id(max(answer_dict.keys()) + 1)

        answer_dict[answer.get_answer_id()] = answer

        db['Answers'] = answer_dict
        db.close()
        return redirect(url_for('studentHomePage'))
    return render_template('takeQuiz.html', form=create_ans_form)



@app.route('/deleteSubjectStudent/<int:id>', methods=['POST'])
def delete_subject_student(id):
    subject_student_dict = {}
    db = shelve.open('subject_student.db', 'w')
    subject_student_dict = db['SubjectStudents']
    subject_student_dict.pop(id)
    db['SubjectStudents'] = subject_student_dict
    db.close()

    return redirect(url_for('retrieve_students'))


@app.route('/retrieveAnswers')
def retrieve_answers():
    answer_dict = {}
    db = shelve.open('answer.db', 'r')
    answer_dict = db['Answers']
    db.close()

    answer_list = []
    for key in answer_dict:
        answer = answer_dict.get(key)
        answer_list.append(answer)

    return render_template('retrieveAnswers.html', count=len(answer_list), answer_list=answer_list)

@app.route('/markAnswer/<int:id>', methods=['GET', 'POST'])
def mark_answer(id):
    answer_dict = {}
    db = shelve.open('answer.db', 'r')
    answer_dict = db['Answers']
    db.close()

    answer = answer_dict.get(id)
    ans_list = []
    ans_list.append(answer)

    quiz_dict = {}
    db = shelve.open('quiz.db', 'r')
    quiz_dict = db['Quizzes']
    db.close()

    quiz = quiz_dict.get(id)
    qn_list = []
    qn_list.append(quiz)

    create_score_form = CreateQuizForm(request.form)
    if request.method == 'POST':  # and create_quiz_form.validate():
        score_dict = {}
        db = shelve.open('score.db', 'c')

        try:
            answer_dict = db['Scores']

        except:
            print("Error in retrieving scores from score.db")

        import Score
        score = Score.Score(1, 1, create_score_form.s1.data, create_score_form.s2.data, create_score_form.s3.data,
                               create_score_form.s4.data, create_score_form.s5.data)
        if len(score_dict) == 0:
            score.set_score_id(1)
        else:
            score.set_score_id(max(score_dict.keys()) + 1)

        score_dict[score.get_score_id()] = score

        db['Scores'] = score_dict
        db.close()
        return redirect(url_for('teacherHomePage'))
    return render_template('markAnswer.html', form=create_score_form, ans_list=ans_list, qn_list=qn_list)

@app.route('/submitScore' , methods=['GET', 'POST'])
def submit_score():
    create_score_form = CreateQuizForm(request.form)
    if request.method == 'POST':  # and create_quiz_form.validate():
        score_dict = {}
        db = shelve.open('score.db', 'c')

        try:
            answer_dict = db['Scores']

        except:
            print("Error in retrieving scores from score.db")

        import Score
        score = Score.Score(1, 1, create_score_form.s1.data, create_score_form.s2.data, create_score_form.s3.data,
                            create_score_form.s4.data, create_score_form.s5.data)
        if len(score_dict) == 0:
            score.set_score_id(1)
        else:
            score.set_score_id(max(score_dict.keys()) + 1)

        score_dict[score.get_score_id()] = score

        db['Scores'] = score_dict
        db.close()
        return redirect(url_for('teacherHomePage'))
    return render_template('markAnswer.html', form=create_score_form)





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




@app.route('/createSubject', methods=['GET', 'POST'])
def create_subject():
    create_subject_form = CreateSubjectForm(request.form)
    if request.method == 'POST' and create_subject_form.validate():
        subject_dict = {}
        db = shelve.open('subject.db', 'c')

        try:
            subject_dict = db['Subjects']

        except:
            print('Error retrieving Subjects from subject.db')
        subject = Subject.Subject(1, create_subject_form.title.data, create_subject_form.description.data, create_subject_form.price.data,
                                  create_subject_form.level.data)
        if len(subject_dict) != 0 and subject.get_subject_id() <= int(list(subject_dict.keys())[-1]):
            subject.set_subject_id(int(list(subject_dict.keys())[-1]) + 1)
            subject_dict[subject.get_subject_id()] = subject
        else:
            subject_dict[subject.get_subject_id()] = subject

        subject_dict[subject.get_subject_id()] = subject

        db['Subjects'] = subject_dict
        db.close()

        return redirect(url_for('retrieve_subjects'))
    return render_template('createSubject.html', form=create_subject_form)


@app.route('/retrieveSubjects')
def retrieve_subjects():
    subject_dict = {}
    db = shelve.open('subject.db', 'r')
    subject_dict = db['Subjects']
    db.close()

    subjects_list = []
    for key in subject_dict:
        subject = subject_dict.get(key)
        subjects_list.append(subject)

    return render_template('retrieveSubjects.html', count=len(subjects_list), subjects_list=subjects_list)


@app.route('/updateSubject/<int:id>/', methods=['GET', 'POST'])
def update_subjects(id):
    update_subject_form = CreateSubjectForm(request.form)
    if request.method == 'POST' and update_subject_form.validate():
        subject_dict = {}
        db = shelve.open('subject.db', 'w')
        subject_dict = db['Subjects']

        subject = subject_dict.get(id)
        subject.set_title(update_subject_form.title.data)
        subject.set_description(update_subject_form.description.data)
        subject.set_level_id(update_subject_form.level.data)

        db['Subjects'] = subject_dict
        db.close()
        return redirect(url_for('retrieve_subjects'))
    else:
        subject_dict = {}
        db = shelve.open('subject.db', 'r')
        subject_dict = db['Subjects']
        db.close()

        subject = subject_dict.get(id)
        update_subject_form.title.data = subject.get_title()
        update_subject_form.description.data = subject.get_description()
        update_subject_form.level.data = subject.get_level_id()

        return render_template('updateSubject.html', form=update_subject_form)


@app.route('/deleteSubject/<int:id>', methods=['POST'])
def delete_subject(id):
    subject_dict = {}
    db = shelve.open('subject.db', 'w')
    subject_dict = db['Subjects']
    subject_dict.pop(id)
    db['Subjects'] = subject_dict
    db.close()

    return redirect(url_for('retrieve_subjects'))



@app.route('/createTeacher', methods=['GET', 'POST'])
def create_teacher():
    create_teacher_form = CreateStudentForm(request.form)
    if request.method == 'POST' and create_teacher_form.validate():
        teacher_dict = {}
        db =shelve.open('teacher.db', 'c')
        try:
            teacher_dict = db['Teachers']

        except:
            print('Error retrieving Teachers from teacher.db')
        import Teacher
        teacher = Teacher.Teacher(create_teacher_form.first_name.data, create_teacher_form.last_name.data, create_teacher_form.gender.data, 1, create_teacher_form.email.data, create_teacher_form.date_joined.data, create_teacher_form.address.data,create_teacher_form.subject1.data, create_teacher_form.subject2.data, create_teacher_form.subject3.data, create_teacher_form.subject4.data)
        if len(teacher_dict) != 0 and teacher.get_teacher_id() <= int(list(teacher_dict.keys())[-1]):
            teacher.set_teacher_id(int(list(teacher_dict.keys())[-1]) + 1)
            teacher_dict[teacher.get_teacher_id()] = teacher
        else:
            teacher_dict[teacher.get_teacher_id()] = teacher

        db['Teachers'] = teacher_dict
        db.close()

        subject_teacher_dict = {}
        db = shelve.open('subject_teacher.db', 'c')
        try:
            subject_teacher_dict = db['SubjectTeachers']

        except:
            print('Error retrieving Subject Teachers from subject_teacher.db')

        subject_teacher = SubjectTeacher.SubjectTeacher(1, teacher.get_teacher_id(),
                                                        int(create_teacher_form.subject1.data))
        if len(subject_teacher_dict) != 0 and subject_teacher.get_subject_teacher_id() <= int(
                list(subject_teacher_dict.keys())[-1]):
            subject_teacher.set_subject_teacher_id((int(list(subject_teacher_dict.keys())[-1]) + 1))
            subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher
        else:
            subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher

        if create_teacher_form.subject2.data != 'N':
            subject_teacher = SubjectTeacher.SubjectTeacher(1, teacher.get_teacher_id(),
                                                            int(create_teacher_form.subject2.data))
            if len(subject_teacher_dict) != 0 and subject_teacher.get_subject_teacher_id() <= int(
                    list(subject_teacher_dict.keys())[-1]):
                subject_teacher.set_subject_teacher_id((int(list(subject_teacher_dict.keys())[-1]) + 1))
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher
            else:
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher

        if create_teacher_form.subject3.data != 'N':
            subject_teacher = SubjectTeacher.SubjectTeacher(1, teacher.get_teacher_id(),
                                                            int(create_teacher_form.subject3.data))
            if len(subject_teacher_dict) != 0 and subject_teacher.get_subject_teacher_id() <= int(
                    list(subject_teacher_dict.keys())[-1]):
                subject_teacher.set_subject_teacher_id((int(list(subject_teacher_dict.keys())[-1]) + 1))
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher
            else:
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher

        if create_teacher_form.subject4.data != 'N':
            subject_teacher = SubjectTeacher.SubjectTeacher(1, teacher.get_teacher_id(),
                                                            int(create_teacher_form.subject2.data))
            if len(subject_teacher_dict) != 0 and subject_teacher.get_subject_teacher_id() <= int(
                    list(subject_teacher_dict.keys())[-1]):
                subject_teacher.set_subject_teacher_id((int(list(subject_teacher_dict.keys())[-1]) + 1))
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher
            else:
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher

        db['SubjectTeachers'] = subject_teacher_dict
        db.close()

        return redirect(url_for('teacherHomePage'))
    return render_template('createTeacher.html', form=create_teacher_form)

@app.route('/retrieveTeachers')
def retrieve_teachers():
    teacher_dict = {}
    db = shelve.open('teacher.db', 'r')
    teacher_dict = db['Teachers']
    db.close()

    teacher_list = []
    for key in teacher_dict:
        teacher = teacher_dict.get(key)
        teacher_list.append(teacher)

    return render_template('retrieveTeachers.html', count=len(teacher_list), teacher_list=teacher_list)

@app.route('/updateTeacher/<int:id>/', methods=['GET', 'POST'])
def update_teachers(id):
    update_teacher_form = CreateStudentForm(request.form)
    if request.method == 'POST' and update_teacher_form.validate():
        teacher_dict = {}
        db = shelve.open('teacher.db', 'w')
        teacher_dict = db['teachers']

        teacher = teacher_dict.get(id)
        teacher.set_first_name(update_teacher_form.first_name.data)
        teacher.set_last_name(update_teacher_form.last_name.data)
        teacher.set_gender(update_teacher_form.gender.data)
        teacher.set_email(update_teacher_form.email.data)
        teacher.set_date_joined(update_teacher_form.date_joined.data)
        teacher.set_address(update_teacher_form.address.data)

        db['teachers'] = teacher_dict
        db.close()
        return redirect(url_for('retrieve_teacher'))
    else:
        teacher_dict = {}
        db = shelve.open('teacher.db', 'r')
        teacher_dict = db['Teachers']
        db.close()

        teacher = teacher_dict.get(id)
        teacher.set_first_name(update_teacher_form.first_name.data)
        teacher.set_last_name(update_teacher_form.last_name.data)
        teacher.set_gender(update_teacher_form.level.data)
        teacher.set_email(update_teacher_form.email.data)
        teacher.set_date_joined(update_teacher_form.date_joined.data)
        teacher.set_address(update_teacher_form.address.data)

        return render_template('updateTeacher.html', form=update_teacher_form)

@app.route('/deleteTeacher/<int:id>', methods=['POST'])
def delete_teacher(id):
    teacher_dict = {}
    db = shelve.open('teacher.db', 'w')
    teacher_dict = db['Teachers']
    teacher_dict.pop(id)
    db['Teachers'] = teacher_dict
    db.close()

    return redirect(url_for('retrieve_teacher'))


@app.route('/createWithdrawal', methods=['GET', 'POST'])

def create_withdrawal():
    create_withdrawal_form = CreateWithdrawalForm(request.form)
    if request.method == 'POST' and create_withdrawal_form.validate():
        withdrawal_dict = {}
        db = shelve.open('withdrawal.db', 'c')

        try:
            withdrawal_dict = db['Withdrawals']

        except:
            print('Error retrieving Withdrawal Applications from Withdrawal.db')
        import Withdrawal
        withdrawal = Withdrawal.Withdrawal(1, create_withdrawal_form.first_name.data, create_withdrawal_form.last_name.data, create_withdrawal_form.level.data, create_withdrawal_form.subject.data, create_withdrawal_form.reason.data,create_withdrawal_form.feedback.data,
                                           create_withdrawal_form.ack.data)
        if len(withdrawal_dict) != 0 and withdrawal.get_withdrawal_id() <= int(list(withdrawal_dict.keys())[-1]):
            withdrawal.set_withdrawal_id(int(list(withdrawal_dict.keys())[-1]) + 1)
            withdrawal_dict[withdrawal.get_withdrawal_id()] = withdrawal
        else:
            withdrawal_dict[withdrawal.get_withdrawal_id()] = withdrawal

        withdrawal_dict[withdrawal.get_withdrawal_id()] = withdrawal

        db['Withdrawals'] = withdrawal_dict
        db.close()

        return redirect(url_for('studentHomePage'))
    return render_template('createWithdrawal.html', form=create_withdrawal_form)


@app.route('/retrieveWithdrawals', )
def retrieve_withdrawals():
    withdrawal_dict = {}
    db = shelve.open('withdrawal.db', 'r')
    withdrawal_dict = db['Withdrawals']
    db.close()

    withdrawal_list = []
    for key in withdrawal_dict:
        withdrawal = withdrawal_dict.get(key)
        withdrawal_list.append(withdrawal)


    return render_template('retrieveWithdrawals.html', count=len(withdrawal_list), withdrawal_list=withdrawal_list)

@app.route('/deleteWithdrawal/<int:id>', methods=['POST'])
def delete_withdrawal(id):
    withdrawal_dict = {}
    db = shelve.open('withdrawal.db', 'w')
    withdrawal_dict = db['Withdrawals']
    withdrawal_dict.pop(id)
    db['Withdrawals'] = withdrawal_dict
    db.close()





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









@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

if __name__ == '__main__':
    app.run()
