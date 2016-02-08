# Proyecto InsertaLogo
## Miguel Ángel García Villegas

Proyecto para las asignaturas IV (Infraestructuras Virtuales) y DAI (Diseño de Aplicaciones para Internet).

**Etiqueta Travis**
[![Build Status](https://travis-ci.org/magvugr/InsertaLogo.svg?branch=master)](https://travis-ci.org/magvugr/InsertaLogo)

**Etiqueta Shippable**
[![Shippable](https://img.shields.io/shippable/54d119db5ab6cc13528ab183.svg)](https://app.shippable.com/projects/563cd39c1895ca447422c9bd)

**Etiqueta Snap-ci** [![Build Status](https://snap-ci.com/magvugr/InsertaLogo/branch/master/build_image)](https://snap-ci.com/magvugr/InsertaLogo/branch/master)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](https://insertalogo.herokuapp.com/)

[<img src="http://azuredeploy.net/deploybutton.png" alt="Azure" height=32>](http://insertalogo.cloudapp.net/)

**Docker Hub** [![Docker](https://www.dropbox.com/s/pv4t7wlh8cztcin/docker-logo_w_195.png?dl=1)](https://hub.docker.com/r/magvugr/insertalogo/)

**Fabric**
[![Fabric](https://www.dropbox.com/s/8gmnun9iy72o2f4/logo.png?dl=1)](https://github.com/magvugr/InsertaLogo/blob/master/fabfile.py)

**Azure**
![Azure](https://www.dropbox.com/s/uaqywmogorsfc89/microsoft-azure-cloud-2.0%20%281%29.jpg?dl=1)

**Vagrant**
[![Vagrant](https://www.dropbox.com/s/k9rxzzsghouo8cu/vagrant-logo.png?dl=1)](https://github.com/magvugr/InsertaLogo/blob/master/Vagrantfile)

**Ansible**
[![Ansible](https://www.dropbox.com/s/iczkyl2xg35wr7o/ansible-logo.jpg?dl=1)](https://github.com/magvugr/InsertaLogo/blob/master/ansible/webservice.yml)

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

		#Makefile

		despliegue:
			chmod a+x variables.sh
			. ./variables.sh

			chmod a+x despliegue5.sh
			./despliegue5.sh pass=$PASSW user=$USERN nomMaq=$MAQSER

		installa:
			sudo pip install -r requirements.txt

		clean:
			rm -rf *~* && find . -name '*.pyc' -exec rm {} \;

		install:
			sudo apt-get update
			sudo apt-get install -y libmysqlclient-dev
			sudo apt-get install -y python-dev
			sudo apt-get install -y libjpeg8-dev
			sudo apt-get install -y libtiff4-dev
			sudo apt-get install -y zlib1g-dev
			sudo apt-get install -y libfreetype6-dev
			sudo apt-get install -y liblcms1-dev
			sudo apt-get install -y libwebp-dev
			sudo apt-get install -y python-pip
			sudo pip install --upgrade -y pip
			sudo pip install -r requirements.txt

		test:
			export DJANGO_SETTINGS_MODULE=InsertaLogo.settings && nosetests

		run:
			- python manage.py runserver
		doc:
			- pycco *.py

		heroku:
			wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
			heroku login
			heroku create
			git add .
			git commit -m "Despliegue heroku"
			git push heroku master
			heroku ps:scale web=1
			heroku open

		docker:
			sudo apt-get update
			sudo apt-get install -y docker.io
			sudo docker pull magvugr/insertalogo
			sudo docker run -p 8000:8000 -t -i magvugr/insertalogo /bin/bash




Algunas de las diferentes opciones del Makefile (que se irán añadiendo más):

- Limpieza (make clean)

- Realizar Tests (make test)

- Ejecutar servidor (make run)

## Test, Sistema de Pruebas.

Hemos realizado varios Test para verificar el funcionamiento del proyecto. Para ejecutarlos lo hacemos llamando a ``make test``

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

Esta es la aplicación ya desplegada en Heroku: [Aplicación InsertaLogo en Heroku](https://insertalogo.herokuapp.com/)

Para llevar a cabo el despliegue en Heroku, hay que añadir el fichero ***Procfile*** y el fichero ***requirements.txt***

- Mi fichero [Procfile](https://github.com/magvugr/InsertaLogo/blob/master/Procfile) que sirve para ejecutar el comando en el servidor de heroku. Éste archivo no debe tener extensión y debe estar colocado en el directorio raíz de su aplicación.
Para que nuestra aplicación se ejecute debemos de definir nuestros [dynos](https://devcenter.heroku.com/articles/dynos). Un dyno no es más que un contenedor que ejecuta el comando que le especificamos.

- Mi archivo [requirements.txt](https://github.com/magvugr/InsertaLogo/blob/master/requirements.txt) que sirve para que Heroku reconozca una aplicación Python y para que conozca sus dependencias. Éste archivo tiene que terner formato txt y debe estar colocado en el directorio raíz del repositorio. Éste fichero se puede generar ejecutando en el terminal ***pip freeze > requirements.txt***

## Docker:

Docker es un proyecto de código abierto con el que fácilmente podremos crear "contenedores". Estos contenedores de Docker podríamos definirlos como máquinas virtuales ligeras, menos exigentes con los chips y memorias de los equipos donde se ejecutarán.


Para crear la imagen, Docker usa un fichero dentro del código de la aplicación llamado [Dockerfile](https://github.com/magvugr/InsertaLogo/blob/master/Dockerfile) para la construcción de la imagen.

En la web de [Docker Hub](https://hub.docker.com/) una vez logueados, creamos un "Automated Build" sobre el repositorio de nuestro proyecto, lo cual comenzará a crear la imagen.

Mi repositorio Docker Automated Build es https://hub.docker.com/r/magvugr/insertalogo/

Ahora todos los cambios se integran en tiempo real y de forma automatizada mediante Docker Hub cada vez que hagamos un ```git push```.

Para ejecutarlo de forma local, hay que ejecutar en el terminal ```make docker```

Instala Docker, descarga el contenedor con la aplicación instalada en él, y arranca el entorno de pruebas.

Para ver que la aplicación de verdad está funcionando crea servidor web localmente y hay que introducir la url en el navegador para acceder a la aplicación.

## Acceso Remoto y Automatización con Fabric

[Fabric](http://www.fabfile.org/) es una librería para Python y línea de comandos para coordinar el uso de SSH para implementación de aplicaciones o tareas de administración de sistemas.

Para instalar Fabric, ***apt-get install fabric***

Para comenzar a realizar nuestras tareas, debemos crear un archivo llamado [fabfile.py](https://github.com/magvugr/InsertaLogo/blob/master/fabfile.py).

En ese archivo definirán todas las tareas que deseen realizar.
Para ejecutar esa tarea utilizamos el comando fab, especificando en qué host vamos a trabajar.

Fabric, utiliza SSH para realizar las tareas, ya sea en local o en remoto. Para no tener que colocar la contraseña cada vez que ejecutemos la tarea, podemos definir el usuario y la contraseña con la que deseamos conectarnos al SSH.

## Azure
[Microsoft Azure] (https://azure.microsoft.com/es-es/) es una plataforma ofrecida como servicio y alojada en los Data Centers de Microsoft.


## Vagrant

[Vagrant](https://www.vagrantup.com/) es una herramienta de software libre, multiplataforma, para la creación y configuración de entornos de desarrollo virtualizados ligeros, reproducibles y portables. De este modo, podremos automatizar la creación y gestión de máquinas virtuales.

## Ansible

[Ansible](http://www.ansible.com/) es una herramienta open-source desarrollada en python y comercialmente ofrecida por AnsibleWorks que la definen como un motor de orquestación muy simple que automatiza las tareas necesarias en el campo de las TI.

## Azure + Vagrant + Ansible + Fabric

Para llevar a cabo nuestra app ***InsertaLogo*** hemos tenido que:
- [x] Crear una cuenta en [Dreamspark](https://www.dreamspark.com/) una vez verifiquemos nuestra inscripción académica ya podemos hospedar aplicaciones web en [Azure](https://azure.microsoft.com/es-es/).

- [x] Entramos en [Windows Azure](manage.windowsazure.com) y configuramos las subcripciones.

- [x] Ahora para desplegar máquinas en Azure, vamos a utilizar Vagrant y Ansible.

- [x] Nuestro fichero [Vagrantfile](https://github.com/magvugr/InsertaLogo/blob/master/Vagrantfile), encargado de crear la máquina y su gestión de usuarios.

- [x] Nuestro fichero [Ansible](https://github.com/magvugr/InsertaLogo/blob/master/ansible/webservice.yml), encargado de instalar las dependencias necesarias.

- [x] A continuación generamos nuestro certificado ***.cer*** y lo subimos al servidor Azure.

- [x] Nuestro fichero [Fabric](https://github.com/magvugr/InsertaLogo/blob/master/fabfile.py) encargado de conectarse a la máquina por nosotros, además de automatizar las diferentes tareas que podemos indicar en el archivo ***Fabfile***.

- [x] Por seguridad hemos creado una [plantilla de variables de entorno](https://github.com/magvugr/InsertaLogo/blob/master/PlantillaVariables.sh) donde se indicarán datos privados de forma segura. En dicho archivo le indicamos nuestros datos, y lo guardamos con el nombre ***variables.sh***

- [x] Una vez hayamos los realizados los pasos anteriores, ejecutamos en el terminal ***make despliegue***, que seguidamente comenzará con el despliegue de nuestra app en azure.

Aquí dejo un pantallazo de la app, funcionando. Aunque se puede consultar en el siguiente enlace ->  http://insertalogo.cloudapp.net/

 ![InsertaLogoCLoudapp](https://www.dropbox.com/s/bwv08eanwoxd1se/InsertaLogoCloudapp.png?dl=1)
