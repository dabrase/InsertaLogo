# Sistema operativo
FROM ubuntu:latest

# Autor
MAINTAINER Miguel Angel Garcia Villegas <magvugr@gmail.com>

# Instalacion 
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get update
RUN sudo apt-get install -y git
RUN sudo apt-get install -y build-essential

# Descarga repositorio de la app
RUN sudo git clone https://github.com/magvugr/InsertaLogo

# Instalacion de la app y sus dependencias
RUN cd InsertaLogo && git pull
RUN cd InsertaLogo && make install


