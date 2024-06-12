from flask import Flask, render_template 
from Models import db, Admin

app = Flask(__name__, static_url_path="/static")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/palac/Documents/prueba-web/escuela.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'tu_clave_secreta_aqui'
db.init_app(app)

# rutas
@app.route('/')
def home():
    titulo = "Escuela Metropolitana"
    return render_template('index.html', titulo=titulo)

# ruta para nosotros
@app.route('/login')
def login():
    titulo = "login"
    return render_template('login.html')

# instrucciones
@app.route('/instrucciones')
def instrucciones():
    titulo = "Instrucciones"
    return render_template('instrucciones.html', titulo=titulo)


# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)