from flask import Response
from config.settings import app
from models.user import Usuario
import json

# from flask import Blueprint

# user_blueprint = Blueprint('usuarios', __name__)


@app.route("/usuarios", methods=["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    print(usuarios_json)
    return gera_response(200, "Usuarios", usuarios_json, "ok")


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")
