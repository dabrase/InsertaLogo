# Sistema operativo
FROM ubuntu:latest

# Autor
MAINTAINER Miguel Angel Garcia Villegas <magvugr@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get -y update

#Descargar aplicacion
RUN sudo apt-get install -y git
RUN sudo git clone https://github.com/magvugr/InsertaLogo

# Instalacion 
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip


# Instalacion de la app y sus dependencias
RUN cd InsertaLogo/ && sudo pip install -r requirements.txt

#RUN cd InsertaLogo && git pull
#RUN cd InsertaLogo && make install

#Migraciones
RUN cd InsertaLogo/ && python manage.py syncdb --noinput


