from flask_restx import Resource, Namespace

from app.models.models_db import *
from app.schemas.events_schemas import *

events_ns = Namespace("Eventos")

@events_ns.route("/cadastrar")
class admEvent(Resource):

    @events_ns.doc(responses={201: 'Recurso criado com sucesso', 400: 'Erro nos dados de entrada'})
    @events_ns.expect(create_event, validate=True)
    def post(self):
        try:
            user_data = events_ns.payload
            novo_evento = Eventos(
                id_adm=user_data['id_adm'],
                time_1=user_data['time_1'],
                time_2=user_data['time_2'],
                odd_time1=user_data['odd_time1'],
                odd_time2=user_data['odd_time2'],
                odd_empate=user_data['odd_empate'],
                data=user_data['data'],
                descricao=user_data['descricao'])

            db.session.add(novo_evento)
            db.session.commit()

            return {"status": "success", "mensagem": "Usuário criado com sucesso"}, 201

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao cadastrar usuário: {str(e)}"}, 500
        
@events_ns.route("/atualizar/<int:id>")
class eventOperation(Resource):
    @events_ns.expect(update_event)
    @events_ns.marshal_with(update_event)
    def put(self, id):
        body = events_ns.payload
        event_obj = Eventos.query.filter_by(id=id).first()

        try:
            if ('odd_time1' in body): event_obj.odd_time1 = body['odd_time1']
            if ('odd_time2' in body): event_obj.odd_time2 = body['odd_time2']
            if ('odd_empate' in body): event_obj.odd_empate = body['odd_empate']
            if ('descricao' in body): event_obj.descricao = body['descricao']

            db.session.commit()
            
            return event_obj, 201

        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao atualizar usuário: {str(e)}"}, 500
        
@events_ns.route("/<int:id>")
class listEvents(Resource):
    @events_ns.marshal_list_with(list_event)
    def get(self, id):
        return Eventos.query.filter_by(id=id).first()

@events_ns.route("/todoseventos")
class listAllEvents(Resource):
    @events_ns.marshal_list_with(list_event)
    def get(self):
        return Eventos.query.all()