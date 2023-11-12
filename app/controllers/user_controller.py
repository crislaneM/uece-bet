from flask import Blueprint, Response, jsonify, request
from werkzeug.security import generate_password_hash
from config.settings import app
from app.models.user import *
import json

user_blueprint = Blueprint('usuario', __name__)

@user_blueprint.route("/cadastrar", methods=["POST"])
def cria_usuario():
    try:
        body = request.get_json()

        if Usuario_apostador.query.filter_by(email=body['email']).first():
            return {
                "status": "error",
                "mensagem": "Email já cadastrado. Escolha outro email."
            }, 400

        if Usuario_apostador.query.filter_by(cpf=body['cpf']).first():
            return {
                "status": "error",
                "mensagem": "Cpf já cadastrado. Escolha outro cpf."
            }, 400

        senha_hash = generate_password_hash(body['senha'], method='pbkdf2:sha256')

        novo_apostador = Usuario_apostador(
            nome=body['nome'],
            nascimento=body['nascimento'],
            cpf=body['cpf'],
            nacionalidade=body["nacionalidade"],
            saldo_apostador=200,
            email=body['email'],
            senha=senha_hash
        )

        db.session.add(novo_apostador)
        db.session.commit()

        return {
            "status": "success",
            "mensagem": "Usuário criado com sucesso",
        }, 201

    except KeyError as e:
        return {
            "status": "error",
            "mensagem": f"Campo obrigatório ausente: {str(e)}"
        }, 400

    except Exception as e:
        return {
            "status": "error",
            "mensagem": f"Erro ao cadastrar usuário: {str(e)}"
        }, 500

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


