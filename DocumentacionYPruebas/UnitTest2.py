import unittest

def doblar(a): return a*2

class PruebaTextFixture(unittest.TestCase):

    def setUp(self) -> None:
        print("Preparando el contexto")
        self.numeros = [1,2,3,4,5]

    def text(self):
        print("Realizando prueba")
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r,[2,4,6,8,10])

    def tearDown(self) -> None:
        print("Destruyendo el  contexto")
        del(self.numeros)

if __name__ == '__main__':
    unittest.main()