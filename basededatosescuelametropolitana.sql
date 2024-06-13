-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.7.0.6850
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura de base de datos para escuelametropolitana
CREATE DATABASE IF NOT EXISTS escuelametropolitana /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE escuelametropolitana;

-- Limpiar la tabla escuelametropolitana.administradores
DELETE FROM administradores;

-- Volcando estructura para tabla escuelametropolitana.administradores
CREATE TABLE IF NOT EXISTS administradores (
  idAdmin int(11) NOT NULL AUTO_INCREMENT,
  usuario varchar(200) NOT NULL,
  password varchar(200) NOT NULL,
  PRIMARY KEY (idAdmin)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;

/*
-- Tabla estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
  idEstudiante INT AUTO_INCREMENT PRIMARY KEY,
  NumLista INT NOT NULL,
  Grupo VARCHAR(1) NOT NULL,
  Genero VARCHAR(10) NOT NULL,
  CicloEscolar VARCHAR(255) NOT NULL,
  Nivel1 INT NOT NULL,
  Nivel2 INT NOT NULL,
  Nivel3 INT NOT NULL,
  PuntajeTotal INT AS (Nivel1 + Nivel2 + Nivel3),
  Promedio DECIMAL(10,2) AS (PuntajeTotal / 3),
  TiempoJugado INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_general_ci; */

-- Volcando datos para la tabla escuelametropolitana.administradores: ~4 rows (aproximadamente)
INSERT INTO administradores (idAdmin, usuario, password) VALUES
    (1, 'leocanete@admin.com', '12345pass'),
    (2, 'sergioruiz@admin.com', '12345pass'),
    (3, 'chrisvallejo@admin.com', '12345pass'),
    (4, 'marquiños@admin.com', '12345');
/*
-- Insertar estudiantes en el grupo A
INSERT INTO estudiantes (NumLista, Grupo, Genero, CicloEscolar, Nivel1, Nivel2, Nivel3, TiempoJugado, PuntajeTotal, Promedio) VALUES
(1, 'A', 'Femenino', '2023-2024', 67, 69, 42, 120, 178, 59.33),
(2, 'A', 'Femenino', '2023-2024', 7, 44, 93, 105, 144, 48),
(3, 'A', 'Femenino', '2023-2024', 60, 7, 0, 90, 67, 22.33),
(4, 'A', 'Femenino', '2023-2024', 55, 85, 93, 110, 233, 77.67),
(5, 'A', 'Femenino', '2023-2024', 91, 53, 76, 95, 220, 73.33),
(6, 'A', 'Masculino', '2023-2024', 48, 13, 95, 85, 156, 52),
(7, 'A', 'Masculino', '2023-2024', 45, 72, 202, 100, 319, 106.33),
(8, 'A', 'Femenino', '2023-2024', 17, 91, 71, 115, 179, 59.67),
(9, 'A', 'Masculino', '2023-2024', 24, 40, 51, 95, 115, 38.33),
(10, 'A', 'Masculino', '2023-2024', 39, 75, 20, 110, 134, 44.67);

-- Insertar estudiantes en el grupo B
INSERT INTO estudiantes (NumLista, Grupo, Genero, CicloEscolar, Nivel1, Nivel2, Nivel3, TiempoJugado, PuntajeTotal, Promedio) VALUES
(1, 'B', 'Masculino', '2023-2024', 55, 85, 93, 85, 233, 77.67),
(2, 'B', 'Masculino', '2023-2024', 91, 53, 76, 95, 220, 73.33),
(3, 'B', 'Masculino', '2023-2024', 48, 13, 95, 110, 156, 52),
(4, 'B', 'Femenino', '2023-2024', 45, 72, 202, 100, 319, 106.33),
(5, 'B', 'Femenino', '2023-2024', 17, 91, 71, 115, 179, 59.67),
(6, 'B', 'Masculino', '2023-2024', 24, 40, 51, 95, 115, 38.33),
(7, 'B', 'Masculino', '2023-2024', 39, 75, 20, 110, 134, 44.67),
(8, 'B', 'Femenino', '2023-2024', 84, 45, 63, 105, 192, 64),
(9, 'B', 'Femenino', '2023-2024', 55, 66, 77, 120, 198, 66),
(10, 'B', 'Masculino', '2023-2024', 88, 99, 11, 85, 198, 66);

-- Insertar estudiantes en el grupo C
INSERT INTO estudiantes (NumLista, Grupo, Genero, CicloEscolar, Nivel1, Nivel2, Nivel3, TiempoJugado, PuntajeTotal, Promedio) VALUES
(1, 'C', 'Femenino', '2023-2024', 45, 72, 202, 130, 319, 106.33),
(2, 'C', 'Femenino', '2023-2024', 17, 91, 71, 115, 179, 59.67),
(3, 'C', 'Femenino', '2023-2024', 24, 40, 51, 100, 115, 38.33),
(4, 'C', 'Masculino', '2023-2024', 39, 75, 20, 110, 134, 44.67),
(5, 'C', 'Masculino', '2023-2024', 84, 45, 63, 105, 192, 64),
(6, 'C', 'Masculino', '2023-2024', 55, 66, 77, 120, 198, 66),
(7, 'C', 'Femenino', '2023-2024', 88, 99, 11, 85, 198, 66),
(8, 'C', 'Femenino', '2023-2024', 60, 30, 90, 95, 180, 60),
(9, 'C', 'Masculino', '2023-2024', 20, 40, 70, 80, 130, 43.33),
(10, 'C', 'Femenino', '2023-2024', 10, 50, 100, 75, 160, 53.33);*/


/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;