import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)

app.config['SECRET_KEY'] = '33c65820ed84e0d6e03e3adbfeefe7c32850ee61eed412edfcc0fab12b7833d7'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:secret@localhost:5432/flaskblog'

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 1025
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog import routes