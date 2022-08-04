#Antes de comenzar hay algunos puntos que no debemos olvidar.

'''
Los entornos pipenv se crean siempre para un proyecto concreto utilizando como referencia su directorio. 
Si creamos un entorno virtual para un proyecto y luego le cambiamos el directorio, ya sea el nombre o la ubicación, éste dejará de funcionar.

Tampoco podemos crear entornos virtuales dentro de otros entornos virtuales, no se pueden tener entornos anidados. 
Si creamos un entorno en un supuesto directorio XXXX e intentamos crear otro en el subdirectorio XXXX/YYYY no funcionará.

La versión de Python del entorno virtual es la misma que la del intérprete nativo donde hemos instalado Pipenv, estableciéndose ésta como su versión por defecto. 
Si un paquete no es compatible con el intérprete nativo tampoco lo será con el del entorno virtual.
'''

#Dicho lo cuál, empecemos creando un directorio en el escritorio para un nuevo proyecto:
'''
> cd Desktop
> mkdir superproyecto
'''

#Vamos a crear un entorno virtual para nuestro proyecto, recordad que se referencia en base a la ubicación del directorio por tanto nos situaremos dentro antes de crearlo:
#> cd superproyecto

#Podemos crear un nuevo entorno virtual en el proyecto simplemente escribiendo el comando:
#> pipenv install  # También con: python -m pipenv install

#A partir de este momento el directorio tiene un entorno enlazado, ya sea en la raíz o cualquier subdirectorio Pipenv sabrá determinar que ahí hay un entorno virtual.

'''
Si revisamos el output veremos información acerca del entorno virtual creado:

Using /Library/Frameworks/Python.framework/Versions/3.10/bin/python3 (3.10.5) to create virtualenv...

Como véis el directorio del entorno tiene el mismo nombre del proyecto y un código único. Dentro encontraremos un par de carpetas lib y bin con las librerías y los binarios. 
Es en ésta última donde se encuentra la copia del intérprete python y el gestor de paquetes pip


'''

#De vuelta en la terminal, vamos al directorio del proyecto
#> cd ~/Desktop/superproyecto

#Desde cualquier lugar del proyecto podemos consultar el intérprete de Python con el comando:
#> pipenv --py

#Si cambiamos el nombre del directorio del proyecto, éste dejará de funcionar

#Con esto hemos aprendido que un entorno virtual crea una copia del Python nativo en un directorio específico y que los cambios relacionados ocasionarán que deje de funcionar.

#Pipfile y Pipfile.lock
#Antes de terminar esta lección hablemos de estos dos ficheros que se han creado en el directorio de nuestro proyecto:
#Según la documentación oficial, los pipfiles contienen información sobre las dependencias del proyecto y reemplazan el archivo requirements.txt ámpliamente utilizado.

#Pipfile
#Se requiere un Pipfile en el repositorio para que los usuarios que lo clonen puedan instalarlas en la máquina escribiendo pipenv install.
#Este es el contenido del fichero Pipfile del entorno recién creado:
'''
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]

[requires]
python_version = "3.10"
'''

#Contiene diferentes bloques con información de la fuente del repositorio, las dependencias normales y de desarrollo y los requisitos.

#Como véis la versión por defecto del entorno virtual es la 3.10, la misma del entorno nativo. 
# Si compartiésemos nuestro proyecto, un usuario con una versión distinta no podría instalarlo, 
# sería necesario que ese usuario edite la línea y la cambie por su versión de Python nativo.

#Esto se indica en la documentación:
'''
Specify your target Python version in your Pipfile’s [requires] section. Ideally you should only have one target 
Python version, as this is a deployment tool. python_version should be in the format X.Y and python_full_version should be in X.Y.Z format.

Nota: Cambiar la versión manualmente puede ocasionar que algunas dependencias no se instalen correctamente.
'''

#Pipfile.lock

'''
Este fichero tiene como objetivo especificar, en función de los paquetes presentes en Pipfile, 
qué versión específica de estos debe usarse, evitando los riesgos de actualizar automáticamente los paquetes que dependen unos de otros 
y romper el árbol de dependencias del proyecto.

Este es el contenido de mi Pipfile.lock, como véis contiene hashes para asegurar 100% la integridad de los paquetes necesarios:
'''

'''
{
    "_meta": {
        "hash": {
            "sha256": 
                "fedbd2ab7afd84cf16f128af0619749267b62277b4cb6989ef16d4bef6e4eef2"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.10"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {},
    "develop": {}
}
'''
#Por regla general nunca modificaremos manualmente un fichero Pipfile.lock, solo lo haremos mediante la instrucción pipenv lock en caso de necesitarlo.




