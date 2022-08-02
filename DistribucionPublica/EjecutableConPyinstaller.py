#Reducir el tamaño de un ejecutable

#pipenv corre un entorno virtual de python limpio sin  dependencias
#pip install pipenv

#pip list para ver que esta instalado en el sistema

#pipenv install pyinstaller

#Crea un ambierte virtual y le instala pyinstaller

#pipenv run pyinstaller programa.py

#El directorio dist que contiene las dependencias termina pesando mucho menos

#pipenv run /*se puede correr todo como si fuera python*/

#Se puede crear un .py con tkinter basico 

#Se usa 
#pipenv run pyinstaller program.py --windowed --onefile --clean

#Si tuviera una foto o alguna dependencia
#primero se crea la carpeta res o resources donde van a ir todos
#se utiliza el metodo resource_path
'''
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
'''
#Se importan sys y os
#pipenv run pyinstaller program.py --windowed --onefile --clean --add-data res:res /*o resources*/
#despues del : de res es con el nombre con el que se va a compilar

