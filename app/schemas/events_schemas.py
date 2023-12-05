from flask_restx import fields
from config.settings import api

create_event = api.model('Criar Evento', {
    'id_adm': fields.Integer(required=True, description='Id ADM'),
    'time_1': fields.String(required=True, description='Time 1'),
    'time_2': fields.String(required=True, description='Time 2'),
    'odd_time1': fields.Float(required=True, description='Odd 1'),
    'odd_time2': fields.Float(required=True, description='Odd 2'),
    'odd_empate': fields.Float(required=True, description='Odd Empate'),
    'data': fields.Date(required=True, description='Data'),
    'descricao': fields.String(required=True, description='Descricao'),
    'evento_status': fields.Boolean(required = True, description ='Evento acontecendo')
})

update_event = api.model('Atualizar evento', {
    "odd_time1": fields.Float(required=True, description='Odd 1'),
    "odd_time2": fields.Float(required=True, description='Odd 2'),
    "odd_empate": fields.Float(required=True, description='Odd Empate'),
    "descricao": fields.String(required=True, description='Descricao')
})

event_add = api.model('Registrar evento', {
    "id" : fields.Integer(required = True),
    "time1": fields.String(required=True, description='Time 1'),
    "time2": fields.String(required=True, description='Time 2'),
    "odd_time1": fields.Float(required=True, description='Odd 1'),
    "odd_time2": fields.Float(required=True, description='Odd 2'),
    "odd_empate": fields.Float(required=True, description='Odd Empate'),
    "data": fields.Date(required=True, description='Data'),
    "descricao": fields.String(required=True, description='Descricao')
})

list_event = api.model('Listar Evento', {
    "id" : fields.Integer(required = True),
    "time_1": fields.String(required=True, description='Time 1'),
    "time_2": fields.String(required=True, description='Time 2'),
    "odd_time1": fields.Float(required=True, description='Odd 1'),
    "odd_time2": fields.Float(required=True, description='Odd 2'),
    "odd_empate": fields.Float(required=True, description='Odd Empate'),
    "data": fields.Date(required=True, description='Data'),
    "descricao": fields.String(required=True, description='Descricao')
})
