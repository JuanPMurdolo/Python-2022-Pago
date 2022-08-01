'''
1.1) A lo largo de estos ejercicios vamos a crear un pequeño sistema para gestionar los platos del menú de un restaurante. Por ahora debes empezar creando un script llamado restaurante.py y dentro una función crear_bd() que creará una pequeña base de datos restaurante.db con las siguientes dos tablas:

* *Si ya existen deberá tratar la excepción y mostrar que las tablas ya existen. En caso contrario mostrará que se han creado correctamente. **

CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)
CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))
Nota: La línea FOREIGN KEY(categoria_id) REFERENCES categoria(id) indica un tipo de clave especial (foránea), por la cual se crea una relación entre la categoría de un plato con el registro de categorías.

** Llama a la función y comprueba que la base de datos se crea correctamente.**

1.2) Crea una función llamada agregar_categoria() que pida al usuario un nombre de categoría y se encargue de crear la categoría en la base de datos (ten en cuenta que si ya existe dará un error, por que el nombre es UNIQUE).

** Ahora, crea un pequeño menú de opciones dentro del script, que te de la bienvenida al sistema y te permita Crear una categoría o Salir. Añade las siguientes tres categorías utilizando este menú de opciones:**

Primeros
Segundos
Postres
1.3) Crea una función llamada agregar_plato() que muestre al usuario las categorías disponibles y le permita escoger una (escribiendo un número).

Luego le pedirá introducir el nombre del plato y lo añadirá a la base de datos, teniendo en cuenta que la categoria del plato concuerde con el id de la categoría y que el nombre del plato no puede repetirse (no es necesario comprobar si la categoría realmente existe, en ese caso simplemente no se insertará el plato).

Agrega la nueva opción al menú de opciones y añade los siguientes platos:

Primeros: Ensalada del tiempo / Zumo de tomate
Segundos: Estofado de pescado / Pollo con patatas
Postres: Flan con nata / Fruta del tiempo
1.4) Crea una función llamada mostrar_menu() que muestre el menú con todos los platos de forma ordenada: los primeros, los segundos y los postres. Optativamente puedes adornar la forma en que muestras el menú por pantalla.
'''


from multiprocessing import context
import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("CREATE TABLE categoria(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(100) UNIQUE NOT NULL)")
    except  sqlite3.OperationalError:
        print("la tabla categoria ya existe")
    else:
        print("Se creo la tabla categoria")
    try:
        cursor.execute('''
            CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id)
            )
        ''')
    except  sqlite3.OperationalError:
        print("La tabla plato ya existe")
    else:
        print("Se creo la tabla plato")
    conexion.close()

def agregar_categoria():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    categ = input("Agregue un nuevo nombre para la categoria: ")
    try:
        cursor.execute("INSERT INTO categoria VALUES (null,'{}')".format(categ))
    except sqlite3.IntegrityError:
        print("La categoria ya existe")
    else:
        print("Categoría '{}' creada correctamente.".format(categ))
    conexion.commit()
    conexion.close()

def menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
    categorias = cursor.execute("SELECT * FROM categoria").fetchall()	
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("\t{}".format(plato[1]))
    conexion.close()

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    categs = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria para añadir al plato")
    for cat in categs:
        print("[{}] {}".format(cat[0], cat[1]))

    categoria_usuario = int(input("> "))
    plato = input("¿Nombre del nuevo plato?\n> ")
    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(plato, categoria_usuario) )
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe.".format(plato))
    else:
        print("Plato '{}' creado correctamente.".format(plato))

    conexion.commit()
    conexion.close()

crear_bd()

while True:
    print("\nBienvenido al gestor del restaurante!")
    opcion= input("\nIntroduce una opción:\n[1] Agregar una categoría\n[2] Agregar un plato\n[3] Mostrar el menú\n[4] Salir del programa\n\n> ")

    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        menu()
    elif opcion == "4":
        print("Saliendo")
        break
    else:
        print("Opción incorrecta")
    
