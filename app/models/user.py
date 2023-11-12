from config.settings import db

'''
class Usuario(db.Model):
    tablename = 'usuarios'
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100), unique = True)
    cpf = db.Column(db.String(11), unique = True)
    nacionalidade = db.Column(db.String(15))
    nascimento = db.Column(db.DateTime)
    tipo_user = db.Column(db.Boolean, default = True) # se True == usuario apostador
   
    apostadores = db.relationship("Usuario_apostador", back_populates = "usuarios")
    apostadores2 = db.relationship("Usuario_adm", back_populates = "usuarios2")

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "cpf" : self.cpf, "nacionalidade" : self.nacionalidade, "nascimento": self.nascimento, "tipo_user": self.tipo_user}
'''
class Usuario_apostador(db.Model):
    __tablename__ = 'apostadores'
    id = db.Column(db.Integer, primary_key= True, )
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100), unique = True)
    cpf = db.Column(db.String(11), unique = True)
    nacionalidade = db.Column(db.String(15))
    nascimento = db.Column(db.DateTime)
    senha = db.Column(db.String(255))
    saldo_apostador = db.Column(db.Float)

    def to_json(self):
        return {"id": self.id, 
                "nome": self.nome, 
                "email": self.email, 
                "cpf" : self.cpf,
                "nacionalidade" : self.nacionalidade,
                "nascimento": self.nascimento, 
                "senha": self.senha,
                "saldo_apostador": self.saldo_apostador}

class Usuario_adm(db.Model):
    __tablename__ = 'administrador'
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100), unique = True)
    cpf = db.Column(db.String(11), unique = True)
    nacionalidade = db.Column(db.String(15))
    nascimento = db.Column(db.DateTime)
    senha = db.Column(db.String(255))
    saldo_adm = db.Column(db.Float)

    def to_json(self):
        return {"id": self.id, 
                "nome": self.nome, 
                "email": self.email, 
                "cpf" : self.cpf,
                "nacionalidade" : self.nacionalidade,
                "nascimento": self.nascimento, 
                "senha": self.senha,
                "saldo_adm": self.saldo_adm}
        