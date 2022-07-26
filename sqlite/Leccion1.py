import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(50), edad INTEGER, email VARCHAR(100))")
#cursor.execute("INSERT INTO usuarios VALUES ('Juan Pablo',30,'ejemplo@gmail.com')")
#cursor.execute("SELECT * FROM usuarios")
#print(cursor)
#usuario = cursor.fetchone()
#print(usuario)

'''usuarios = [
    ('Juan', 20, 'alfa@gmail.com'),
    ('Pablo', 30, 'alfa@gmail.com'),
    ('Martin', 40, 'alfa@gmail.com'),
]'''

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

conexion.commit()

conexion.close()