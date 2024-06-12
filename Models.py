from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    idAdmin = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
class Estudiante(db.Model):
    idEstudiante = db.Column(db.Integer, primary_key=True)
    Grupo = db.Column(db.String(255))
    NumLista = db.Column(db.Integer)
    Genero = db.Column(db.Boolean)
    CicloEscolar = db.Column(db.String(255))
    Puntaje = db.Column(db.String(255))
    Promedio = db.Column(db.String(255))
    TiempoJugado = db.Column(db.Integer)