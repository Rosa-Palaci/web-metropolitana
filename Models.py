from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    idAdmin = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Estudiante(db.Model):
    idEstudiante = db.Column(db.Integer, primary_key=True)
    Grupo = db.Column(db.String(255), nullable=False)
    NumLista = db.Column(db.Integer, nullable=False)
    Genero = db.Column(db.String(10), nullable=False)
    CicloEscolar = db.Column(db.String(255), nullable=False)
    Nivel1 = db.Column(db.Integer, nullable=False)
    Nivel2 = db.Column(db.Integer, nullable=False)
    Nivel3 = db.Column(db.Integer, nullable=False)
    PuntajeTotal = db.Column(db.Integer, nullable=False)
    Promedio = db.Column(db.Float, nullable=False)
    TiempoJugado = db.Column(db.Integer, nullable=False)
