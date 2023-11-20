from config.settings import app, db, api
from app.controllers.user_controller import user_ns

class DatabaseManager:
    def __init__(self):
        self.app = app
        self.db = db
        self.api = api
        self.api.add_namespace(user_ns, path='/usuario')
        
    def create_tables(self):
        try:
            with self.app.app_context():
                self.db.create_all()
            print("Tabelas criadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar tabelas: {str(e)}")

    def run(self):
        return self.app.run(debug=True)