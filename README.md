# Proyecto InsertaLogo
## Miguel Ángel García Villegas

Proyecto para las asignaturas IV (Infraestructuras Virtuales) y DAI (Diseño de Aplicaciones para Internet).

**Etiqueta Travis**
	[![Build Status](https://travis-ci.org/magvugr/InsertaLogo.svg?branch=master)](https://travis-ci.org/magvugr/InsertaLogo)

**Etiqueta Snap-ci** [![Build Status](https://snap-ci.com/magvugr/InsertaLogo/branch/master/build_image)](https://snap-ci.com/magvugr/InsertaLogo/branch/master)

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

# Hito 2

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
			- python insertaLogo/setup.py install
		test:
			- python insertaLogo/manage.py test insertaLogo/insertaLogo/appInsertaLogo


		run:
			- python insertaLogo/manage.py runserver
		doc:
			- pycco *.py
			- pycco insertaLogo/*.py

## Integración Continua
- [x] [Travis](https://travis-ci.org/) permite testear el código del proyecto. Para llevar a cabo esto hay que adjuntar en el directorio raíz de nuestro proyecto el fichero **.travis.yml**. Mi archivo [.travis.yml](https://github.com/magvugr/InsertaLogo/blob/master/.travis.yml)

El código utilizado para el fichero .travis.yml es el siguiente:

		language: python
		python:
		- "2.7"
		# command to install dependencies
		install:
		- sudo apt-get install python-dev
		- pip install -q Django==1.8.5
		- pip install -q wheel==0.24.0
		- pip install pycco
		# command to run tests
		script:
		- pycco insertaLogo/*.py
		- pycco insertaLogo/appInsertaLogo/*.py
		- make -f Makefile test

		branches:
		- only:
		- master

Desde la web Travis logueándose con GitHub automáticamente se realizarán comprobaciones con los test creados previamente, cada vez que se realice un *push*

## Documentación, **Pycco**
Las directivas para documentar el código del proyecto, están contempladas en el [make](https://github.com/magvugr/InsertaLogo/blob/master/makefile)

## Test

Hemos realizado varios Test para verificar el funcionamiento del proyecto. Para ejecutarlos lo hacemos llamando a ```make test```

- [x] test_usuarios, éste test crea un usuario.

			def test_usuarios(self):
			user = Usuario(nombre = 'nombre',apellidos = 'apellidos',user = 'user',password = 'pass', email = 'email')
			user.save()
			self.assertEqual(user.nombre,'nombre')
			print("Se ha creado usuario, Test = OK")

- [x] test_cambiar_nombre, éste test realiza un cambio de nombre.

		def test_cambiar_nombre(self):
			user = Usuario(nombre = 'nombre',apellidos = 'apellidos',user = 'user',password = 'pass', email = 'email')
			user.save()
			user.nombre='CambioNombre'
			user.save()
			self.assertEqual(user.nombre,'CambioNombre')
			print("Se ha realizado el cambio de nombre, Test = OK")

- [x] test_cambiar_email, éste test realiza un cambio de email.

		def test_cambiar_email(self):
			user = Usuario(nombre = 'nombre',apellidos = 'apellidos',user = 'user',password = 'pass', email = 'email')
			user.save()
			user.email='CambioEmail'
			user.save()
			self.assertEqual(user.email,'CambioEmail')
			print("Se ha realizado el cambio de email, Test = OK")

- [x] test_form_usuarios, éste test valida un formulario usuario.

		def test_form_usuarios(self):
			data_form = {'nombre' : 'nombre','apellidos' : 'apellidos','user' : 'user', 'password': 'pass', 'email':'email'}
			form = crea_usuario(data = data_form)
			self.assertTrue(form.is_valid())
			print("Formulario Usuario, Test = OK")

El resultado de nuestro proyecto en Travis es el siguiente:

![Travis](https://www.dropbox.com/s/qrmflob8zsyq1e3/travis.png?dl=1)
