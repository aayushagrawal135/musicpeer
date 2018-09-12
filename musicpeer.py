# a top-level scipt importing the application instance assists to run
from myApp import app, db
from myApp.models import User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
