from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_login import UserMixin,login_user,LoginManager,current_user,logout_user,login_required
from datetime import timedelta
from sqlalchemy.exc import IntegrityError,DataError,DatabaseError,InterfaceError,InvalidRequestError
from werkzeug.routing import BuildError
from flask_bcrypt import Bcrypt,generate_password_hash, check_password_hash
from app import create_app,db,login_manager,bcrypt
from models import User
from teachermodels import teacher
from forms import login_form,register_form
from teacherforms import teacher_login_form,register_form


app = create_app()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.user_loader
def load_user(user_id):
    return teacher.query.get(int(user_id))


@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index3.html",title="Home")

@app.route("/teacher", methods=("GET", "POST"), strict_slashes=False)
def index1():
    return render_template("teacherindex.html",title="Home")


@app.route("/loginstudent/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return render_template("index.html")
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("auth.html",
        form=form,
        text="Student login",
        title="Login",
        btn_action="Login"
        )



# Register route
@app.route("/registerstudent", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = register_form()
    if form.validate_on_submit():
        try:
            username = form.username.data
            email = form.email.data
            pwd = form.pwd.data

            newuser = User(
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )

            db.session.add(newuser)
            db.session.commit()
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("login"))

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"User already exists!.", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured !", "danger")

    return render_template("auth.html",
        form=form,
        text="Create student account",
        title="Register",
        btn_action="Register account"
        )

@app.route("/loginteacher/", methods=("GET", "POST"), strict_slashes=False)
def teacherlogin():
    form = teacher_login_form()

    if form.validate_on_submit():
        try:
            user = teacher.query.filter_by(admin_number=form.admin_number.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('index1'))
            else:
                flash("Invalid Username or password!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("teacherauth.html",
        form=form,
        text="Teacher login",
        title="Login",
        btn_action="Login"
        )



# Register route
@app.route("/registerteacher/", methods=("GET", "POST"), strict_slashes=False)
def teacherregister():
    form = register_form()
    if form.validate_on_submit():
        try:
            admin_number = form.admin_number.data
            email = form.email.data
            pwd = form.pwd.data
            username = form.username.data

            newteacher = teacher(
                admin_number = admin_number,
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )

            db.session.add(newteacher)
            db.session.commit()
            flash(f"Account Succesfully created", "success")
            return redirect(url_for("teacherlogin"))

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Something went wrong!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"User already exists!.", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Invalid Entry", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Error connecting to the database", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"An error occured !", "danger")

    return render_template("teacherauth.html",
        form=form,
        text="Create teacher account",
        title="Register",
        btn_action="Register account"
        )

# @app.route('/createUser', methods=['GET', 'POST'])
# def create_user():
#     create_user_form = CreateStudentForm(request.form)
#     if request.method == 'POST' and create_user_form.validate():
#
#         return redirect(url_for('index'))
#     return render_template('studentlist.html', form=create_user_form)
#
# #This is the index route where we are going to
# #query on all our employee data
# @app.route('/account_management')
# def account_management():
#     all_data = teacher.query.all()
#     return render_template("index.html", teacher = all_data)


#This is the index route where we are going to query on all our data
@app.route('/teacheraccountmanagement')
def Index1():
    all_data = teacher.query.all()

    return render_template("myclass.html", teacher = all_data)



#this route is for inserting data to mysql database via html forms
@app.route('/teacherinsert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']


        my_data = teacher(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Teacher's Inserted Successfully")

        return redirect(url_for('Index1'))

    else:
        flash("There is an error")


#this is our update route where we are going to update our employee
@app.route('/teacherupdate', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = teacher.query.get(request.form.get('id'))

        my_data.admin_number = request.form['admin_number']
        my_data.email = request.form['email']
        my_data.pwd = request.form['password']

        db.session.commit()

        db.session.commit()
        flash("Teacher's credentials have been updated successfully")

        return redirect(url_for('Index1'))

#This is the index route where we are going to query on all our data
@app.route('/studentaccountmanagement')
def Index2():
    all_data = User.query.all()

    return render_template("myclass1.html", student = all_data)



#this route is for inserting data to mysql database via html forms
@app.route('/studentinsert', methods = ['POST'])
def insert1():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']


        my_data = User(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Student's Inserted Successfully")

        return redirect(url_for('Index2'))

    else:
        flash("There is an error")


#this is our update route where we are going to update our employee
@app.route('/studentupdate', methods = ['GET', 'POST'])
def update1():

    if request.method == 'POST':
        my_data = User.query.get(request.form.get('id'))

        my_data.email = request.form['email']
        my_data.pwd = request.form['password']


        db.session.commit()
        flash("Student's credentials have been updated successfully")

        return redirect(url_for('Index2'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
