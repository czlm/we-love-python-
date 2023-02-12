from app import db
from flask_login import UserMixin

class teacher(UserMixin, db.Model):
    __tablename__ = "teacher"

    id = db.Column(db.Integer, primary_key=True)
    admin_number = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, name, email, pwd,admin_number):

        self.name = name
        self.email = email
        self.password = pwd
        self.admin_number = admin_number
