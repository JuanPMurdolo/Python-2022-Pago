#1 < 2 and 2 < 3
#devuelve True

#(3>2) and (2>1)
#True

#(3 > 2) > 1
#False

numero = 35
if numero >= 0 and numero <= 100:
    print("El numero {} se encuentra entre 0 y 100".format(numero))
else:
    print("El numero {} no se encuentra entre 0 y 100".format(numero))

if 0 <= numero <= 100:
    print("El numero {} se encuentra entre 0 y 100".format(numero))
else:
    print("El numero {} no se encuentra entre 0 y 100".format(numero))
