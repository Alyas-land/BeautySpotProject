from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy()


# Insert Database Folder for DB file
base_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(base_dir, '..', 'infrastructure', 'database', 'project.db')


# config Secret key
app.config['SECRET_KEY'] = '29f2b5b30b255de80ff08b80fb4394479d5f9b88b2b6c8899cf25f394edbca312586c4972018a2fc'
#cinfig Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'

db.init_app(app)
