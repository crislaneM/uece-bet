from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort
from app.models.models_db import *
from app.schemas.events_schemas import *

# def verificar_permissao_admin(error):
#     user_id = get_jwt_identity()
#     user = Usuarios.query.get(user_id)
#     if user.tipo_usuario == 0:
#         abort(403, {"ERRO": f'{error}'})

# user_nao_adm = "Permissão negada: O usuário não é administrador"

events_ns = Namespace("Eventos")

@events_ns.route("/cadastrar")

class admEvent(Resource):
    @events_ns.doc(responses={201: 'Recurso criado com sucesso', 400: 'Erro nos dados de entrada'})
    @events_ns.expect(create_event, validate=True)
    # @jwt_required()
    def post(self):
        # verificar_permissao_admin(user_nao_adm)
        try:
            user_data = events_ns.payload
            user_admin = Usuarios.query.filter_by(id=user_data['id_adm']).first()

            if user_admin.tipo_usuario == 1:
                novo_evento = Eventos(
                    id_adm=user_data['id_adm'],
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
            
            return {"ERRO": "Permissão negada: O usuário não é administrador"},403

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao cadastrar evento: {str(e)}"}, 500
        
@events_ns.route("/atualizar/<int:evento_id>")
class eventOperation(Resource):
    @events_ns.expect(update_event)
    # @jwt_required()
    def put(self, evento_id):
        #verificar_permissao_admin(user_nao_adm)
        try:
            body = events_ns.payload
            user_admin = Eventos.query.filter_by(id=evento_id).first()

            # duvida: como saber quem é o usuario? garantir que ele ta alterando os arquivos ele mesmo criou?

            if user_admin.tipo_admin is not None: #imaginando que pra cadastrar ele já seja um administrador

                event_obj = Eventos.query.filter_by(id=evento_id).first()

                if ('odd_time1' in body): event_obj.odd_time1 = body['odd_time1']
                if ('odd_time2' in body): event_obj.odd_time2 = body['odd_time2']
                if ('odd_empate' in body): event_obj.odd_empate = body['odd_empate']
                if ('descricao' in body): event_obj.descricao = body['descricao']

                db.session.commit()
                
                response_data = {
                    "msg": "Evento atualizado com sucesso.",
                    "atualizações": events_ns.marshal(event_obj, update_event)
                }

                return response_data, 201
            
            return {"ERRO": "Permissão negada: O usuário não é administrador"},403
    
        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao atualizar evento: {str(e)}"}, 500
      
#seleciona um evento só      
@events_ns.route("/<int:evento_id>")
class listEvents(Resource):
    @events_ns.marshal_list_with(list_event)
    def get(self, evento_id):
        return Eventos.query.filter_by(id=id).first()

#mostra todos os eventos
@events_ns.route("/todoseventos")
class listAllEvents(Resource):
    @events_ns.marshal_list_with(list_event)
    def get(self):
        return Eventos.query.all()
