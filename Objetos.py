'''
Preparación
Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, o si es el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

Nota: La función raíz cuadrada en Python sqrt() se debe importar del módulo math y utilizarla de la siguiente forma:

import math
math.sqrt(9)
> 3.0
Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area.
Puedes identificar fácilmente estos valores si intentas dibujar el cuadrado a partir de su diagonal. Si andas perdido, prueba de dibujarlo en un papel, ¡seguro que lo verás mucho más claro! Además recuerda que puedes utilizar la función abs() para saber el valor absolute de un número.

Experimentación
Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
Consulta a que cuadrante pertenecen el punto A, C y D.
Consulta los vectores AB y BA.
(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
Crea un rectángulo utilizando los puntos A y B.
Consulta la base, altura y área del rectángulo.
'''

import math

class Punto:
    x = 0
    y = 0
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "El punto es ({},{})".format(self.x, self.y)
    
    def cuadrante(self):
        if (self.y > 0):
            if (self.x > 0):
                return ("El punto esta en el primer cuadrante")
            elif (self.x < 0):
                return("el punto esta en el 2do cuadrante")
        elif (self.y < 0):
            if (self.x > 0):
                return ("El punto esta en el 4to cuadrante")
            elif (self.x < 0):
                return("el punto esta en el 3er cuadrante")
        elif (self.x == 0 and self.y == 0):
            return("el punto se encuentra en el origen")
    
def vector(punto1: Punto, punto2: Punto) -> Punto:
    puntoNuevo = Punto()
    puntoNuevo.x = (punto2.x - punto1.x)
    puntoNuevo.y = (punto2.y - punto1.y)
    return puntoNuevo

def distancia(punto1: Punto, punto2: Punto) -> float:
    x = math.pow((punto2.x - punto1.x),2)
    y = math.pow((punto2.y - punto1.y),2)
    d = math.sqrt(x + y)
    return d

class Rectangulo:

    def __init__(self, inicial=Punto(), final=Punto) -> None:
        self.pInicial = inicial
        self.pFinal = final
    
    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print("La base del rectángulo es {}".format( self.base ))

    def altura(self):
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        print("La altura del rectángulo es {}".format( self.altura ))
    
    def area(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        self.area = self.base * self.altura
        print("El área del rectángulo es {}".format( self.area ) )

puntoA = Punto(2,3)
puntoB = Punto(5,5)
puntoC = Punto(-3,-1)
puntoD = Punto()
print(str(puntoA))
print(str(puntoB))
print(str(puntoC))
print(str(puntoD))
print(puntoA.cuadrante())
print(puntoB.cuadrante())
print(puntoC.cuadrante())
print(puntoD.cuadrante())
print(vector(puntoA,puntoB))
print(vector(puntoB, puntoA))
print(distancia(puntoA, puntoB))
print(distancia(puntoB, puntoA))
d1 = distancia(puntoD, puntoA)
d2 = distancia(puntoD, puntoB)
d3 = distancia(puntoD, puntoC)
if (d1 > d2 and d1 > d3):
    print("El punto A esta mas lejos del origen")
if (d2 > d1 and d2 > d3):
    print("El punto B esta mas lejos del origen")
if (d3 > d2 and d3 > d1):
    print("El punto C esta mas lejos del origen")
rectangulo = Rectangulo(puntoA, puntoB)
rectangulo.base()
rectangulo.altura()
rectangulo.area()
