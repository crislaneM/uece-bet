from flask import jsonify
from flask_migrate import Migrate

from app import app, db
from app.models import User

Migrate(app, db)

@app.make_shell_context
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User
    )

