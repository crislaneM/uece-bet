from flask import Blueprint, Response, request
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


@user_blueprint.route("/apostadores/<int:id>", methods=["DELETE"])
def deleta_usuario(id):
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