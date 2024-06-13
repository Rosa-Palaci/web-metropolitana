from flask import Flask, render_template, request, flash, url_for, redirect
from flask_mysqldb import MySQL
import os
import plotly.express as px
import pandas as pd
from flasgger import Swagger, swag_from

app = Flask(_name_)
swagger = Swagger(app)

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
    """
    Página de inicio.
    ---
    responses:
      200:
        description: Página principal
    """
    titulo = "Escuela Metropolitana"
    return render_template('index.html', titulo=titulo)

# ruta para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Página de inicio de sesión.
    ---
    parameters:
      - name: usuario
        in: formData
        type: string
        required: true
        description: Nombre de usuario
      - name: password
        in: formData
        type: string
        required: true
        description: Contraseña del usuario
    responses:
      200:
        description: Página de inicio de sesión
      400:
        description: Error en los campos del formulario
    """
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
    """
    Página de instrucciones.
    ---
    responses:
      200:
        description: Página de instrucciones
    """
    titulo = "Instrucciones"
    return render_template('instrucciones.html', titulo=titulo)

# profesor
@app.route('/profesor')
def profesor():
    """
    Página principal del profesor.
    ---
    responses:
      200:
        description: Página del profesor
    """
    titulo = "Profesor"
    return render_template('profesor.html', titulo=titulo)

#Dashboard

# mejores
@app.route('/mejores')
def mejores():
    """
    Dashboard de mejores estudiantes.
    ---
    responses:
      200:
        description: Página de mejores estudiantes
    """
    return render_template('dashboards/mejores.html')

# peores
@app.route('/peores')
def peores():
    """
    Dashboard de peores estudiantes.
    ---
    responses:
      200:
        description: Página de peores estudiantes
    """
    return render_template('dashboards/peores.html')

# promedios
@app.route('/promedios')
def promedios():
    """
    Dashboard de promedios de estudiantes.
    ---
    responses:
      200:
        description: Página de promedios de estudiantes
    """
    return render_template('dashboards/promedios.html')

# alumnos
@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    """
    Consulta de información de estudiantes.
    ---
    parameters:
      - name: numLista
        in: formData
        type: string
        required: true
        description: Número de lista del estudiante
      - name: grupo
        in: formData
        type: string
        required: true
        description: Grupo del estudiante
    responses:
      200:
        description: Información del estudiante
      404:
        description: Estudiante no encontrado
    """
    if request.method == 'POST':
        num_lista = request.form['numLista'].strip()
        grupo = request.form['grupo'].strip().upper()
        
        # Realizar la consulta a la base de datos MySQL
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM estudiantes WHERE NumLista = %s AND Grupo = %s', (num_lista, grupo))
        estudiante = cursor.fetchone()
        cursor.close()
        
        if estudiante:
            # Convertir la fila en un diccionario para facilitar el acceso en la plantilla
            estudiante_dict = {
                'idEstudiante': estudiante[0],
                'NumLista': estudiante[1],
                'Grupo': estudiante[2],
                'Genero': estudiante[3],
                'CicloEscolar': estudiante[4],
                'Nivel1': estudiante[5],
                'Nivel2': estudiante[6],
                'Nivel3': estudiante[7],
                'PuntajeTotal': estudiante[8],
                'Promedio': float(estudiante[9]) if estudiante[9] is not None else None,
                'TiempoJugado': estudiante[10]
            }
            return render_template('dashboards/alumnos.html', estudiante=estudiante_dict)
        else:
            return render_template('dashboards/alumnos.html', message="No se encontró el estudiante.")
    return render_template('dashboards/alumnos.html')

# grupos
@app.route('/grupos')
def grupos():
    """
    Dashboard de grupos.
    ---
    responses:
      200:
        description: Página de grupos
    """
    return render_template('dashboards/grupos.html')

# genero
@app.route('/genero')
def genero():
    """
    Dashboard de géneros.
    ---
    responses:
      200:
        description: Página de géneros
    """
    return render_template('dashboards/genero.html')

# bloque de prueba
if _name_ == "_main_":
    app.run(debug=True)