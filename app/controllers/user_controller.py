from flask import Response, jsonify, request
from flask_restx import Resource, Namespace, fields
from werkzeug.security import generate_password_hash
from app.models.user import *

import json

user_ns = Namespace("usuario")

user_model = user_ns.model('User', {
    'nome': fields.String(required=True, description='Nome de usuário'),
    'data_nascimento': fields.String(required=True, description='Data de nascimento do usuário'),
    'cpf': fields.String(required=True, description='Cpf do usuário'),
    'nacionalidade': fields.String(required=True, description='Nacionalidade do usuário'),
    'saldo_apostado': fields.String(required=True, description='Saldo inicial do usuário'),
    'email': fields.String(required=True, description='Endereço de e-mail'),
    'senha': fields.String(required=True, description='Senha'),   
})

@user_ns.route("/cadastrar")
class userRegister(Resource):

    @user_ns.doc(responses={201: 'Recurso criado com sucesso', 400: 'Erro nos dados de entrada'})
    @user_ns.expect(user_model, validate=True)
    def post(self):
        try:
            user_data = user_ns.payload

            if Usuario_apostador.query.filter_by(email=user_data['Email']).first():
                return {"status": "error", "mensagem": "Email já cadastrado. Escolha outro email."}, 400

            if Usuario_apostador.query.filter_by(cpf=user_data['Cpf']).first():
                return {"status": "error", "mensagem": "Cpf já cadastrado. Escolha outro cpf."}, 400

            novo_apostador = Usuario_apostador(
                nome=user_data['nome'],
                nascimento=user_data['nata_nascimento'],
                cpf=user_data['cpf'],
                nacionalidade=user_data['nacionalidade'],
                saldo_apostador=user_data['saldo_apostado'],
                email=user_data['email'],
                senha=generate_password_hash(user_data['senha'], method='pbkdf2:sha256')
            )

            db.session.add(novo_apostador)
            db.session.commit()

            return {"status": "success", "mensagem": "Usuário criado com sucesso"}, 201

        except ValidationError as e:
            return {"status": "error", "mensagem": f"Erro nos dados de entrada: {str(e.messages)}"}, 400

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao cadastrar usuário: {str(e)}"}, 500
        
@user_ns.route("/usuarios")
class seleciona_usuarios(Resource):
    def get(self):
        usuarios_objetos = Usuario_adm.query.all()
        usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
        print(usuarios_json)
        return gera_response(200, "Usuarios", usuarios_json, "ok")

@user_ns.route("/apostadores/<int:id>")
class deleta_usuario(id):
    def delete(self):
        usuario_objeto = Usuario_apostador.query.filter_by(id=id).first()
        try:
            db.session.delete(usuario_objeto)
            db.session.commit()
            return gera_response(200, "usuario", usuario_objeto.to_json(), "Deletado com sucesso")
        except Exception as e:
            print('Erro', e)
            return gera_response(400, "usuario", {}, "Erro ao deletar")
    
# @user_blueprint.route("/apostadores/<int:id>", methods=["PUT"])
# def atualiza_usuario(id):
#     usuario_objeto = Usuario_apostador.query.filter_by(id=id).first()
#     body = request.get_json()

#     try:
#         if('senha' in body):
#             usuario_objeto.senha = body['senha']
        
#         db.session.add(usuario_objeto)
#         db.session.commit()
#         return gera_response(200, "usuario", usuario_objeto.to_json(), "Atualizado com sucesso")
#     except Exception as e:
#         print('Erro', e)
#         return gera_response(400, "usuario", {}, "Erro ao atualizar")


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")