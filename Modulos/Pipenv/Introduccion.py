'''
Configuración previa
Instalación de Pipenv por si alguien no lo tiene:

pip install pipenv
También se puede instalar desde el propio Jupyter Notebook con una exclamación delante:

!pip install pipenv
'''

#Entornos Virtuales
#Python y PIP
#Cuando ejecutamos Python generalmente lo hacemos a través del intérprete instalado en nuestro sistema,
#podemos consultar donde se encuentra ese entorno ejecutando una simple consulta en el módulo sys:

import sys
print(sys.executable)

#Podemos consultar la versión del intérprete desde una terminal:
#!python --version  en su defecto utilizar python3

#El intérprete de Python tiene su propio gestor de paquetes llamado pip:
#!pip --version
#!python -m pip --version

#Cada intérprete tiene asignado un solo un gestor de paquetes pip, eso significa que solo podemos instalar una versión de el mismo paquete:
#!pip list

'''
¿No estáis de acuerdo conmigo en que si desarrollamos diferentes proyectos, es posible que necesitemos versiones diferentes de un mismo paquete?

Por ejemplo imaginad que empezamos un proyecto con la versión 1 de un paquete como dependencia y al poco lo actualizan a la 2. Sin embargo no podemos actualizarlo 
porque han cambiado cosas y el proyecto quedaría inservible. 
Si a eso le sumamos que paralelamente necesitamos instalar sí o sí la versión 2 para otro proyecto qué podemos hacer?
'''

#Entornos virtuales
#Los desarrolladores de Python son consicientes de este problema y por eso el intérprete incorpora un módulo interno llamado venv:
#!python -m venv -h
#Este módulo permite crear copias del entorno nativo de Python con su propio gestor pip llamadas entornos virtuales.

#Como manejar entornos virtuales con venv requiere mucho trabajo aprenderemos un módulo más moderno para hacer lo mismo y más:

#Pipenv

#Tal como su nombre indica, Pipenv es pip + venv, un conjunto de funcionalidades que permite gestionar entornos virtuales y sus dependencias:
#!python -m pipenv -h






