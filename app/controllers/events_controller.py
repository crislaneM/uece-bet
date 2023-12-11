from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import abort
from app.models.models_db import *
from app.schemas.events_schemas import *
from app.controllers.helper import verificar_permissao_admin

events_ns = Namespace("Eventos")

@events_ns.route("/cadastrar")

class admEvent(Resource):
    @events_ns.doc(responses={201: 'Recurso criado com sucesso', 400: 'Erro nos dados de entrada'})
    @events_ns.expect(create_event, validate=True)
    @jwt_required()
    def post(self):
        verificar_permissao_admin()
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
        verificar_permissao_admin()
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
            return {"status": "error", "mensagem": f"Erro ao atualizar evento: {str(e)}"}, 500
      
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

#pode ter duas abordagens: enviar o nome do time logo ou se é time_1, empate ou time_2. Ou pegar o nome dos times da tabela evento (como está sendo feito)
@events_ns.route("/encerrar/<int:evento_id>")
class eventShutDown(Resource):
    @events_ns.expect(shutdown)
    @jwt_required()
    def put(self, evento_id):
        verificar_permissao_admin()
        try:
            body = events_ns.payload
            event_obj = Eventos.query.filter_by(id=evento_id).first()
            caixa = Caixa.query.filter_by(id=1).first()
            # if(event_obj.evento_status == False):
            #     return {"ERRO": "evento já foi encerrado"}, 403
            event_obj.evento_status = False
            #if('resultado_evento' in body): event_obj.resultado_evento = body['resultado_evento']   
            if body['resultado_evento'] == 'time_1': 
                event_obj.resultado_evento = event_obj.time_1
            elif body['resultado_evento'] == 'time_2':
                event_obj.resultado_evento = event_obj.time_2
            else:
                event_obj.resultado_evento = 'empate'
            db.session.commit()
            # apos finalizar o evento
            # input o time que ganhou e distribui para os usuarios que apostaram naquele time
            # quais usuarios apostaram nesse evento? e no time que ganhou

            apost_obj = Aposta.query.filter_by(id_evento=evento_id, resultado_apostado = event_obj.resultado_evento).all()
            if apost_obj:
                for aposta in apost_obj:
                    print(aposta)
                    usuario = Usuarios.query.filter_by(id = aposta.id_apostador).first()
                    ganhos = (((aposta.odd_apostada-1) * aposta.valor_apostado) + aposta.valor_apostado)
                    usuario.saldo+=ganhos
                    caixa.saldo_casa -= ganhos

            db.session.commit()
            response_data = {
                "msg": "Evento encerrado com sucesso."
            }
            return response_data, 201
        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao encerrar evento: {str(e)}"}, 500
