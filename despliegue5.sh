#! /bin/bash

#Despliegue Azure, Vagrant, Ansible y Fabric
sudo apt-get install -y vagrant
sudo apt-get install -y ansible
sudo apt-get install -y fabric
vagrant plugin install vagrant-azure
vagrant up --provider=azure
fab -p $1 -H $2@$3.cloudapp.net run_app_2
