#from sqlalchemy import db.Column, ForeignKey, Integer, String, Float, DateTime, create_engine
#from sqlalchemy.orm import relationship
from myApp import login
from hashlib import sha256
from flask_login import UserMixin
#from myApp import Base
from myApp import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)


    @staticmethod
    def set_password(password):
        key = sha256(password.encode()).hexdigest()
        password_hash = key
        return key

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('user.username'))
    query = db.Column(db.String(140), nullable=False)
    #timestamp = db.Column(db.DateTime, primary_key=True)

    def __repr__(self):
        return '{}'.format(self.username)

# loads a user object from its object ID
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#class Post(db.Model):
#    id = db.db.Column(db.Integer, primary_key=True)
#    body = db.db.Column(db.String(140))
#    timestamp = db.db.Column(db.DateTime, index=True, default=datetime.utcnow)
#    user_id = db.db.Column(db.Integer, db.ForeignKey('user.id'))

#    def __repr__(self):
#        return '<Post {}>'.format(self.body)
