from config.settings import app, db
from app.controllers.user_controller import user_blueprint

class DatabaseManager:
    def __init__(self):
        self.app = app
        self.db = db

    def create_tables(self):
        self.app.register_blueprint(user_blueprint)
        try:
            with self.app.app_context():
                self.db.create_all()
            print("Tabelas criadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar tabelas: {str(e)}")

    def run(self):
        return self.app.run()