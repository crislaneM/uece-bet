from flask import Flask
from flask_sqlalchemy import SQLAlchemy


user_db = "postgres"
password_db = "postgres"

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password_db}@localhost:5432/uecebet'

db = SQLAlchemy(app)
