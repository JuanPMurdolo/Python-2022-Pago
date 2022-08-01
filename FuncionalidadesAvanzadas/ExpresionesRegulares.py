import re

#Buscar 
def buscar(patrones, texto):
    for patron in patrones:
        print( re.findall(patron, texto))

#Search
texto = "En esta cadena se encuenta una palabra magica"
re.search('magica', texto)
#Si devuelve vacio es que no encontro nada, si devuele un objeto
#de tipo match es que si existe
palabra = "magica"
encontrado = re.search(palabra, texto)

#el mejor if seria
if encontrado is not None:
    print("Se encontro la palabra")
else:
    print("No se encontro la palabra")

print(encontrado.start())
print(encontrado.end())
print(encontrado.span())
print(encontrado.string)

#match
#Match solo busca al principio de la string
texto = "Hola Mundo"
print(re.match('Hola', texto))

#split
#Dividir una cadena a partir de un patron
texto = "Vamos a dividir esta cadena"
print(re.split(" ", texto))

#sub
#sustituye todas las coincidencias en una cadena
texto = "Hola Amigo"
print(re.sub("Hola", "Chau", texto))

#findall
#buscar las coincidencias en una cadena
texto = "hola adios hola hola"
print(re.findall("hola", texto))
print(len(re.findall("hola", texto)))
texto = "hola adios hola hola hello"
print(re.findall("(hola|hello)", texto))
print(len(re.findall("(hola|hello)", texto)))

#Patrones con sintaxis repetidas
texto = "hla hola hoola hooola hooooola"
patrones = ['hla', 'hola', 'hoola']
buscar(patrones, texto)

#Con meta-carácter *
#Lo utilizaremos para definir ninguna o más repeticiones de la letra a la izquierda del meta-carácter:
patrones = ['ho','ho*','ho*la','hu*la']  # 'ho', 'ho[0..N]', 'ho[0..N]la', 'hu[0..N]la'
buscar(patrones, texto)

#Con meta-carácter +
#Lo utilizaremos para definir una o más repeticiones de la letra a la izquierda del meta-carácter:
patrones = ['ho*', 'ho+']  # 'ho[0..N], 'ho[1..N]'
buscar(patrones, texto)

#Con meta-carácter ?
#Lo utilizaremos para definir una o ninguna repetición de la letra a la izquierda del meta-carácter:
patrones = ['ho*', 'ho+', 'ho?', 'ho?la']  # 'ho[0..N], 'ho[1..N]', 'ho[0..1]', 'ho[0..1]la'
buscar(patrones, texto)

#Con número de repeticiones explícito {n}
#Lo utilizaremos para definir 'n' repeticiones exactas de la letra a la izquierda del meta-carácter:
patrones = ['ho{0}la', 'ho{1}la', 'ho{2}la']  # 'ho[0]la', 'ho[1]la', 'ho[2]la'
buscar(patrones, texto)

#Con número de repeticiones en un rango {n, m}
#Lo utilizaremos para definir un número de repeticiones variable entre 'n' y 'm' de la letra a la izquierda del meta-carácter:
patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,9}la']  # 'ho[0..1]la', 'ho[1..2]la', 'ho[2..9]la'
buscar(patrones, texto)

#Trabajando con conjuntos de caracteres [ ]
#Cuando nos interese crear un patrón con distintos carácteres, podemos definir conjuntos entre paréntesis:
texto = "hala hela hila hola hula"
patrones = ['h[ou]la', 'h[aio]la', 'h[aeiou]la']
buscar(patrones, texto)

texto = "haala heeela hiiiila hoooooola"
patrones = ['h[ae]la', 'h[ae]*la', 'h[io]{3,9}la']
buscar(patrones, texto)

#Exclusión en grupos [^ ]
#Cuando utilizamos grupos podemos utilizar el operador de exclusión ^ para indicar una búsqueda contraria:
texto = "hala hela hila hola hula"

patrones = ['h[o]la', 'h[^o]la'] 
buscar(patrones, texto)

#Rangos [ - ]
'''
Otra característica que hace ultra potentes los grupos, es la capacidad de definir rangos. Ejemplos de rangos:

[A-Z]: Cualquier carácter alfabético en mayúscula (no especial ni número)
[a-z]: Cualquier carácter alfabético en minúscula (no especial ni número)
[A-Za-z]: Cualquier carácter alfabético en minúscula o mayúscula (no especial ni número)
[A-z]: Cualquier carácter alfabético en minúscula o mayúscula (no especial ni número)
[0-9]: Cualquier carácter numérico (no especial ni alfabético)
[a-zA-Z0-9]: Cualquier carácter alfanumérico (no especial)

Tened en cuenta que cualquier rango puede ser excluido para conseguir el patrón contrario.
'''
texto = "hola h0la Hola mola m0la M0la"

patrones = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', '[A-Z][A-z0-9]{3}'] 
buscar(patrones, texto)

#Códigos escapados \
'''
Si cada vez que quisiéramos definir un patrón variable tuviéramos que crear rangos, al final tendríamos expresiones regulares gigantes. Por suerte su sintaxis también acepta una serie de caracteres escapados que tienen un significo único. Algunos de los más importantes son:

El problema que encontraremos en Python a la hora de definir código escapado, es que las cadenas no tienen en cuenta el \ a no ser que especifiquemos que son cadenas en crudo (raw), por lo que tendremos que precedir las expresiones regulares con una 'r'.
'''
texto = "Este curso de Python se publicó en el año 2016"

patrones = [r'\d+', r'\D+', r'\s', r'\S+', r'\w+', r'\W+'] 
buscar(patrones, texto)

print("Fin")


