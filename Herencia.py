'''}
                        -> Coche(velocidad, cilindrada) -> Camioneta(Carga)
vehiculo (color, ruedas)
                        ->Bicicleta(tipo(Urbana/Deportiva)) -> Motocicleta(velocidad, cilindrada)
Experimenta
Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
Recordatorio: Puedes utilizar el atributo especial de clase name de la siguiente forma para recuperar el nombre de la clase de un objeto:
'''

class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class Camioneta(Coche):
    carga = 0
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
def catalogar(lista, rueda):
    j = 0
    for i in lista:
        if (i.ruedas == rueda):
            print(type(i).__name__)
            print(i.color)
            print(i.ruedas)
            if (type(i).__name__ == Bicicleta):
                print(i.tipo)
            if(type(i).__name__ == Motocicleta):
                print(i.tipo)
                print(i.velocidad)
                print(i.cilindrada)
            if(type(i).__name__ == Coche):
                print(i.velocidad)
                print(i.cilindrada)
            if(type(i).__name__ == Camioneta):
                print(i.velocidad)
                print(i.cilindrada)
                print(i.carga)
            j += 1
    print("Se han encontrado {} vehículos con {} ruedas:".format(j, rueda))
    

lista = []
bici = Bicicleta("Azul", 2, "Urbana")
auto = Coche("Negro", 4, 240, 3600)
camio = Camioneta("Blanca", 4, 200, 3000, 145)
lista.append(bici)
lista.append(auto)
lista.append(camio)
catalogar(lista, 4)