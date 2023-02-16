from flask import Flask, render_template, request, redirect, url_for

import Student
import SubjectStudent
import SubjectTeacher
from Forms import *
import shelve, Subject

app = Flask(__name__)
app.config['SECRET_KEY'] =  'secret_key'
app.config['WTF_CSRF_SECRET_KEY'] = 'csrf_secret_key'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/teacherHomePage')
def teacher_home_page():
    return render_template('teacherHomePage.html')

@app.route('/ghome')
def guest_home_page():
    return render_template('ghome.html')

@app.route('/english')
def english_page():
    return render_template('english.html')



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

@app.route('/createStudent', methods=['GET', 'POST'])
def create_student():
    create_student_form = CreateStudentForm(request.form)
    if request.method == 'POST' and create_student_form.validate():
        student_dict = {}
        db = shelve.open('student.db', 'c')

        try:
            student_dict = db['Students']

        except:
            print('Error retrieving Students from student.db')
        student = Student.Student(create_student_form.first_name.data, create_student_form.last_name.data,
                                  create_student_form.gender.data, 1, create_student_form.email.data,
                                  create_student_form.date_joined.data, create_student_form.address.data,
                                  create_student_form.level.data, create_student_form.subject1.data,
                                  create_student_form.subject2.data, create_student_form.subject3.data,
                                  create_student_form.subject4.data)
        if len(student_dict) != 0 and student.get_student_id() <= int(list(student_dict.keys())[-1]):
            student.set_student_id(int(list(student_dict.keys())[-1]) + 1)
            student_dict[student.get_student_id()] = student
        else:
            student_dict[student.get_student_id()] = student

        db['Students'] = student_dict
        db.close()

        subject_student_dict = {}
        db = shelve.open('subject_student.db', 'c')

        try:
            subject_student_dict = db['SubjectStudents']
        except:
            print('Error retrieving SubjectStudents from subject_student.db')


        subject_student = SubjectStudent.SubjectStudent(1, student.get_student_id(), int(create_student_form.subject1.data))
        if len(subject_student_dict) != 0 and subject_student.get_subject_student_id() <= int(
                list(subject_student_dict.keys())[-1]):
            subject_student.set_subject_student_id((int(list(subject_student_dict.keys())[-1]) + 1))
            subject_student_dict[subject_student.get_subject_student_id()] = subject_student
        else:
            subject_student_dict[subject_student.get_subject_student_id()] = subject_student

        if create_student_form.subject2.data != 'N':
            subject_student = SubjectStudent.SubjectStudent(1, student.get_student_id(),
                                                        int(create_student_form.subject2.data))
            if len(subject_student_dict) != 0 and subject_student.get_subject_student_id() <= int(list(subject_student_dict.keys())[-1]):
                subject_student.set_subject_student_id((int(list(subject_student_dict.keys())[-1]) + 1))
                subject_student_dict[subject_student.get_subject_student_id()] = subject_student
            else:
                subject_student_dict[subject_student.get_subject_student_id()] = subject_student

        if create_student_form.subject3.data != 'N':
            subject_student = SubjectStudent.SubjectStudent(1, student.get_student_id(),
                                                        int(create_student_form.subject3.data))
            if len(subject_student_dict) != 0 and subject_student.get_subject_student_id() <= int(list(subject_student_dict.keys())[-1]):
                subject_student.set_subject_student_id((int(list(subject_student_dict.keys())[-1]) + 1))
                subject_student_dict[subject_student.get_subject_student_id()] = subject_student
            else:
                subject_student_dict[subject_student.get_subject_student_id()] = subject_student

        if create_student_form.subject4.data != 'N':
            subject_student = SubjectStudent.SubjectStudent(1, student.get_student_id(),
                                                        int(create_student_form.subject2.data))
            if len(subject_student_dict) != 0 and subject_student.get_subject_student_id() <= int(list(subject_student_dict.keys())[-1]):
                subject_student.set_subject_student_id((int(list(subject_student_dict.keys())[-1]) + 1))
                subject_student_dict[subject_student.get_subject_student_id()] = subject_student
            else:
                subject_student_dict[subject_student.get_subject_student_id()] = subject_student

        db['SubjectStudents'] = subject_student_dict
        db.close()

        return redirect(url_for('home'))
    return render_template('createStudent.html', form=create_student_form)

@app.route('/retrieveStudents')
def retrieve_students():
    student_dict = {}
    db = shelve.open('student.db', 'r')
    student_dict = db['Students']
    db.close()

    subject_student_dict = {}
    db = shelve.open('subject_student.db', 'r')
    subject_student_dict = db['SubjectStudents']
    db.close()

    students_list = []
    for key in student_dict:
        student = student_dict.get(key)
        students_list.append(student)

    # Convert the subject-student dictionary into a list
    subject_student_list = []
    for key in subject_student_dict:
        ss = subject_student_dict.get(key)
        subject_student_list.append(ss)

    return render_template('retrieveStudents.html', student_count=len(students_list), students_list=students_list,
                           subject_student_count=len(subject_student_list), subject_student_list=subject_student_list)


