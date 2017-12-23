from sqlalchemy import Column, Float,Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    phone = Column(String(80), unique=True, nullable=False)
    account = Column(Float,nullable=True)
    sms =  Column(String(80),nullable=True)

    def __init__(self, username=None, password=None, phone = None, sms = "",account=0):
        self.username = username
        self.password = password
        self.phone = phone
        self.sms = sms
        self.account = account

    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return (self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)


# print("Hello from models")


# from runapp import app
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password_hash = db.Column(db.String(120), nullable=False)
#     phone = db.Column(db.String(80), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username


# print("Hello from models")