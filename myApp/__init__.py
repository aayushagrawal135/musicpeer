from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# initialize an instace of flask: all the client request that comes to server, will pass through
# this instance, it will then make decisions to address the request
app = Flask(__name__)

# LoginManager takes care of/ provides many functions related to Login feature
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# routes will contain the maping of urls and the function (view functions) to be executed correspondingly
from myApp import routes, models
