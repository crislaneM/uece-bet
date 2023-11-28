from config.settings import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique = True)
    nome = db.Column(db.String(100), nullable=False)
    tipo_usuario = db.Column(db.Integer, nullable=False)
    cpf = db.Column(db.String(11), unique = True, nullable = False)
    nacionalidade = db.Column(db.String(50))
    nascimento = db.Column(db.Date)
    saldo = db.Column(db.Float)
    senha = db.Column(db.String(255), nullable = False)
    #relacao
    eventos = db.relationship('Eventos', back_populates='usuario', uselist=False)
    
    
class Eventos(db.Model):
    __tablename__ = 'eventos'
    id = db.Column(db.Integer, primary_key=True)
    time_1 = db.Column(db.String, nullable=False )
    time_2 = db.Column(db.String, nullable=False)
    odd_time1 = db.Column(db.Float, nullable=False)
    odd_time2 = db.Column(db.Float, nullable=False)
    odd_empate = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    descricao = db.Column(db.Text)
    id_adm = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    #relacao
    usuario = db.relationship('Usuarios', back_populates='eventos')
    # times = db.relationship('Times', back_populates='eventos')

class Aposta(db.Model):
    __tablename__ = 'aposta'
    id = db.Column(db.Integer, primary_key = True)
    valor_apostado = db.Column(db.Float, nullable = False)
    resultado_apostado = db.Column(db.String, nullable = False)
    odd_apostada = db.Column(db.Float, nullable = False)
    id_apostador = db.Column(db.Integer, nullable = False)


# class Times(db.Model):
#     __tablename__ = 'times'
#     nome = db.Column(db.String(30), primary_key = True)
#     modalidade = db.Column(db.String(20))
#     #relacao
#     eventos = db.relationship('Eventos', back_populates = 'times')
    