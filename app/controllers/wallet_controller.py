from app.models.models_db import *
from app.schemas.wallet_schemas import *
from flask_restx import Resource, Namespace
from app.controllers.helper import verificar_permissao_admin
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import request

carteira_ns = Namespace("Carteira")

@carteira_ns.route("/sacar/<int:id>")
class withdraw(Resource):
    @carteira_ns.expect(withdraw_status)
    def post(self, id):
        withdraw_data = carteira_ns.payload
        usuario = Usuarios.query.get(id)

        if usuario:
            valor_saque = withdraw_data['saldo']
            usuario.saldo -= valor_saque
            db.session.commit()
            return {'message': 'Saque bem-sucedido', 'novo_saldo': usuario.saldo}
        
        else:
            return {'message': 'Usuário não encontrado'}, 404

@carteira_ns.route("/depositar/<int:id>")
class deposit(Resource):
    @carteira_ns.expect(deposit_status)
    def post(self, id):
        deposit_data = carteira_ns.payload
        usuario = Usuarios.query.get(id)

        if usuario:
            valor_deposito = deposit_data['deposito']
            usuario.saldo += valor_deposito
            db.session.commit()
            return {'message': 'Depósito bem-sucedido', 'novo_saldo': usuario.saldo}
        
        else:
            return {'message': 'Usuário não encontrado'}, 404
        
@carteira_ns.route("/depositar/adm")
class deposit2(Resource):
    @carteira_ns.expect(deposit_status)
    @jwt_required()
    def post(self):
        verificar_permissao_admin()
        caixa = Caixa.query.filter_by(id=1).first()
        deposit_data = carteira_ns.payload
        valor_deposito = deposit_data['deposito']
        caixa.saldo_casa += valor_deposito
        db.session.commit()
        return {'message': 'Depósito bem-sucedido', 'novo_saldo': caixa.saldo_casa}

 
@carteira_ns.route("/sacar/adm")
class withdraw2(Resource):
    @carteira_ns.expect(withdraw_status)
    @jwt_required()   
    def post(self):
        verificar_permissao_admin()
        caixa = Caixa.query.filter_by(id=1).first()
        withdraw_data = carteira_ns.payload
        valor_saque = withdraw_data['saldo']
        caixa.saldo_casa -= valor_saque
        db.session.commit()
        return {'message': 'Saque bem-sucedido', 'novo_saldo': caixa.saldo_casa}

@carteira_ns.route("/ver_saldo/adm")
class saldo(Resource):
    def get(self):
        saldo = Caixa.query.filter_by(id=1).first()
        return{"saldo": saldo.saldo_casa}  

@carteira_ns.route("/ver_saldo_user/<int:id>")
class deposit(Resource):
    @carteira_ns.expect(deposit_status)
    def get(self, id):
        usuario = Usuarios.query.get(id)
        if usuario:
            return {'saldo': usuario.saldo}
        else:
            return {'message': 'Usuário não encontrado'}, 404