from flask_restx import fields
from config.settings import api

user_register_model = api.model('Registro de usuário', {
    'nome': fields.String(required=True, description='Nome de usuário'),
    'nascimento': fields.String(required=True, description='Nascimento do usuário'),
    'cpf': fields.String(required=True, description='Cpf do usuário'),
    'nacionalidade': fields.String(required=True, description='Nacionalidade do usuário'),
    'email': fields.String(required=True, description='Endereço de e-mail'),
    'senha': fields.String(required=True, description='Senha'),   
    'tipo_usuario':fields.Integer(required=True, description='Tipo do usuário')
})

user_model = api.model('Usuários apostadores',{
    'id':fields.Integer,
    'nome':fields.String,
    'saldo_apostador':fields.Float
})

adm_model = api.model('Usuários administradores',{
    'id':fields.Integer,
    'nome':fields.String,
    'saldo_adm':fields.Float
})

update_pwd_user= api.model('Atualizar senha apostador',{
    'senha': fields.String(required=True),
})

login_users= api.model('Login de todos usuários',{
    'email': fields.String(required=True),
    'senha': fields.String(required=True)
})
