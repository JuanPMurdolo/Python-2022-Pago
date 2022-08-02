#modelo de un setup para packages
#install_requires son todos los import que tiene un package
#Se puede especificar la version con == o >=
#otra forma es sacar todos los imports a un txt para poder manejarlo mejor 
#Asi se maneja en en  la linea que no esta comentada

#Se pueden incluir pruebas unitarias
#Se tiene que generar una carpeta tests que contenga las rutinas con pruebas unitarias

#para poder hacer la distribucion hay que entrar a pypi.org o test.pypi.org(test es un buen comienzo)
from setuptools import setup, find_packages

setup(
    name="Nombre del paquete",
    version="1.0",
    description="Descripcion del paquete",
    long_description=open('README.md').read(),
    author="Yo",
    author_email="email@mail.com",
    url="web",
    license_files=['LICENSE'],
    packages=find_packages(),
    scripts=["test.py"],
#   install_requires=['numpy>=1.23.0']
    test_suite="tests",
    install_requires=[paquete.strip() for paquete in open("requirements.txt").readline()],
    classifiers=['Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python']
)

#una vez terminado esto hay que installar con pip dos paquetes
#pip install build twine
#o
#pip install build twine --upgrade si ya estan instalados
#python3 -m build
#una vez que chequea que este todo terminado 
#python3 -m twine chesck dist/*
#Esto ultimo chequea para ver que no haya errores en el paquete
#Una vez terminado esto si queremos subirlo
#python3 -m twine upload -r testpypi dist/*
#Y pide un login de test.pypi.org
