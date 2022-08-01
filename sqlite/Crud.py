import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

#listar con filtro
#cursor.execute("SELECT * FROM users3 WHERE id=1")
#usuario = cursor.fetchone()
#print(usuario)

#Editar
cursor.execute("UPDATE users3 SET nombre='Juan Pengas', edad = 30 WHERE id=1")

#delete sin filtro para borrar toda la tabla
#cursor.execute("DELETE FROM users3")

#delete con filtro
#cursor.execute("DELETE FROM users3 WHERE id=1")

conexion.commit()
conexion.close()
