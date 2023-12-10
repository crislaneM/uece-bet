from flask_restx import fields
from config.settings import api

withdraw_status = api.model("Sacar", {
    "saldo": fields.Float(required = True)
    })

deposit_status = api.model("Depositar", {
    "deposito": fields.Float(required = True)
    })