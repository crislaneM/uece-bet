from flask import Flask
from flask_sqlalchemy import SQLALCHEMY
from flask_marshmallow import Marsmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://dev:postgres@localhost:5432/uecebet'
app.config['SECRET_KEY'] = 'secret'

db= SQLALCHEMY(app)
ma= Marshmallow(app) 
