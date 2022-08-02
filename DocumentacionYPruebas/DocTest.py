def suma(a,b):
    """
    la funcion suma(a,b), recibe dos parametros a y b.
    devuelve la suma de ambos

    >>> suma(5,10)
    15

    >>> suma(10,10)
    20

    >>> suma(20,20)
    40
    """
    return a+b

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

#Se usa siempre en scripts

#Ejecutar desde la termina con -v