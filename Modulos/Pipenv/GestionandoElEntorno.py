#Gestionando el entorno

'''
Tenemos dos formas de trabajar con un entorno virtual:

Desde su interior activando el entorno con pipenv shell.
Desde el exterior sin activarlo con pipenv run.
Ambas formas nos permitirán ejecutar comandos fuera del entorno nativo.
'''

#Mediante pipenv shell

'''
Nota: Si utilizáis Windows es muy importante que ejecutéis las siguientes instrucciones en una terminal CMD.

Si activamos un entorno aparecerá en la parte delantera de la terminal su nombre entre paréntesis:

(superproyecto)
En este momento, todas las instrucciones que realicemos harán referencia al entorno virtual, por ejemplo:

> python -c "import sys; print(sys.executable)"
Para salir del entorno virtual escribiremos:

> exit
Personalmente no me gusta utilizar la shell, considero que puede llevar a confusión a la hora de ejecutar los comandos 
y por esa razón a partir de ahora utilizaremos siempre pipenv run.
'''

#Mediante pipenv run¶

'''
Ejecutar los comandos desde el exterior requiere escribir un poco más, pero al tener la referencia explícita evitaremos confusiones.

Podemos ejecutar fácilmente una instrucción en el Python de la máquina:

> python -c "import sys; print(sys.executable)"

/usr/local/bin/python
O hacer referencia al intérprete del entorno virtual:

> pipenv run python -c "import sys; print(sys.executable)"

'''

#Ejecutar un script

'''
Si tenemos un script en el proyecto ejecutarlo con el entorno virtual es intuitivo:

hola.py

import sys 

print("Hola mundo!")
print(sys.executable)
Solo debemos indicarle que utilice el python virtual y pasarle el script:

> pipenv run python hola.py

Hola mundo!
'''

#Listar paquetes

'''
También podemos consultar los paquetes instalados en el entorno fácilmente:

pipenv run pip list

Package    Version
---------- -------
pip        22.1.2
setuptools 62.6.0
wheel      0.37.1
Pipenv tiene su propia instrucción para consultar los paquetes del entorno sin requerir la sintaxis anterior:

> pipenv graph
Si no hemos instalado ningún paquete esta instrucción no devolverá nada, vamos a instalar algunos.
'''

#Instalar paquetes
'''
La forma de instalar un paquete en Pipenv es mediante:

> pipenv install <package>
Por ejemplo:

> pipenv install numpy
Al instalar una dependencia de esta forma se agregará al Pipfile:

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
numpy = "*"

[dev-packages]

[requires]
python_version = "3.10"
'''

#Paquetes de desarrollo
'''
Fijaros que se agrega al bloque [packages] y no a [dev-packages], esto es porque son para dos cosas diferentes.

Un módulo tiene como mínimo dos versiones:

Versión Retail: Para clientes que quieran utilizar el módulo.
Versión Dev: Para programadores que quieran desarrollar el módulo.
Cuando un paquete es necesario solo para los desarrolladores podemos instalarlo como dependencia de desarrollo.

Por ejemplo imaginemos que numpy es necesario para el cliente final pero pandas solo se utiliza en pruebas durante el desarrollo, en ese caso lo instalaremos con:

> pipenv install pandas --dev
Ahora el Pipfile contendrá:

[packages]
numpy = "*"

[dev-packages]
pandas = "*"
'''

#Paquetes con versión exacta
'''
Y supongamos que necesitamos matplotlib para que los clientes vean unos gráficos, pero la versión más reciente no nos sirve, necesitamos explícitamente la 3.5.1.

Para instalar esa dependencia exacta podemos hacer:

> pipenv install matplotlib==3.5.1
[packages]
numpy = "*"
matplotlib = "==3.5.1"
'''
#Actualizar y downgradear paquetes
'''
Si necesitamos actualizar o downgradear podemos hacerlo forzando la versión, por ejemplo para downgradear a numpy==1.23.0 haremos:

> pipenv install numpy==1.23.0
[packages]
numpy = "==1.23.0"
matplotlib = "==3.5.1"
'''
#Desinstalar paquetes
'''
Y si queremos desinstalar un paquete del entorno podemos hacer:

> pipenv uninstall numpy

Uninstalling numpy...
Found existing installation: numpy 1.23.0
Uninstalling numpy-1.23.0:
  Successfully uninstalled numpy-1.23.0
'''

#Comprobar Seguridad
'''
Finalmente, una prueba que podemos realizar para saber si las dependencias son íntegras y seguras es:

> pipenv check

Checking PEP 508 requirements...
Passed!
Checking installed package safety...
All good!
'''

