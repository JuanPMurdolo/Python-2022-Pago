

lista = [1,2,3]

def hola():

    numero = 50

    def bienvenidos():
        return "HOLA!"
    
    print (locals())
    print(globals())
    print(globals().keys())

    return bienvenidos

def test(funcion):
    print(funcion())

def hola2():
    return "HOLA!"

def adios():
    print("Adios!")

#Monitorizar sin argumentos
def monitorizar(funcion):
    
    def decorar():
        print("\t Se esta a punto de ejecutar la funcion:",funcion.__name__)

        funcion()

        print("\t Se finalizo la ejecucion de la funcion:",funcion.__name__)
    return decorar


@monitorizar
def hola7():
    print("Hola!")

@monitorizar
def adios2():
    print("Adios2")

#Monitorizar con argumentos
def monitorizar_args(funcion):
    def decorar(*args, **kwargs):
        print("\t Se esta a punto de ejecutar la funcion:",funcion.__name__)

        funcion(*args, *kwargs)

        print("\t Se finalizo la ejecucion de la funcion:",funcion.__name__)
    return decorar

@monitorizar_args
def saludo(texto):
    print(texto)

saludo("HOLA")

