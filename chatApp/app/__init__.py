from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///user.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'pass'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True

from app import routes 