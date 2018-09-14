from flask import render_template, flash, redirect, request, url_for
from myApp import app, db
from myApp.forms import LoginForm, RegistrationForm
from myApp.Page import ResultPage
from myApp.Artist import Artist
from myApp.models import User, History
from flask_login import logout_user, login_required, current_user, login_user
from werkzeug.urls import url_parse

@app.route('/', methods = ['GET', 'POST'])
@login_required
def start():
    print("#############started####################")
    return render_template('index.html')


# lines above the function: called decorators, they draw the conditions when the
# following function should be run
# A decorator-function for home page
@app.route('/index', methods = ['GET', 'POST'])
# a decorator/ function from the LoginManager class stating protocol that only logged in
# users can enter the following function
@login_required
def index():
    # render template lets the .html take over that is mentioned in the 1st argument
    # from 2nd argument on
    print(request.form)
    value = request.form.get('q')
    if value != None:
        #print("%%%%%%%%%%%%%%%%", value)
        page = ResultPage(value)
        page = page.get_results()
        #print("@@@@@@@@@@@@@@@@", page)
        return render_template('index.html', title='Home Page', page=page)
    else:
        return render_template('index.html', title='Home Page', page=None)


# decorator-function for Login
# methods carry what direction of passing of data can occur
# GET : server -> client, POST : client -> server
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
        user = User.query.filter_by(username=form.username.data).first()
        print(type(user))
        print(user)

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # log in the user, a boolean value recvd to form.remember_me.data is also passed
        login_user(user, remember=form.remember_me.data)

                                                                            # Doubt
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

        # load login.html page, pass the following written agruments to the html
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# protcol for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    # doubt: i dont get when this would be called since current user would never access
    # regisger button itself
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
                                                                                # Doubt
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        # all the flash messages are stored in a buffer like context named 'g'
        flash('Congratulations, you are now a registered user!')
        # if registration is successful go to login
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/clicked_artist_details/<query>', methods=['GET', 'POST'])
@login_required
def clicked_artist_details(query):
    log = History(username=current_user, body=query)
    #db.session.add(log)
    #db.session.commit()
    print('Log added')
    artist = Artist(query)
    return render_template('clicked_artist_details.html', artist=artist)

@app.route('/search_history')
def search_history():
    return render_template('search_history.html')
