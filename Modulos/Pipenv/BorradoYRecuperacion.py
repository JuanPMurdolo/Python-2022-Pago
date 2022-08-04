#Borrado y recuperación

#Si en algún momento necesitamos borrar el entorno virtual del disco duro podemos utilizar la instrucción:
#pipenv --rm

#En este momento hemos liberado el espacio, 
# pero la configuración del entorno virtual sigue definida en los pipfiles, 
# mientras los tengamos podemos reinstalar el entorno fácilmente ejecutando: #> pipenv install
#Esto instalará todas las dependencias excepto las de desarrollo:
#> pipenv install

#Si queremos incluir las dependencias de desarrollo debemos instalar con:
#> pipenv install --dev

#Mientras la versión del Python nativo concuerde con la del Pipfile todo funcionará sin problemas, en caso de no tener 
# la misma versión recordad que podéis editarla manualmente pero tened presente que alguna dependencia podría ser exclusiva de la versión establecida en el Pipfile.


#Uso de requirements.txt
#Si somos más tradicionalistas, podemos manejar el entorno con el típico fichero requirements.txt.
#Podemos generarlo haciendo: > pipenv requirements > requirements.txt

#Con esto ya tendremos el fichero requirements.txt generado en el directorio del proyecto, sin embargo, Faltan las dependencias de desarrollo como pandas, si queremos incluirlas debemos indicarlo explícitamente:
#pipenv requirements --dev

#De hecho es mejor práctica incluirlas en un dev-requirements.txt por separado, lo cuál podemos hacer mediante: > pipenv requirements --dev-only > dev-requirements.txt

#Ahora si borramos el entorno: > pipenv --rm
# También podemos reinstalarlo tomando como origen el fichero requirements.txt: pipenv install -r requirements.txt
#Y si queremos instalar las dependencias de desarrollo: > pipenv install -r dev-requirements.txt
