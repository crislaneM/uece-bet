from flask_restx import fields
from config.settings import api

betting = api.model('Apostar', {
    'id_apostador': fields.Integer(required=True, description='Id apostador'),
    'resultado_apostado': fields.String(required=True, description='Time escolhido'),
    'valor_apostado': fields.Float(required=True, description='Valor apostado'),
    'id_evento': fields.Integer(required = True, description = 'Evento apostado')
})

caixa = api.model('Caixa', {
    'saldo_casa': fields.Float(required=True, description='Saldo total da casa'),
})

