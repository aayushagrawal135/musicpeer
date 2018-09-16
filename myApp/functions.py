import datetime
import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from myApp.models import User, Log
#from myApp import Base
from flask import flash
from hashlib import sha256
from myApp import db

def is_valid_User(session, data):
    key = sha256(data['password'].encode()).hexdigest()
    res = db.session.query(User).filter(User.username==data['username'], User.password_hash==key).first()
    return res


def is_new_User(session, data):
    res1 = db.session.query(User).filter(User.username==data['username']).all()
    res2 = db.session.query(User).filter(User.email==data['email']).all()
    if len(res1)>0 or len(res2)>0:
        return False
    else:
        return True

def insert_User(session, data):
    print("YOOOOOOOOOO", data)
    new = User(id = data['id'], username = data['username'], email=data['email'], password_hash=data['password'])
    db.session.add(new)
    db.session.commit()
    flash("Congratulations, you are a registered user now")

def insert_Log(session, data):
    print("aaaaaaaaaaaaaaaaa", data)
    new = Log(id = data['id'], username = data['username'], query = data['query'])
    print(new)
    db.session.add(new)
    db.session.commit()

def delete_User(seesion, data):
    old = db.session.query(User).filter(User.username == data['username'], User.password == data['password']).all()
    db.session.delete(old)
    db.session.commit()

def delete_Log(session, user):
    old = db.session.query(Log).filter(Log.username==user).all()
    for i in range(len(old)):
        db.session.delete(old[i])
    db.session.commit()

def list_user_Logs(session, username):
    log_list = []
    for log in session.query(Log).filter(Log.username==username).all():
        log_list.append((log.username, log.query))
    return log_list

def get_next_userid(session):
    data = db.session.query(User).all()
    return len(data)+1

def get_next_logid(session):
    data = db.session.query(Log).all()
    return len(data)+1

# ------------------------------------------------------

def delete_all_Log(session):
    old = db.session.query(Log).all()
    for i in range(len(old)):
        db.session.delete(old[i])
    db.session.commit()

def delete_all_User(session):
    old = db.session.query(User).all()
    for i in range(len(old)):
        db.session.delete(old[i])
    db.session.commit()


    #return log_list

def list_all_Logs(session):
    log_list = db.session.query(Log).all()
    return log_list

def list_all_Users(session):
    user_list = db.session.query(User).all()
    return user_list
