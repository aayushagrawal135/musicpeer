from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()

#engine = create_engine('sqlite:///pci.db')
#Base.metadata.bind = engine

#DBSession = sessionmaker(bind=engine)
#session = DBSession()

root_url = "http://ws.audioscrobbler.com/2.0/"
API_KEY = "a0b8a0a745497e69b39e4815af5e923d"

# routes will contain the maping of urls and the function (view functions) to be executed correspondingly
from myApp import routes, models
