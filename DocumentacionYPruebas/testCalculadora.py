import unittest
from Calculadora import Calculadora
class TestCalculadora(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculadora()

    def test_valor_inicial(self):
        self.assertEqual(self.calc.value, 0)

    def test_metodo_suma(self):
        self.calc.sumar(1,3)
        self.assertEqual(self.calc.value, 4)

    def test_metodo_restar(self):
        self.calc.restar(3,1)
        self.assertEqual(self.calc.value, 2)