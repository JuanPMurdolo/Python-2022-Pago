import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(50), edad INTEGER, email VARCHAR(100))")
cursor.execute("INSERT INTO usuarios VALUES ("Juan Pablo",30,"ejemplo@gmail.com")")

conexion.close()