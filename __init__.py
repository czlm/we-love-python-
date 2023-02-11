from flask import Flask, render_template, request, redirect, url_for, session
from Forms import CreateUserForm, CreateGradeForm, CreateAnnouncementForm, CreateProgressreportForm, CreateTeacherForm, CreateQuizForm
import shelve, User, Grade, Announcement, Progressreport, Teacher, Quiz
from datetime import datetime

from werkzeug.utils import secure_filename



app = Flask(__name__)
app.secret_key = 'any_random_string'

@app.route('/')
def guest_home_page():
    return render_template('ghome.html')

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




@app.route('/createTeacher', methods=['GET', 'POST'])
def create_teacher():
    subjects = ['English', 'Math', 'Science', 'Chinese']
    create_teacher_form = CreateTeacherForm(request.form)
    if request.method == 'POST':
        teachers_dict = {}
        # print(request.form.getlist('mycheckbox')) #returns subjects in a python list
        db = shelve.open('teacher.db', 'c')

        try:
            if 'Teachers' in db:
                teachers_dict = db['Teachers']
            else:
                db['Teachers'] = teachers_dict
        except:
            print("Error in retrieving Teachers from teacher.db.")

        teacher = Teacher.Teacher(create_teacher_form.first_name.data, create_teacher_form.last_name.data, create_teacher_form.gender.data, request.form.getlist('mycheckbox'),
                         create_teacher_form.email.data, create_teacher_form.date_joined.data, create_teacher_form.address.data, create_teacher_form.subject.data)
        teachers_dict[teacher.get_teacher_id()] = teacher

        db['Teachers'] = teachers_dict

        db.close()

        session['teacher_created'] = teacher.get_first_name() + ' ' + teacher.get_last_name()

        return redirect(url_for('teacherHomePage'))
    return render_template('createTeacher.html', form=create_teacher_form, subjects=subjects)


@app.route('/retrieveTeachers')
def retrieve_teachers():
    teachers_dict = {}
    db = shelve.open('teacher.db', 'c')
    try:
        teachers_dict = db['Teachers']
    except:
        print("Error in retrieving Teachers from teacher.db.")
    db.close()

    teachers_list = []
    for key in teachers_dict:
        teacher = teachers_dict.get(key)
        teachers_list.append(teacher)

    return render_template('retrieveTeachers.html', count=len(teachers_list), teacherslist=teachers_list)


@app.route('/updateTeacher/<int:id>/', methods=['GET', 'POST'])
def update_teacher(id):
    update_teacher_form = CreateTeacherForm(request.form)
    if request.method == 'POST' and update_teacher_form.validate():
        teachers_dict = {}
        db = shelve.open('teacher.db', 'w')
        teachers_dict = db['Teachers']

        teacher = teachers_dict.get(id)
        teacher.set_first_name(update_teacher_form.first_name.data)
        teacher.set_last_name(update_teacher_form.last_name.data)
        teacher.set_gender(update_teacher_form.gender.data)
        teacher.set_email(update_teacher_form.email.data)
        teacher.set_date_joined(update_teacher_form.date_joined.data)
        teacher.set_address(update_teacher_form.address.data)
        teacher.set_subject(update_teacher_form.subject.data)


        db['Teachers'] = teachers_dict
        db.close()

        session['teacher_updated'] = teacher.get_first_name() + ' ' + teacher.get_last_name()

        return redirect(url_for('retrieve_teachers'))
    else:
        teachers_dict = {}
        db = shelve.open('teacher.db', 'r')
        teachers_dict = db['Teachers']
        db.close()

        teacher = teachers_dict.get(id)
        update_teacher_form.first_name.data = teacher.get_first_name()
        update_teacher_form.last_name.data = teacher.get_last_name()
        update_teacher_form.gender.data = teacher.get_gender()
        update_teacher_form.email.data = teacher.get_email()
        update_teacher_form.date_joined.data = teacher.get_date_joined()
        update_teacher_form.address.data = teacher.get_address()
        update_teacher_form.subject.data = teacher.get_subject()

        return render_template('updateTeacher.html', form=update_teacher_form)


@app.route('/deleteTeacher/<int:id>', methods=['POST'])
def delete_teacher(id):
    teachers_dict = {}

    db = shelve.open('teacher.db', 'w')
    teachers_dict = db['Teachers']
    teachers_dict.pop(id)
    db['Teachers'] = teachers_dict
    db.close()
    # session['teacher_deleted'] = teacher.get_first_name() + ' ' + teacher.get_last_name()

    return redirect(url_for('retrieve_teachers'))



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








@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

if __name__ == '__main__':
    app.run()
