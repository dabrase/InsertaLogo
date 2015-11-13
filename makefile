#Miguel Angel Garcia Villegas

clean:
	- rm -rf *~*
	- find . -name '*.pyc' -exec rm {} \;
install:
	- python insertaLogo/insertaLogo/setup.py install
test:
	- python insertaLogo/insertaLogo/manage.py test insertaLogo/insertaLogo/appInsertaLogo
 

run:
	- python insertaLogo/insertaLogo/manage.py runserver
doc:
	- pycco *.py
	- pycco insertaLogo/*.py
	- pycco insertaLogo/insertaLogo/*.py
	
