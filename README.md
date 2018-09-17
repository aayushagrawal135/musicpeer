## Project Title

Flask-Python based Web application - Music Peer

### Basics

Parameters are passed between HTML to Python by url_for method, from Python to HTML while calling render_template. Jinja has {% <declarative command> %} and {{<variable name>}} which facilitate accessing, looping over parameters in HTML.

For HTML page rendering, Navbar is made in the _base.html_ and all the pages will inherit that from it so that duplication can be avoided and uniformity be maintained. This is facilitated by a {% block <blockname> %}{% endblock %} tag.

Every HTML page has a mapping with a function which is supposed to run when the particular HTML file is rendered. In the project these functions are mentioned in routes.py. These url corresponding to functions are also called decorators. They act like a protocol for entering into a function. Other protocols can also be added, like _login_required_ which is implicit.

For database, finally, SQLAlchemy's flask extensions is used. Tuples are accessed as if objects. Classes/Tables for the same are mentioned in models.py. Functions enabling operations on the database tables are written in _functions.py_.

### Getting Started

At the crux, there are features like:
* login-logout based on credentials (flask_login, flask_sqlalchemy)
  * sign in form (flask_wtf)
  * sign up form
* a search bar (taking music artist as input)
* API calling for pulling data (LastFM)
  * Artist list
  * Individual aritist: Bio, images, tracks, similar artists, etc
* Storing, clearing search history of users only when logged in (flask_sqlalchemy)

### Installing

Python 3.4+
pip install flask
pip install python-dotenv
pip install flask_wtf
pip install requests
pip install flask_migrate
pip install flask_wtf
pip install flask_sqlalchemy
pip install flask_login

## Running the tests

python3 -m venv <venv name>
source "v-environment name"/bin/activate
export FLASK_APP=musicpeer.py
FLASK_APP=musicpeer.py
flask run

In the working directory, running the command, _sqlite3 <database name>_ opens that that database in CLI,
now SQL queries can be used to maintain, build tables

### Helpful References

[Miguel Grinberg's Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
[Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/)
[Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/quickstart/)
[Flask-SQLAlchemy](https://media.readthedocs.org/pdf/flask-sqlalchemy/latest/flask-sqlalchemy.pdf)
[LastFM API](https://www.last.fm/api)

## Instructions to deploy on AWS EC2

1. Create an EC2 instance using the UI after you login to the AWS Cloud infrastructure.
2. Created Ubuntu 16.04 Linux box for the deployment purpose of the App.
3. Connect to the instance from the local machine(my machine was Linux) using the below command on terminal
ssh -i "privatefilename.pem" ubuntu@ec2-34-215-78-135.us-west-2.compute.amazonaws.com
4. In the above command privatefilename.pem is used as key-pair which behaves as a password to access the instance.
5. 'ubuntu' is the username and rest is the host url
6. Install git using the below command
sudo apt-get update
sudo apt-get install git
7. Clone the repository
git clone https://github.com/aayushagrawal135/musicpeer.git
8. Install python3 pip using below command
sudo apt-get install -y python3-pip
9. Install the dependencies of python module
  1. flask
  2. flask_migrate'
  3. flask_wtf
  4. flask_sqlalchemy
  5. flask_login
10. Run the application using the below command
cd musicpeer
source venv/bin/activate
export FLASK_APP=musicpeer.py
python3 musicpeer.py
11. To make the url of the application available to everyone allow the rule in AWS to Protocol:TCP. Access the url http://ec2-34-215-78-135.us-west-2.compute.amazonaws.com:5000 to naviagte to the URL.




