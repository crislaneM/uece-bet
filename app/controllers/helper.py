from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.models_db import *
from flask import abort

def verificar_permissao_admin():
    user_id = get_jwt_identity()
    user = Usuarios.query.get(user_id)
    if user.tipo_usuario == 0:
        abort(403, {"ERRO": f"Permissão negada: O usuário não é administrador"})

