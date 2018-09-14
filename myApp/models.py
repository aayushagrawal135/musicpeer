from myApp import db, login
from datetime import datetime
from hashlib import sha256
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    logs = db.relationship('History', backref='User', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = sha256(password.encode()).hexdigest()

    def check_password(self, password):
        recvd_password_hash = sha256(password.encode()).hexdigest()
        if self.password_hash == recvd_password_hash:
            return True
        else:
            return False

    def __repr__(self):
        return '<User {}>'.format(self.username)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('user.username'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '{}'.format(self.body)

# loads a user object from its object ID
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    body = db.Column(db.String(140))
#    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#    def __repr__(self):
#        return '<Post {}>'.format(self.body)
