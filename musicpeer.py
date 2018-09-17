# a top-level scipt importing the application instance assists to run
from myApp import app
from myApp.models import User

if _name_ == '_main_':
    app.run(host = '0.0.0.0',port = '5000')
#@app.shell_context_processor
#def make_shell_context():
#    return {'db': db, 'User': User}
