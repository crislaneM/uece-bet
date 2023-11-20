from flask import Response,jsonify, request
from flask_restx import Resource, Namespace, fields
from werkzeug.security import generate_password_hash
from app.models.user import *
from app.schemas.user_schemas import user_register_model, user_model, adm_model, update_pwd_user

import json

user_ns = Namespace("Usuários")

@user_ns.route("/registro")
class userRegister(Resource):

    @user_ns.doc(responses={201: 'Recurso criado com sucesso', 400: 'Erro nos dados de entrada'})
    @user_ns.expect(user_register_model, validate=True)
    def post(self):
        try:
            user_data = user_ns.payload

            if Usuario_apostador.query.filter_by(email=user_data['email']).first():
                return {"status": "error", "mensagem": "Email já cadastrado. Escolha outro email."}, 400

            if Usuario_apostador.query.filter_by(cpf=user_data['cpf']).first():
                return {"status": "error", "mensagem": "Cpf já cadastrado. Escolha outro cpf."}, 400

            novo_apostador = Usuario_apostador(
                nome=user_data['nome'],
                nascimento=user_data['nascimento'],
                cpf=user_data['cpf'],
                nacionalidade=user_data['nacionalidade'],
                saldo_apostador=200,
                email=user_data['email'],
                senha=generate_password_hash(user_data['senha'], method='pbkdf2:sha256')
            )

            db.session.add(novo_apostador)
            db.session.commit()

            return {"status": "success", "mensagem": "Usuário criado com sucesso"}, 201

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao cadastrar usuário: {str(e)}"}, 500
      
@user_ns.route("/apostador/todosusuarios")
class allUserGumbler(Resource):

    @user_ns.marshal_list_with(user_model)
    def get(self):
        return Usuario_apostador.query.all()

@user_ns.route("/adm/todosusuarios")
class allUserAdm(Resource):

    @user_ns.marshal_list_with(adm_model)
    def get(self):
        return Usuario_adm.query.all()

@user_ns.route("/<int:id>")
class userOperations(Resource):

    @user_ns.marshal_with(user_model)
    def delete(self,id):
        usuario_objeto = Usuario_apostador.query.filter_by(id=id).first()
        
        try:
            db.session.delete(usuario_objeto)
            db.session.commit()
            return usuario_objeto, 201

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao cadastrar usuário: {str(e)}"}, 500
        
    
    @user_ns.expect(update_pwd_user)
    @user_ns.marshal_with(user_model)
    def put(self, id):
        body = user_ns.payload
        usuario_obj = Usuario_apostador.query.filter_by(id=id).first()

        try:
            if('senha' in body):
                usuario_obj.senha = generate_password_hash(body['senha'], method='pbkdf2:sha256')

            db.session.commit()
            
            return usuario_obj, 201

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao cadastrar usuário: {str(e)}"}, 500
        
    

        

