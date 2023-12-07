from app.models.models_db import *
from app.schemas.bets_schemas import *
from flask_restx import Resource, Namespace
from flask_jwt_extended import get_jwt_identity, jwt_required

carteira_ns = Namespace("Carteira")
