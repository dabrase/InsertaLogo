from fabric.api import task, run, local, hosts, cd, env

def informacion_sistema():
    run('uname -a')

########   Docker y descargar imagen Inserta Logo
def getdocker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull magvugr/insertalogo')

########   Ejecutamos Docker
def rundocker():
	run('sudo docker run -i -t magvugr/insertalogo')

########   Clonamos repositorio
def getapp():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
	run('sudo git clone https://github.com/magvugr/InsertaLogo.git')

########   Install del make
def install():
	run('cd InsertaLogo && make install')

########   Test
def test():
	run('cd InsertaLogo && make test')

########   Ejecucion app
def run_app():
	run('cd InsertaLogo && sudo python manage.py runserver 0.0.0.0:80')

def run_app_2():
    run('cd InsertaLogo && sudo gunicorn -b 0.0.0.0:80 InsertaLogo.wsgi --log-file - &')

########   Borrar
def remove():
    run('sudo rm -r InsertaLogo')
