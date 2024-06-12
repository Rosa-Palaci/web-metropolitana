import sqlite3
import random

def escuelaDB():
    conn = sqlite3.connect("escuela.db")
    conn.commit()
    conn.close()

def createTables():
    conn = sqlite3.connect("escuela.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Estudiante (
            idEstudiante INTEGER PRIMARY KEY,
            Grupo VARCHAR(255),
            NumLista INTEGER,
            Genero TEXT,
            CicloEscolar VARCHAR(255),
            Nivel1 INTEGER,
            Nivel2 INTEGER,
            Nivel3 INTEGER,
            PuntajeTotal INTEGER,
            Promedio DECIMAL(10,2),
            TiempoJugado INTEGER
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

def addStudents():
    conn = sqlite3.connect("escuela.db")
    cursor = conn.cursor()
    students = []
    for grupo in ['A', 'B', 'C']:  # Crear estudiantes para cada grupo
        for idEstudiante in range(1, 11):  # 10 estudiantes por grupo
            numLista = idEstudiante
            genero = random.choice(["Femenino", "Masculino"])
            cicloEscolar = "2023-2024"
            nivel1 = random.randint(0, 100)
            nivel2 = random.randint(0, 100)
            nivel3 = random.randint(0, 100)
            puntajeTotal = nivel1 + nivel2 + nivel3
            promedio = round(puntajeTotal / 3, 2)
            tiempoJugado = random.randint(0, 120)
            students.append((idEstudiante + (30 * (grupo == 'B')) + (60 * (grupo == 'C')), grupo, numLista, genero, cicloEscolar, nivel1, nivel2, nivel3, puntajeTotal, promedio, tiempoJugado))
    
    cursor.executemany("""
        INSERT INTO Estudiante (
            idEstudiante, Grupo, NumLista, Genero, CicloEscolar, Nivel1, Nivel2, Nivel3, PuntajeTotal, Promedio, TiempoJugado
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, students)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    escuelaDB()
    createTables()
    addAdmins()
    addStudents()
