from flask_restx import fields
from config.settings import api

withdraw_status = api.model("Sacar", {
    "saldo": fields.Float(required = True)
    })