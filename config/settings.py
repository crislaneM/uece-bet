from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config.variables import ConfigBancoDados

user = ConfigBancoDados.user_db
password = ConfigBancoDados.password_db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@localhost:5432/uecebet'
app.config['SECRET_KEY']='thisissecret'

api = Api()
api.init_app(app)

jwt = JWTManager(app)
jwt.init_app(app)

db = SQLAlchemy(app)
