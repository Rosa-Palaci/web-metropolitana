from flask import Flask, render_template 
app = Flask(__name__)
# rutas
@app.route('/')
def home():
    titulo = "pagina inicio"
    return render_template('index.html')

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