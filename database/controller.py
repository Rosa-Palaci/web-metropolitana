import sqlite3 

def escuelaDB():
    conn = sqlite3.connect("escuela.db")
    conn.commit()
    conn.close()

def createTables():
    conn = sqlite3.connect("escuela.db")
    cursor = conn.cursor()
    # Ejecuta cada sentencia CREATE TABLE por separado
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estudiante (
            idEstudiante INTEGER PRIMARY KEY,
            Grupo VARCHAR(255),
            NumLista INTEGER,
            Genero BOOLEAN,
            CicloEscolar VARCHAR(255)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Maestros (
            idMaestro INTEGER PRIMARY KEY,
            usuario VARCHAR(255),
            password VARCHAR(255)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Partida (
            idPartida INTEGER PRIMARY KEY,
            nombre VARCHAR(255),
            idEstudiante INTEGER,
            idNivel INTEGER,
            puntaje INTEGER,
            fecha_jugada VARCHAR(255),
            minutos_jugados INTEGER,
            FOREIGN KEY (idEstudiante) REFERENCES Estudiante (idEstudiante),
            FOREIGN KEY (idNivel) REFERENCES Nivel (idNivel)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Nivel (
            idNivel INTEGER PRIMARY KEY,
            nombre VARCHAR(255),
            descripcion VARCHAR(255),
            escenario INTEGER,
            FOREIGN KEY (escenario) REFERENCES Escenario (idEscenario)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Escenario (
            idEscenario INTEGER PRIMARY KEY,
            nombreEscenario VARCHAR(255),
            descripcion VARCHAR(255)
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Admin (
            idAdmin INTEGER PRIMARY KEY,
            usuario VARCHAR(255),
            password VARCHAR(255)
        );
    """)
    conn.commit()
    conn.close()

def addAdmins():
    conn = sqlite3.connect("escuela.db")
    cursor = conn.cursor()
    
    # Agregar administradores
    admins = [
        ("leocanete@admin.com", "12345pass"),
        ("sergioruiz@admin.com", "12345pass"),
        ("chrisvallejo@admin.com", "12345pass")
    ]
    cursor.executemany("""
        INSERT INTO Admin (usuario, password) VALUES (?, ?)
    """, admins)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    escuelaDB()
    createTables()
    addAdmins()