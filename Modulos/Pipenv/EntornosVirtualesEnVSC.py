#Entornos virtuales en VSC

#Nota: En Windows os recomiendo establecer la terminal por defecto a la CMD presionando F1, buscando la opción default shell 
# y en el desplegable seleccionar la cmd o línea de comandos. Luego cerrar todas las terminales abiertas y reiniciar el programa:

#Si abrimos un proyecto con un entorno virtual en el editor e intentamos editar un fichero python en su interior (extensión .py), 
# desde la parte inferior podemos establecer en cualquier momento el intérprete para el proyecto (si no nos aparece en la lista buscar el nombre del proyecto):

#Al guardar o ejecutar un script .py con el intérprete virtual seleccionado VSC intentará cargar e instalar los paquetes de linting y autoformateo, 
#os recomiendo instalar todo lo que el editor os sugiera:

#A partir de este momento, y cada vez que se abra una terminal en el proyecto, se activará el entorno virtual automáticamente (aquello que vimos de pipenv shell):

#Ya podremos trabajar con el entorno e incluso los scripts se ejecutarán automáticamente con el intérprete aislado.

#En caso de no querer activar el entorno automáticamente, podemos cambiar la opción python.terminal.activateEnvironment de la configuración a falso:
#En este punto si reiniciamos la terminal integrada podremos ejecutar cualquier comando con pipenv run tal como vimos (algo que os recomiendo):


#Scripts personalizados

'''
Algo que podemos configurar son alias de ejecución de scripts.

Por ejemplo si queremos ejecutar un determinado comando como pipenv run python hola.py más fácilmente, podemos editar el Pipfile y en un nuevo bloque [scripts] añadir el alias en una línea:

[scripts]
hola = "pipenv run python hola.py"
A partir de este momento podemos ejecutar este comando solo escribiendo en la terminal:

pipenv run hola

Es una funcionalidad especialmente útil con módulos que tienen muchos comandos como Django.
'''