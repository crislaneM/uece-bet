from config.settings import app, db
from app.models.user import *


# from app.controllers.user_controller import user_blueprint

# app.register_blueprint(user_blueprint)



try:
    with app.app_context():
        db.create_all()
    print("Tabelas criadas com sucesso.")
except Exception as e:
    print(f"Erro ao criar tabelas: {str(e)}")
