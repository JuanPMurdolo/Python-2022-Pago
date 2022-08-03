import csv
import unittest
import database as db
import copy
import helpers
import config

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista=[
            db.Cliente("123", "Jose", "Perez"),
            db.Cliente("456", "Martin", "Pocho"),
            db.Cliente("326", "Martin", "Pocho"),
            db.Cliente("789", "Maria", "Barrios")
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar("123")
        cliente_inexistente = db.Clientes.buscar("105")
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear("103", "Juan", "M")
        self.assertEqual(len(db.Clientes.lista), 5)
        self.assertEqual(nuevo_cliente.dni, "103")
        self.assertEqual(nuevo_cliente.nombre, "Juan")
        self.assertEqual(nuevo_cliente.apellido, "M")

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar("123"))
        print(cliente_a_modificar)
        cliente_modificado = db.Clientes.modificar("326", "Pablo", "M")
        self.assertEqual(cliente_a_modificar.nombre, "Jose")
        self.assertEqual(cliente_modificado.nombre, "Pablo")

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar("789")
        cliente_rebuscado = db.Clientes.buscar("789")
        self.assertEqual(cliente_borrado.dni, "789")
        self.assertIsNone(cliente_rebuscado)

    def test_validar_dni(self):
        self.assertTrue(helpers.validar_dni("027", db.Clientes.lista))
        self.assertFalse(helpers.validar_dni("A28", db.Clientes.lista))
        self.assertFalse(helpers.validar_dni("A23", db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar("123")
        db.Clientes.borrar("456")
        db.Clientes.borrar("326")
        db.Clientes.modificar("789","Faso","Lita")

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH) as fichero:
            reader = csv.reader(fichero, delimiter=";")
            dni, nombre, apellido = next(reader)
        
        self.assertEqual(dni, "789")
        self.assertEqual(nombre, "Faso")
        self.assertEqual(apellido, "Lita")
