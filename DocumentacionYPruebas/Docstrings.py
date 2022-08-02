def hola(arg):
    """Este es el docstring de la funcion"""
    print('Hola', arg, "|")

hola("Hector")

#help(hola)

class Clase:
    """Este es el docstring de una clase"""
    def __init__(self) -> None:
        """Docstring del inicializador de la clase"""
        """puede ser varias lineas
        separadas asi
        """
        pass

    def metodo(self):
        """Docstring del metodo de clase"""
        pass

#Se invoca asi
o = Clase()
help(o)

'''Se puede llevar a paquetes tambien haciendo 
que modulos de un paquete tengan su texto de help'''

