from app.models.models_db import *
from app.schemas.bets_schemas import *
from flask_restx import Resource, Namespace
from flask_jwt_extended import get_jwt_identity, jwt_required

apostas_ns = Namespace("Apostas")

#nao esta descontando do saldo ao apostar (vai ser assim mesmo?)
#user_id pegando pelo jwt identity
#os dados sobre o time selecionado serão passados assim?
#terá algum campo para mostrar os possíveis lucro nesse momento ou em outro endpoint?
@apostas_ns.route("/apostar/<int:evento_id>")
class userApostar(Resource):
    @apostas_ns.doc(responses={201: 'Aposta realizada com sucesso', 400: 'Erro nos dados de entrada'})
    @apostas_ns.expect(betting, validate=True)
    @jwt_required()
    def post(self, evento_id):
        try:
            body = apostas_ns.payload
            user_id = get_jwt_identity()
            evento = Eventos.query.filter_by(id=evento_id).first()
            usuario = Usuarios.query.filter_by(id=user_id).first()
            caixa = Caixa.query.filter_by(id = 1).first()
            
            if Aposta.query.filter_by(id_evento=evento_id, id_apostador=user_id).first():
                return {"ERRO": f"A aposta já existe{Aposta.query.filter_by(id_evento=evento_id, id_apostador=user_id).first()}"}, 400
            
            if body['valor_apostado'] > (usuario.saldo):
                return{"ERRO": "Saldo insuficiente"}, 400
           
            if body['resultado_apostado'] == evento.time_1:
                nova_aposta = Aposta(
                    id_evento = evento_id,
                    id_apostador=user_id,
                    resultado_apostado=evento.time_1,
                    odd_apostada = evento.odd_time1, 
                    valor_apostado=body['valor_apostado'])
                
                usuario.saldo-=body['valor_apostado']
                caixa.saldo_casa+=body['valor_apostado']
                db.session.add(nova_aposta)
                db.session.commit()
                return {"status": "success", "mensagem": "Usuário criado com sucesso"}
            
            if body['resultado_apostado'] == evento.time_2:
                nova_aposta = Aposta(
                    id_evento = evento_id,
                    id_apostador=user_id,
                    resultado_apostado=evento.time_2,
                    odd_apostada = evento.odd_time2, 
                    valor_apostado=body['valor_apostado'])

                usuario.saldo-=body['valor_apostado']
                caixa.saldo_casa+=body['valor_apostado']
                db.session.add(nova_aposta)
                db.session.commit()
                return {"status": "success", "mensagem": "Usuário criado com sucesso"}
            
            if body['resultado_apostado'] == 'empate':
                nova_aposta = Aposta(
                    id_evento = evento_id,
                    id_apostador=user_id,
                    resultado_apostado=body['resultado_apostado'],
                    odd_apostada = evento.odd_empate, 
                    valor_apostado=body['valor_apostado'])

                usuario.saldo-=body['valor_apostado']
                caixa.saldo_casa+=body['valor_apostado']
                db.session.add(nova_aposta)
                db.session.commit()    
                return {"status": "success", "mensagem": "Usuário criado com sucesso"}
            
        except Exception as e:
            return {"status": "error", "mensagem": f"Erro ao criar aposta: {str(e)}"}, 500

@apostas_ns.route("distruibuir/<int:evento_id>") 
class dinheirosAposta(Resource):
    pass
            

