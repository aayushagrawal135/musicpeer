from flask import render_template, flash, redirect, request, url_for
from myApp import app
from myApp.forms import LoginForm, RegistrationForm
from myApp.Page import ResultPage
from myApp.Artist import Artist
from myApp.TrackList import TrackList
from myApp.models import User, Log
from flask_login import logout_user, login_required, current_user, login_user
from werkzeug.urls import url_parse
from myApp.functions import insert_User, get_next_userid, is_new_User, is_valid_User
from myApp.functions import insert_Log, get_next_logid, list_user_Logs, list_all_Logs, delete_user_Log
#from myApp import session
from myApp import db
from datetime import datetime

# GET : server -> client, POST : client -> server
@app.route('/', methods = ['GET', 'POST'])
@login_required
def start():
    print("#############started####################")
    return render_template('index.html')


@app.route('/index', methods = ['GET', 'POST'])
@login_required
def index():
    # value comes from search-bar located in base.html
    value = request.form.get('q')
    if value != None:
        page = ResultPage(value)
        page = page.get_results()
        return render_template('index.html', title='Home Page', page=page)
    else:
        return render_template('index.html', title='Home Page', page=None)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # states that the current user has provided correct credentials : Doubt
    if current_user.is_authenticated:
        # all good? redirect to index/home page
        return redirect(url_for('index'))
    form = LoginForm()
    # checks if the conditions specified in LoginForm are met
    if form.validate_on_submit():
        # if username-password pair fails: redirect to same page, login again
        data = {}
        data['username'] = form.username.data
        data['password'] = form.password.data
        user = is_valid_User(db.session, data)

        if user == None:
            flash('Invalid username or password')
            return redirect(url_for('login'))

        # store log in the user, a boolean value recvd to form.remember_me.data is also passed
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
            print("next page her -> ", next_page)
        return redirect(next_page)

    # load login.html page, pass the following written agruments to the html
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    #db.session.clear()
    logout_user()
    return redirect(url_for('index'))


# protcol for registration
@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        data = {}
        data['username'] = form.username.data
        data['email'] = form.email.data
        if is_new_User(db.session, data):
            newUser = {}
            newUser['id'] = get_next_userid(db.session)                                                                        # Doubt
            newUser['username'] = form.username.data
            newUser['email'] = form.email.data
            newUser['password'] = User.set_password(form.password.data)
            insert_User(db.session, newUser)

            return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

# dynamic queries are made by appending like this in the route decorator
@app.route('/clicked_artist_details/<query>', methods=['GET', 'POST'])
@login_required
def clicked_artist_details(query):
    # tracks of the clicked artist
    list_tracks = TrackList(query)
    list_tracks = list_tracks.get_results()

    # collecting the search- store in database
    data = {}
    data['id'] = get_next_logid(db.session)
    data['username'] = current_user.username
    data['query'] = query
    #data['timestamp'] = datetime.utcnow()
    insert_Log(db.session, data)

    # get artist object from Artist.getInfo API call inside
    artist = Artist(query)
    return render_template('clicked_artist_details.html', artist=artist, list_tracks=list_tracks)

@app.route('/search_history')
def search_history():
    log_list = list_user_Logs(db.session, current_user.username)
    print(log_list)
    return render_template('search_history.html', log_list=log_list)

@app.route('/clear_search_history')
def clear_search_history():
    print(current_user.username)
    delete_user_Log(db.session, current_user.username)
    log_list = list_user_Logs(db.session, current_user.username)
    print(log_list)
    return render_template('search_history.html', log_list=log_list)