@app.route('/updateStudent/<int:id>/', methods=['GET', 'POST'])
def update_students(id):
    update_student_form = CreateStudentForm(request.form)
    if request.method == 'POST' and update_student_form.validate():
        student_dict = {}
        db = shelve.open('student.db', 'w')
        student_dict = db['Students']

        student = student_dict.get(id)
        student.set_first_name(update_student_form.first_name.data)
        student.set_last_name(update_student_form.last_name.data)
        student.set_gender(update_student_form.gender.data)
        student.set_email(update_student_form.email.data)
        student.set_date_joined(update_student_form.date_joined.data)
        student.set_address(update_student_form.address.data)

        db['Students'] = student_dict
        db.close()
        return redirect(url_for('retrieve_students'))
    else:
        student_dict = {}
        db = shelve.open('student.db', 'r')
        student_dict = db['Students']
        db.close()

        student = student_dict.get(id)
        student.set_first_name(update_student_form.first_name.data)
        student.set_last_name(update_student_form.last_name.data)
        student.set_gender(update_student_form.level.data)
        student.set_email(update_student_form.email.data)
        student.set_date_joined(update_student_form.date_joined.data)
        student.set_address(update_student_form.address.data)

        return render_template('updateStudents.html', form=update_student_form)

@app.route('/deleteStudent/<int:id>', methods=['POST'])
def delete_student(id):
    student_dict = {}
    db = shelve.open('student.db', 'w')
    student_dict = db['Subjects']
    student_dict.pop(id)
    db['Students'] = student_dict
    db.close()

    return redirect(url_for('retrieve_students'))

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
                                                        create_teacher_form.subject1.data)
        if len(subject_teacher_dict) != 0 and subject_teacher.get_subject_teacher_id() <= int(
                list(subject_teacher_dict.keys())[-1]):
            subject_teacher.set_subject_teacher_id((int(list(subject_teacher_dict.keys())[-1]) + 1))
            subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher
        else:
            subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher

        if create_teacher_form.subject2.data != 'N':
            subject_teacher = SubjectTeacher.SubjectTeacher(1, teacher.get_teacher_id(),
                                                            create_teacher_form.subject2.data)
            if len(subject_teacher_dict) != 0 and subject_teacher.get_subject_teacher_id() <= int(
                    list(subject_teacher_dict.keys())[-1]):
                subject_teacher.set_subject_teacher_id((int(list(subject_teacher_dict.keys())[-1]) + 1))
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher
            else:
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher

        if create_teacher_form.subject3.data != 'N':
            subject_teacher = SubjectTeacher.SubjectTeacher(1, teacher.get_teacher_id(),
                                                            create_teacher_form.subject3.data)
            if len(subject_teacher_dict) != 0 and subject_teacher.get_subject_teacher_id() <= int(
                    list(subject_teacher_dict.keys())[-1]):
                subject_teacher.set_subject_teacher_id((int(list(subject_teacher_dict.keys())[-1]) + 1))
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher
            else:
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher

        if create_teacher_form.subject4.data != 'N':
            subject_teacher = SubjectTeacher.SubjectTeacher(1, teacher.get_teacher_id(),
                                                            create_teacher_form.subject2.data)
            if len(subject_teacher_dict) != 0 and subject_teacher.get_subject_teacher_id() <= int(
                    list(subject_teacher_dict.keys())[-1]):
                subject_teacher.set_subject_teacher_id((int(list(subject_teacher_dict.keys())[-1]) + 1))
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher
            else:
                subject_teacher_dict[subject_teacher.get_subject_teacher_id()] = subject_teacher

        db['SubjectTeachers'] = subject_teacher_dict
        db.close()

        return redirect(url_for('home'))
    return render_template('createTeacher.html', form=create_teacher_form)

@app.route('/retrieveTeacher')
def retrieve_teachers():
    teacher_dict = {}
    db = shelve.open('teacher.db', 'r')
    teacher_dict = db['Teachers']
    db.close()

    teacher_list = []
    for key in teacher_dict:
        teacher = teacher_dict.get(key)
        teacher_list.append(teacher)

    return render_template('retrieveTeacher.html', count=len(teacher_list), teacher_list=teacher_list)

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

        return redirect(url_for('retrieve_withdrawals'))
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

    return redirect(url_for('retrieve_withdrawal'))
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
        if len(quiz_dict) == 0:
            quiz.set_quiz_id(1)
        else:
            quiz.set_quiz_id(max(quiz_dict.keys()) + 1)

        quiz_dict[quiz.get_quiz_id()] = quiz

        db['Quizzes'] = quiz_dict
        db.close()
        return redirect(url_for('home'))
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
        return redirect(url_for('home'))
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
        return redirect(url_for('home'))
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

    qn_dict = {}
    db = shelve.open('quiz.db','r')
    qn_dict = db['Quizzes']
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
    if quiz is not None:
        qn_list.append(quiz)
    else:
        return f"No quiz found with id {id}"

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
        return redirect(url_for('home'))
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
        return redirect(url_for('home'))
    return render_template('markAnswer.html', form=create_score_form)


if __name__ == '__main__':
    app.run()
