import sys
import sqlite3

DATABASE_PATH = "clientes.csv"
CONEXION = sqlite3.connect("clientes.db")
CURSOR = CONEXION.cursor()

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/clientes_test.csv"