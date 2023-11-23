from flask import jsonify
from flask_restx import Resource, Namespace
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.user import *
from app.schemas.user_schemas import user_register_model, user_model, update_pwd_user, login_users
# from app.authorization import jwt_required


user_ns = Namespace("Usuários")

@user_ns.route("/registro")
class userRegister(Resource):

    @user_ns.doc(responses={201: 'Recurso criado com sucesso', 400: 'Erro nos dados de entrada'})
    @user_ns.expect(user_register_model, validate=True)
    def post(self):
        try:
            user_data = user_ns.payload

            if Usuarios.query.filter_by(email=user_data['email']).first():
                return {"status": "error", "mensagem": "Email já cadastrado. Escolha outro email."}, 400

            if Usuarios.query.filter_by(cpf=user_data['cpf']).first():
                return {"status": "error", "mensagem": "Cpf já cadastrado. Escolha outro cpf."}, 400

            novo_apostador = Usuarios(
                nome=user_data['nome'],
                nascimento=user_data['nascimento'],
                cpf=user_data['cpf'],
                nacionalidade=user_data['nacionalidade'],
                saldo=20,
                email=user_data['email'],
                senha=generate_password_hash(user_data['senha'], method='pbkdf2:sha256'),
                tipo_usuario=user_data['tipo_usuario']
            )

            db.session.add(novo_apostador)
            db.session.commit()

            return {"status": "success", "mensagem": "Usuário criado com sucesso"}, 201

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao cadastrar usuário: {str(e)}"}, 500
      
@user_ns.route("/apostador/todosusuarios")
class allUserGumbler(Resource):

    @user_ns.marshal_list_with(user_model)
    def get(self):
        return Usuarios.query.filter_by(tipo_usuario=0).first()

@user_ns.route("/adm/todosusuarios")
class allUserAdm(Resource):

    @user_ns.marshal_list_with(user_model)
    def get(self):
        return Usuarios.query.filter_by(tipo_usuario=1).first()

@user_ns.route("/<int:id>")
class userOperations(Resource):

    @user_ns.marshal_with(user_model)
    def delete(self,id):
        usuario_objeto = Usuarios.query.filter_by(id=id).first()
        
        try:
            db.session.delete(usuario_objeto)
            db.session.commit()
            return usuario_objeto, 201

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao deletar usuário: {str(e)}"}, 500
        
    @user_ns.expect(update_pwd_user)
    @user_ns.marshal_with(user_model)
    def put(self, id):
        body = user_ns.payload
        usuario_obj = Usuarios.query.filter_by(id=id).first()

        try:
            if('senha' in body):
                usuario_obj.senha = generate_password_hash(body['senha'], method='pbkdf2:sha256')

            db.session.commit()
            
            return usuario_obj, 201

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao atualizar usuário: {str(e)}"}, 500
        
@user_ns.route('/login')
class createLogin(Resource):
    
    @user_ns.expect(login_users, validate=True)
    def post(self):

        body_login = user_ns.payload

        user = Usuarios.query.filter_by(email=body_login['email']).first()
        
        if user != None:
        
            check_password = check_password_hash(user.senha, body_login['senha'])
                
            if user.email and check_password:
                access_token = create_access_token(identity=user.id)
                refresh_token = create_refresh_token(identity=user.id)

                return  {   
                            "message" : "Logged In",
                            "tokens":{
                                "access": access_token,
                                "refresh": refresh_token
                        }    
                    },200    
        
        return {"error": "Email e senha inválidos"}

@user_ns.route('/protected')
class createProtected(Resource):

    @user_ns.marshal_with(user_model)
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()

        return Usuarios.query.filter_by(id=current_user).first()
        

