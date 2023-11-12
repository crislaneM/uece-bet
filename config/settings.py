from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.variables import ConfigBancoDados

user = ConfigBancoDados.user_db
password = ConfigBancoDados.password_db

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@localhost:5432/uecebet'

db = SQLAlchemy(app)
