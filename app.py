from flask import Flask
from Flask import Blueprint
from . import db
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired
from werkzeug.utils import secure_filename
from sqlalchemy_orm import DeclarativeBase
import hashlib
#import der Bibliotheken


db = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)
# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)


main = Blueprint('main', __name__)


@app.route("/")
def welcome():
    return "<p>Hello, please Login!</p>"

@app.route("login", methods=['GET','POST'])
def login():
    return "<p>Hello</p>"


def checkform(LoginForm):
     return None

class LoginForm(FlaskForm):
    username = StringField('username', validators =[FileRequired()])
    password = FileField('password', validators=[FileRequired])