from flask import Flask, render_template, request, flash, url_for, redirect
from Models import db, Admin, Estudiante
from flask_mysqldb import MySQL
import os
import plotly.express as px
import pandas as pd

app = Flask(__name__)


# Configuración de MySQL
app.config['MYSQL_HOST'] = 'escuelametropolitana.c9ygi46o271u.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'escuelametropolitana'

mysql = MySQL(app)

# Establecer la clave secreta
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')




# rutas
@app.route('/')
def home():
    titulo = "Escuela Metropolitana"
    return render_template('index.html', titulo=titulo)

# ruta para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        if not usuario or not password:
            flash('Todos los campos son requeridos', 'error')
            return redirect(url_for('login'))

        # Realizar la consulta a la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM administradores WHERE usuario = %s AND password = %s', (usuario, password))
        admin = cursor.fetchone()
        cursor.close()

        if admin:
            flash('Inicio exitoso', 'success')
            return redirect(url_for('profesor'))
        else:
            flash('Correo electrónico o contraseña incorrectos', 'error')
            return redirect(url_for('login'))
    else:
        titulo = "Inicio de sesión"
        return render_template('login.html', titulo=titulo)




# instrucciones
@app.route('/instrucciones')
def instrucciones():
    titulo = "Instrucciones"
    return render_template('instrucciones.html', titulo=titulo)

# profesor
@app.route('/profesor')
def profesor():
    titulo = "Profesor"

    return render_template('profesor.html', titulo=titulo)

#Dashboard

# mejores
@app.route('/mejores')
def mejores():
    estudiantes = Estudiante.query.order_by(Estudiante.Puntaje.desc()).limit(10).all()
    df = pd.DataFrame([{
        'Nombre': f"Estudiante {e.idEstudiante}",
        'Puntaje': int(e.Puntaje)
    } for e in estudiantes])
    fig = px.bar(df, x='Nombre', y='Puntaje', title="Top 10 Mejores Puntajes")
    graphJSON = fig.to_json()
    return render_template('dashboards/mejores.html', graphJSON=graphJSON)

# peores
@app.route('/peores')
def peores():
    return render_template('dashboards/peores.html')

# promedios
@app.route('/promedios')
def promedios():
    return render_template('dashboards/promedios.html')

# alumnos
@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    if request.method == 'POST':
        input_data = request.form.get('numLista').strip()
        if len(input_data) > 1:
            num_lista = input_data[:-1]  # Todo excepto el último carácter
            grupo = input_data[-1]  # El último carácter
            estudiante = Estudiante.query.filter_by(NumLista=num_lista, Grupo=grupo).first()
            if estudiante:
                return render_template('dashboards/alumnos.html', estudiante=estudiante)
            else:
                return render_template('dashboards/alumnos.html', message="No se encontró el estudiante.")
        else:
            return render_template('dashboards/alumnos.html', message="Formato de entrada inválido.")
    return render_template('dashboards/alumnos.html')
# grupos
@app.route('/grupos')
def grupos():
    return render_template('dashboards/grupos.html')

# genero
@app.route('/genero')
def genero():
    return render_template('dashboards/genero.html')

# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)