from flask_restx import fields
from config.settings import api

withdraw_status = api.model("Sacar", {
    "saldo": fields.Float(required = True)
    })

deposit_status = api.model("Depositar", {
    "deposito": fields.Float(required = True)
    })
deposit_adm = api.model("Depositar2", {
    "deposito2": fields.Float(required = True)
    })