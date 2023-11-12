from flask import Flask
from flask import Blueprint, Response, request
from config.settings import app, db
from app.models.user import Usuario
import json

user_blueprint = Blueprint('usuario', __name__)
#app = Flask(__name__)

@user_blueprint.route("/usuarios", methods=["GET"])
def lista_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    print(usuarios_json)
    return gera_response(200, "Usuarios", usuarios_json, "ok")


# @app.route("/usuarios", methods=["POST"])
# def cria_usuario():
#     body = request.get_json()

#     try:
#         usuario = Usuario(nome=body["nome"], email= body["email"])
#         db.session.add(usuario)
#         db.session.commit()
#         return gera_response(201, "usuario", usuario.to_json(), "Criado com sucesso")
#     except Exception as e:
#         print('Erro', e)
#         return gera_response(400, "usuario", {}, "Erro ao cadastrar")





def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")