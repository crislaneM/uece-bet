from flask import Blueprint, Response
from config.settings import app
from app.models.user import *
import json

user_blueprint = Blueprint('usuario', __name__)

#mudado para usuario_adm (nao existe mais apenas usuario)
@user_blueprint.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario_adm.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    print(usuarios_json)
    return gera_response(200, "Usuarios", usuarios_json, "ok")


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


