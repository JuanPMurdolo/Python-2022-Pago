import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

#cursor.execute("CREATE TABLE users2 (dni VARCHAR(9) PRIMARY KEY, nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

'''users = [
    ('222222222', 'Hector', 27, 'hector@ejemplo.com'),
    ('222222223', 'Luis', 32, 'Luis@ejemplo.com'),   
    ('222222224','Ester', 27, 'Ester@ejemplo.com'),
    ('222222225', 'Mario', 32, 'Mario@ejemplo.com')
]'''

#cursor.executemany("INSERT INTO users2 VALUES (?,?,?,?)", users)


#cursor.execute('''
#CREATE TABLE productos (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nombre VARCHAR(100) NOT NULL,
#    marca VARCHAR(50) NOT NULL,
#    precio FLOAT NOT NULL)
#    ''')
'''
productos = [
    ('Teclado', 'Logitech', 19.95),
    ('Teclado', 'Razer', 20.95),
    ('Mouse', 'Logitech', 19.95),
    ('Mouse', 'Razer', 19.95),
    ('Pantalla 19"', 'Lg', 19.95),
    ('Pad', 'Logitech', 19.95),
]
'''

#cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

#cursor.execute("SELECT * FROM productos")

#productos = cursor.fetchall()
#for producto in productos:
#   print(producto)

cursor.execute('''
    CREATE TABLE users3(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        mail VARCHAR(100)
    )
''')

users = [
    ('222222222', 'Hector', 27, 'hector@ejemplo.com'),
    ('222222223', 'Luis', 32, 'Luis@ejemplo.com'),   
    ('222222224','Ester', 27, 'Ester@ejemplo.com'),
    ('222222225', 'Mario', 32, 'Mario@ejemplo.com')
]

cursor.executemany("INSERT INTO users3 VALUES (null,?,?,?,?)", users)


conexion.commit()
conexion.close()