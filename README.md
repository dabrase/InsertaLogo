# Proyecto InsertaLogo
## Miguel Ángel García Villegas

Proyecto para las asignaturas IV (Infraestructuras Virtuales) y DAI (Diseño de Aplicaciones para Internet).

**Etiqueta Travis**
[![Build Status](https://travis-ci.org/magvugr/InsertaLogo.svg?branch=master)](https://travis-ci.org/magvugr/InsertaLogo)

**Etiqueta Shippable**
[![Shippable](https://img.shields.io/shippable/54d119db5ab6cc13528ab183.svg)](https://app.shippable.com/projects/563cd39c1895ca447422c9bd)

**Etiqueta Snap-ci** [![Build Status](https://snap-ci.com/magvugr/InsertaLogo/branch/master/build_image)](https://snap-ci.com/magvugr/InsertaLogo/branch/master)

[![Heroku](https://www.herokucdn.com/deploy/button.png)]()

## Descripción

Consiste en la que usuarios pueden poner su sello o logo, en sus fotos de una manera rápida y sencilla.

## Más info y detalles
- [x]  Registro: Un usuario se registra en la aplicación, a través de usuario y contraseña.
- [x]  Añadir Logos Vinculados a un Usuario en concreto: Una Vez registrado y logeado añade el logo o logos con los que habitualmente trabaja.
- [x]  Selección de Foto y/o Fotos: Se seleccionará la foto o fotos donde quieres añadir el logo desde su pc.
- [x]  Indicar logo a insertar: Seguidamente de la selección de foto o fotos, deberá seleccionar el logo vinculado a su registro que desea incorporar en la foto, la posición donde quiere situarlo y la resolución de la foto.
- [x]  Exportación de foto final: Finalmente la foto se exportará con las características previamente seleccionadas con el logo incorporado.

## Infraestructura Virtual
- [x]  Servidor de Base de Datos para la gestión de usuarios.
- [x]  Servidor de Base de Datos para el contenido de la Web.
- [x]  Servidor Web.

## Trabajaremos:

- [x]  Framework Django.
- [x]  Usuarios y Logos, Base de Datos Gestionada con MySqL

## Herramientas de construcción

- [x]  Manage.py
- [x]  Makefile

## Automatización, **Make**
He realizado un archivo [make](https://github.com/magvugr/InsertaLogo/blob/master/Makefile) para automatizar el proceso.

El código de mi Makefile es el siguiente:

		#Miguel Angel Garcia Villegas

		clean:
		- rm -rf *~*
		- find . -name '*.pyc' -exec rm {} \;
		install:
		- python setup.py install
		test:
		- python manage.py test

		run:
		- python manage.py runserver
		doc:
		- pycco *.py

		heroku:
		- wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh   
		- heroku login
		- heroku create
		- git add .
		- git commit -m "Subir a Heroku"
		- git push heroku master
		- heroku ps:scale web=1
		- heroku open


Algunas de las diferentes opciones del Makefile (que se irán añadiendo más):

- Limpieza (make clean)

- Realizar Tests (make test)

- Ejecutar servidor (make run)

## Test, Sistema de Pruebas.

Hemos realizado varios Test para verificar el funcionamiento del proyecto. Para ejecutarlos lo hacemos llamando a ```make test```

- [x] test_registros, éste test crea un registro.

		def test_registros(self):
		reg = Registro(email = 'email', nombre = 'nombre',apellidos = 'apellidos')
		reg.save()
		self.assertEqual(reg.nombre,'nombre')
		print("Se ha creado usuario, Test = OK")

- [x] test_cambiar_nombre, éste test realiza un cambio de nombre.

		def test_cambiar_nombre(self):
		reg = Registro(email = 'email', nombre = 'nombre',apellidos = 'apellidos')
		reg.save()
		reg.nombre='CambioNombre'
		reg.save()
		self.assertEqual(reg.nombre,'CambioNombre')
		print("Se ha realizado el cambio de nombre, Test = OK")

- [x] test_cambiar_email, éste test realiza un cambio de email.

		def test_cambiar_email(self):
		reg = Registro(email = 'email', nombre = 'nombre',apellidos = 'apellidos')
		reg.save()
		reg.email='CambioEmail'
		reg.save()
		self.assertEqual(reg.email,'CambioEmail')
		print("Se ha realizado el cambio de email, Test = OK")

## Integración Continua

Sistema de integración continua comprueba de forma continua que cada cambio realizado al repositorio, siga funcionando correctamente.

**Etiqueta Travis**
[![Build Status](https://travis-ci.org/magvugr/InsertaLogo.svg?branch=master)](https://travis-ci.org/magvugr/InsertaLogo)

**Etiqueta Shippable**
[![Shippable](https://img.shields.io/shippable/54d119db5ab6cc13528ab183.svg)](https://app.shippable.com/projects/563cd39c1895ca447422c9bd)

**Etiqueta Snap-ci** [![Build Status](https://snap-ci.com/magvugr/InsertaLogo/branch/master/build_image)](https://snap-ci.com/magvugr/InsertaLogo/branch/master)

- [x] [Travis](https://travis-ci.org/) permite testear el código del proyecto. Para llevar a cabo esto hay que adjuntar en el directorio raíz de nuestro proyecto el fichero **.travis.yml**. Mi archivo [.travis.yml](https://github.com/magvugr/InsertaLogo/blob/master/.travis.yml)

El código utilizado para el fichero .travis.yml es el siguiente:

		language: python
		python:
		 - "2.7"
		# command to install dependencies
		install:
		 - sudo apt-get install python-dev
		 - pip install -q Django==1.8
		 - pip install -q wheel==0.24.0
		 - pip install pycco
		# command to run tests
		script:
		 - make -f Makefile test

		branches:
		  - only:
		    - master


- [x] [Shippable](https://app.shippable.com/) permite testear el código del proyecto. Para llevar a cabo esto hay que adjuntar en el directorio raíz de nuestro proyecto el fichero **shippable.yml**. Mi archivo [shippable.yml](https://github.com/magvugr/InsertaLogo/blob/master/shippable.yml)

Desde la web Travis, Shippable o Snap-ci logueándose con GitHub automáticamente se realizarán comprobaciones con los test creados previamente, cada vez que se realice un *push*

El resultado de nuestro proyecto en Travis es el siguiente:

![Travis](https://www.dropbox.com/s/qrmflob8zsyq1e3/travis.png?dl=1)

## Documentación, **Pycco**
Las directivas para documentar el código del proyecto, están contempladas en el [make](https://github.com/magvugr/InsertaLogo/blob/master/Makefile)

## Despliegue en Heroku (PaaS):

Esta es la aplicación ya desplegada en Heroku: [Aplicación InsertaLogo en Heroku]()

Para llevar a cabo el despliegue en Heroku, hay que añadir el fichero ***Procfile*** y el fichero ***requirements.txt***

- Mi fichero [Procfile](https://github.com/magvugr/InsertaLogo/blob/master/Procfile) que sirve para ejecutar el comando en el servidor de heroku. Éste archivo no debe tener extensión y debe estar colocado en el directorio raíz de su aplicación.
Para que nuestra aplicación se ejecute debemos de definir nuestros [dynos](https://devcenter.heroku.com/articles/dynos). Un dyno no es más que un contenedor que ejecuta el comando que le especificamos.

- Mi archivo [requirements.txt](https://github.com/magvugr/InsertaLogo/blob/master/requirements.txt) que sirve para que Heroku reconozca una aplicación Python y para que conozca sus dependencias. Éste archivo tiene que terner formato txt y debe estar colocado en el directorio raíz del repositorio. Éste fichero se puede generar ejecutando en el terminal ***pip freeze > requirements.txt***
