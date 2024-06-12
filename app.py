from flask import Flask, render_template, request, flash, url_for, redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'escuelametropolitana.cbcweu0impys.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'AdminRosa'
app.config['MYSQL_PASSWORD'] = 'Rv431!Pb'
app.config['MYSQL_DB'] = 'escuelametropolitana'

mysql = MySQL(app)

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
        cursor.execute('SELECT * FROM Admin WHERE usuario = %s AND password = %s', (usuario, password))
        admin = cursor.fetchone()
        cursor.close()

        if admin:
            flash('Inicio exitoso', 'success')
            return redirect(url_for('instrucciones'))
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


# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)