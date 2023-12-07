from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort
from app.models.models_db import *
from app.schemas.events_schemas import *

def verificar_permissao_admin(error):
    user_id = get_jwt_identity()
    user = Usuarios.query.get(user_id)
    if user.tipo_usuario == 0:
        abort(403, {"ERRO": f'{error}'})

#msg de erro para user nao adm
user_nao_adm = "Permissão negada: O usuário não é administrador"

events_ns = Namespace("Eventos")

@events_ns.route("/cadastrar")

class admEvent(Resource):
    @events_ns.doc(responses={201: 'Recurso criado com sucesso', 400: 'Erro nos dados de entrada'})
    @events_ns.expect(create_event, validate=True)
    @jwt_required()
    def post(self):
        verificar_permissao_admin(user_nao_adm)
        user_id = get_jwt_identity()
        try:
            user_data = events_ns.payload
            novo_evento = Eventos(
                id_adm = user_id,
                time_1=user_data['time_1'],
                time_2=user_data['time_2'],
                odd_time1=user_data['odd_time1'],
                odd_time2=user_data['odd_time2'],
                odd_empate=user_data['odd_empate'],
                data=user_data['data'],
                descricao=user_data['descricao'],
                evento_status = True )

            db.session.add(novo_evento)
            db.session.commit()

            return {"status": "success", "mensagem": "Evento criado com sucesso"}, 201
        

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao cadastrar evento: {str(e)}"}, 500
        
@events_ns.route("/atualizar/<int:evento_id>")
class eventOperation(Resource):
    @events_ns.expect(update_event)
    @jwt_required()
    def put(self, evento_id):
        verificar_permissao_admin(user_nao_adm)
        try:
            body = events_ns.payload
            user_admin = Eventos.query.filter_by(id=evento_id).first()
            if user_admin.tipo_admin is not None: 
                event_obj = Eventos.query.filter_by(id=evento_id).first()

                if ('odd_time1' in body): event_obj.odd_time1 = body['odd_time1']
                db.session.commit()
                
                response_data = {
                    "msg": "Evento atualizado com sucesso.",
                    "atualizações": events_ns.marshal(event_obj, update_event)
                }

                return response_data, 201
            
            return {"ERRO": "Permissão negada: O usuário não é administrador"},403
    
        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao atualizar usuário: {str(e)}"}, 500
      
#seleciona um evento só      
@events_ns.route("/<int:evento_id>")
class listEvents(Resource):
    @events_ns.marshal_list_with(list_event)
    def get(self, evento_id):
        return Eventos.query.filter_by(id=evento_id).first()

#mostra todos os eventos
@events_ns.route("/todos_eventos")
class listAllEvents(Resource):
    @events_ns.marshal_list_with(list_event)
    def get(self):
        return Eventos.query.all()

#FAZENDO
@events_ns.route("/encerrar/<int:evento_id>")
class eventShutDown(Resource):
    @events_ns.expect(shutdown)
    @jwt_required()
    def put(self, evento_id):
        verificar_permissao_admin(user_nao_adm)
        try:
            event_obj = Eventos.query.filter_by(id=evento_id).first()
            event_obj.evento_status = False
            db.session.commit()
            response_data = {
                "msg": "Evento encerrado com sucesso."
            }
            return response_data, 201
        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao atualizar usuário: {str(e)}"}, 500
