from config.settings import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique = True)
    nome = db.Column(db.String(50), nullable=False)
    tipo_usuario = db.Column(db.Boolean, nullable=False)
    cpf = db.Column(db.String(11), unique = True, nullable = False)
    nacionalidade = db.Column(db.String(50))
    nascimento = db.Column(db.Date)
    saldo = db.Column(db.Float)
    senha = db.Column(db.String(50), nullable = False)
    #relacao
    eventos = db.relationship('Eventos', back_populates='usuario', uselist=False)
    
   
class Eventos(db.Model):
    __tablename__ = 'eventos'
    id = db.Column(db.Integer, primary_key=True)
    time_1 = db.Column(db.String, db.ForeignKey('times.nome'))
    time_2 = db.Column(db.String, db.ForeignKey('times.nome'))
    odd_time1 = db.Column(db.Float, nullable=False)
    odd_time2 = db.Column(db.Float, nullable=False)
    odd_empate = db.Column(db.Float, nullable=False)
    id_adm = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    #relacao
    usuario = db.relationship('Usuarios', back_populates='eventos')
    times = db.relationship('Times', back_populates='eventos')

class Times(db.Model):
    __tablename__ = 'times'
    nome = db.Column(db.String(30), primary_key = True)
    modalidade = db.Column(db.String(20))
    #relacao
    eventos = db.relationship('Eventos', back_populates = 'times')
    