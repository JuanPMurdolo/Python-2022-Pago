def multiple(numero):
    if numero % 5 == 0:
        return True

def doblar(numero):
    return numero*2

class Persona:

    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)

numeros = [2,3,4,55,6,7,10,50]

list(filter(multiple, numeros))

f = filter(multiple, numeros)
next(f)

filter(lambda numero: numero%5==0, numeros)

personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manuel", 78),
    Persona("Eduardo", 12)
]

menores = filter(lambda persona: persona.edad < 18, personas)

for menor in  menores:
    print(menor)

#Funcion Map
m = map(doblar, numeros)
print(map(doblar, numeros))
print(next(m))
print(next(m))

list(map(lambda x: x*2, numeros))

a =[1,2,3,4,5]
b=[6,7,8,9,10]
c=[11,12,13,14,15]
print(list(map(lambda x,y:x*y,a,b)))
print(list(map(lambda x,y,z:x*y*z, a,b,c)))

'''
Funciones anónimas
Utilizando dos funciones anónimas anidadas en una sola línea, debes:

Mapear una lista llamada numeros de la cuál no conoces su contenido y dividir sus valores entre 2.

A su vez debes filtrar el resultado de esa lista mapeada y eliminar los números que no sean múltiples de 5.

El resultado final será una lista cuyos números son la mitad de los originales y sólo quedarán los que sean múltiples de 5.

Notas:

Única y exclusivamente debes editar la línea 4.
'''
numeros = list(filter(lambda x: x % 5 == 0, map(lambda x: x/2,numeros)))
