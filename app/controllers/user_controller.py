from flask import Blueprint, Response, make_response, request
from config.settings import app
from app.models.user import *
import json

user_blueprint = Blueprint('usuario', __name__)

#mudado para usuario_adm (nao existe mais apenas usuario)
@user_blueprint.route("/apostadores", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario_apostador.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    print(usuarios_json)
    return gera_response(200, "Usuarios", usuarios_json, "ok")


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")

@user_blueprint.route("/apostadores/<int:id>", methods = ["PUT"])
def atualizar_usuario(id):
    body = request.get_json()
    usuario_obj = Usuario_apostador.query.filter_by(id=id).first()
    try:
        if('senha' in body):
            usuario_obj.senha = body['senha']
        db.session.commit()
        return gera_response(200, "usuario", usuario_obj.to_json() ,"senha atualizada" )
    except Exception as error:
        return gera_response(200, "usuario", usuario_obj.to_json(), f"erro ao mudar senha: {error}")
    

        

