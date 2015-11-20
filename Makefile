#Miguel Angel Garcia Villegas

clean:
	- rm -rf *~*
	- find . -name '*.pyc' -exec rm {} \;
install:
	- python insertaLogo/setup.py install
test:
	- python insertaLogo/manage.py test insertaLogo/appInsertaLogo
 

run:
	- python insertaLogo/manage.py runserver
doc:
	- pycco *.py
	- pycco insertaLogo/*.py
	
