from app.models.models_db import *
from app.schemas.wallet_schemas import *
from flask_restx import Resource, Namespace
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request

carteira_ns = Namespace("Carteira")

@carteira_ns.route("/sacar/<int:id>")
class withdraw(Resource):
    @carteira_ns.marshal_list_with(withdraw_status)
    def get(self, id):
        usuario = Usuarios.query.filter_by(id=id).first()
        saldo_atual = usuario.saldo
        if not usuario:
            return {'success': False, 'message': 'Usuário não encontrado'}, 404
        
        if saldo_atual < 100:
            return {'success': False, 'message': 'Saldo insuficiente para o saque'}, 400
        
        db.session.commit()