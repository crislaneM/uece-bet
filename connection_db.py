from config.settings import app, db, api, jwt
from app.controllers.user_controller import user_ns
from app.controllers.events_controller import events_ns
from app.controllers.bet_controller import apostas_ns
from app.controllers.wallet_controller import carteira_ns
from app.models.models_db import Caixa

class DatabaseManager:
    def __init__(self):
        self.app = app
        self.db = db
        self.jwt = jwt
        self.api = api
        self.api.add_namespace(user_ns, path='/usuario')
        self.api.add_namespace(events_ns, path='/evento')
        self.api.add_namespace(apostas_ns, path='/apostas')
        self.api.add_namespace(carteira_ns, path='/carteira')
        
    def create_tables(self):
        try:
            with self.app.app_context():
                self.db.create_all()
                if not Caixa.query.first():
                    novo_item_caixa = Caixa(saldo_casa=0)
                    self.db.session.add(novo_item_caixa)
                    self.db.session.commit()
            print("Tabelas criadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar tabelas: {str(e)}")

    def run(self):
        return self.app.run(debug=True)