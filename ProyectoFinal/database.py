import csv
import config

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
    
    def __str__(self):
        return "{} {} {}".format(self.dni, self.nombre, self.apellido)
    
class Clientes:

    lista = []
    conexion = config.CONEXION
    cursor = conexion.cursor()
    '''
    with open(config.DATABASE_PATH) as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for dni, nombre, apellido in  reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)
    '''
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    cli = Cliente(None, None, None)
    for cliente in clientes:
        cli.dni = cliente[0]
        cli.nombre = cliente[1]
        cli.apellido = cliente[2]
        lista.append(cli)
    cursor.close()
    
    @staticmethod
    def buscar(dni):
        conexion = config.CONEXION
        cursor = conexion.cursor()
        #for cliente in Clientes.lista:
        #    if cliente.dni == dni:
        #        return cliente
        cursor.execute("SELECT * FROM clientes WHERE dni={dni}")
        cursor.close()

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar(cliente)
        return cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                conexion = config.CONEXION
                cursor = conexion.cursor()
                cursor.execute("UPDATE clientes SET nombre='{}', apellido='{}' WHERE dni='{}'".format(nombre, apellido, dni))
                return Clientes.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                conexion = config.CONEXION
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM clientes WHERE dni='{}'".format(dni))
                conexion.commit()
                return cliente

    @staticmethod
    def guardar(cliente):
        conexion = config.CONEXION
        cursor = conexion.cursor()
        #with open(config.DATABASE_PATH, 'w') as fichero:
        #    writer = csv.writer(fichero, delimiter=";")
        #    for cliente in Clientes.lista:
        #        writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))
        cursor.execute("INSERT INTO clientes VALUES ('{}','{}','{}')".format(cliente.dni, cliente.nombre, cliente.apellido))
        conexion.commit()
        cursor.close()