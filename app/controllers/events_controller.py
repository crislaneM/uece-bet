from flask_restx import Resource, Namespace

from app.models.user import *
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
                time_2=user_data['time_1'],
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