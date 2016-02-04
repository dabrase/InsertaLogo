from fabric.api import run, local, hosts, cd

#infomacion del host
def host_info():
    run('uname -s')

#descarga de la aplicacion utilizando git
def get_app():
	run('sudo apt-get update')
	run('sudo apt-get install -y git')
	run('sudo git clone https://github.com/magvugr/InsertaLogo.git')

#Instalacion necesaria para host virgen
def install():
	run('cd InsertaLogo && make install')

def remove():
    run('sudo rm -r InsertaLogo')


#Ejecucion de test
def test_app():
	run('cd InsertaLogo && make test')

#Ejecucion de la aplicacion
def run_app():
	run('cd InsertaLogo/InsertaLogo && python __main__.py')

#Peticion
def peticion():
	run('curl http://localhost:80/')



#Ejecucion remota del docker
#Instalacion de docker y descarga de imagen
def get_docker():
	run('sudo apt-get update')
	run('sudo apt-get install -y docker.io')
	run('sudo docker pull magvugr/insertalogo')

#Ejecucion de docker
def run_docker():
	run('sudo docker run -i -t magvugr/insertalogo')