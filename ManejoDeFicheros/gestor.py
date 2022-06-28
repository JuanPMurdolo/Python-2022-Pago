'''
3) Utilizando como base el ejercicio de los personajes que hicimos, en este ejercicio tendrás que crear un gestor de personajes (gestor.py) para añadir 
y borrar la información de los siguientes personajes:

                Vida	    Ataque	    Defensa	    Alcance
Caballero	    4	        2	        4      	    2
Guerrero	    2	        4	        2	        4
Arquero	        2	        4	        1	        8

Deberás hacer uso del módulo pickle y todos los cambios que realices se irán guardando en un fichero binario personajes.pckl, 
por lo que aunque cerremos el programa los datos persistirán.

Crea dos clases, una Personaje y otra Gestor.
La clase Personaje deberá permitir crear un personaje con el nombre (que será la clase), 
y sus propiedades de vida, ataque, defensa y alcance (que deben ser números enteros positivos mayor que cero obligatoriamente).**

Por otro lado la clase Gestor deberá incorporar todos los métodos necesarios para añadir personajes, mostrarlos y borrarlos 
(a partir de su nombre por ejemplo) (tendrás que pensar una forma de hacerlo), además de los métodos esenciales para guardar los cambios en el fichero personajes.pckl 
que se deberían ejecutar automáticamente.
En caso de que el personaje ya exista en el Gestor entonces no se creará.
** Una vez lo tengas listo realiza las siguientes prueba en tu código: **

Crea los tres personajes de la tabla anterior y añádelos al Gestor.
Muestra los personajes del Gestor.
Borra al Arquero.
Muestra de nuevo el Gestor.
Sugerencias: El ejemplo con pickle que realizamos puede servirte como base.
'''
from io import open
import pickle

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance) -> None:
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    
    def __str__(self):
        return "{} => {} vida, {} ataque, {} defensa, {} alcance".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor:
    personajes = []

    def __init__(self) -> None:
        self.cargar()
    
    def agregar(self, p):
        for pTemp in self.personajes:
            if pTemp.nombre == p.nombre:
                return
        self.personajes.append(p)
        self.guardar()

    def borrar(self, nombre):
        for pTemp in self.personajes:
            if pTemp.nombre == nombre:
                self.personajes.remove(pTemp)
                self.guardar()
                print("\n Personaje {} Borrado".format(nombre))
                return
    
    def mostrar(self):
        if len(self.personajes) == 0:
            print("El gestor esta vacio")
            return
        for p in self.personajes:
            print(p)
    
    def cargar(self):
        fichero = open("personajes.pckl", "ab+")
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            pass
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format(len (self.personajes)))
        
    def guardar(self):
        fichero = open("personajes.pckl" , "wb")
        pickle.dump(self.personajes,  fichero)
        fichero.close()
    
G = Gestor()
G.agregar( Personaje("Caballero",4,2,4,2) )
G.agregar( Personaje("Guerrero",2,4,2,4) )
G.agregar( Personaje("Arquero",2,4,1,8) )
G.mostrar()
