from config.settings import app, db, api, jwt
from app.controllers.user_controller import user_ns
from app.controllers.events_controller import events_ns

class DatabaseManager:
    def __init__(self):
        self.app = app
        self.db = db
        self.jwt = jwt
        self.api = api
        self.api.add_namespace(user_ns, path='/usuario')
        self.api.add_namespace(events_ns, path='/evento')
        
    def create_tables(self):
        try:
            with self.app.app_context():
                self.db.create_all()
            print("Tabelas criadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar tabelas: {str(e)}")

    def run(self):
        return self.app.run(debug=True)