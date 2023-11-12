from flask import Flask
from flask_sqlalchemy import SQLAlchemy


user_db = "postgres"
password_db = "postgres"

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password_db}@localhost:5432/uecebet'
# app.app_context()
db = SQLAlchemy(app)

# class Usuario(db.Model):
#     id = db.Column(db.Integer, primary_key= True)
#     nome = db.Column(db.String(50))
#     email = db.Column(db.String(100))
#     teste = db.Column(db.String(100))

#     def to_json(self):
#         return {"id": self.id, "nome": self.nome, "email": self.email}
    
# class Usuario_apostador(db.Model):
#     id = db.Column(db.Integer, primary_key= True)
#     nome = db.Column(db.String(50))
#     email = db.Column(db.String(100))

#     def to_json(self):
#         return {"id": self.id, "nome": self.nome, "email": self.email}

# class Usuario_adm(db.Model):
#     id = db.Column(db.Integer, primary_key= True)
#     nome = db.Column(db.String(50))
#     email = db.Column(db.String(100))

#     def to_json(self):
#         return {"id": self.id, "nome": self.nome, "email": self.email}

# class teste(db.Model):
#     id = db.Column(db.Integer, primary_key= True)
#     nome = db.Column(db.String(50))
#     email = db.Column(db.String(100))
#     teste = db.Column(db.String(100))

