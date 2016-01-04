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

