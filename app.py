from flask import Flask, render_template, request, flash, url_for, redirect
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
    return render_template('dashboards/mejores.html')

# peores
@app.route('/peores')
def peores():
    return render_template('dashboards/peores.html')

# promedios
@app.route('/promedios')
def promedios():
    cursor = mysql.connection.cursor()
    query = """
    SELECT AVG(Nivel1) AS PromedioNivel1, AVG(Nivel2) AS PromedioNivel2, AVG(Nivel3) AS PromedioNivel3
    FROM estudiantes
    """
    cursor.execute(query)
    resultados = cursor.fetchone()
    cursor.close()

    if resultados:
        df = pd.DataFrame([resultados], columns=['PromedioNivel1', 'PromedioNivel2', 'PromedioNivel3'])
        
        fig = px.bar(df, title='Promedio Global por Nivel')
        fig.update_layout(
            xaxis_title='Nivel',
            yaxis_title='Promedio de Puntaje',
            xaxis=dict(tickmode='array', tickvals=[0, 1, 2], ticktext=['Nivel 1', 'Nivel 2', 'Nivel 3'])
        )
        
        graphHTML = fig.to_html(full_html=False)
        
        return render_template('dashboards/promedios.html', graphHTML=graphHTML)
    else:
        return render_template('dashboards/promedios.html', message="No hay datos disponibles.")


# alumnos
@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    if request.method == 'POST':
        num_lista = request.form['numLista'].strip()
        grupo = request.form['grupo'].strip().upper()
        
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM estudiantes WHERE NumLista = %s AND Grupo = %s', (num_lista, grupo))
        estudiante = cursor.fetchone()
        cursor.close()
        
        if estudiante:
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
    cursor = mysql.connection.cursor()
    query = """
    SELECT Grupo, PuntajeTotal, TiempoJugado
    FROM estudiantes
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()

    if resultados:
        df = pd.DataFrame(resultados, columns=['Grupo', 'PuntajeTotal', 'TiempoJugado'])
        
        fig = px.box(df, x='Grupo', y='PuntajeTotal', title='Distribución de Puntajes por Grupo')
        fig2 = px.box(df, x='Grupo', y='TiempoJugado', title='Distribución de Tiempo Jugado por Grupo')

        graphHTML = fig.to_html(full_html=False)
        graphHTML2 = fig2.to_html(full_html=False)

        return render_template('dashboards/grupos.html', graphHTML=graphHTML, graphHTML2=graphHTML2)
    else:
        return render_template('dashboards/grupos.html', message="No hay datos disponibles.")


# genero
@app.route('/genero')
def genero():
    cursor = mysql.connection.cursor()
    query = """
    SELECT Genero, AVG(PuntajeTotal) as PuntajePromedio
    FROM estudiantes
    GROUP BY Genero
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()

    if resultados:
        df = pd.DataFrame(resultados, columns=['Genero', 'PuntajePromedio'])
        
        fig = px.bar(df, x='Genero', y='PuntajePromedio', title='Puntaje Promedio por Género',
                     labels={'PuntajePromedio': 'Puntaje Promedio', 'Genero': 'Género'})
        
        graphHTML = fig.to_html(full_html=False)
        
        return render_template('dashboards/genero.html', graphHTML=graphHTML)
    else:
        return render_template('dashboards/genero.html', message="No hay datos disponibles.")


# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)