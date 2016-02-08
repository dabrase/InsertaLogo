#Instalar plugin azure vagrant plugin install vagrant-azure

Vagrant.configure('2') do |config|
    config.vm.box = 'azure'
    config.vm.network "forwarded_port", guest: 80, host: 80
    config.vm.provider :azure do |azure, override|
        # Mandatory Settings
        azure.mgmt_certificate = File.expand_path(ENV['CERTIFICADOM'])
        azure.mgmt_endpoint    = 'https://management.core.windows.net'
        azure.subscription_id = ENV['SUBCRIP']
        azure.vm_name     = ENV['MAQSER']
        azure.vm_image    = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
        azure.vm_size     = 'Small'
        config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
        azure.cloud_service_name = ENV['MAQSER']

	# Optional Settings
        azure.vm_user = ENV['USERN'] # defaults to 'vagrant' if not provided
        azure.vm_password = ENV['PASSW']
        azure.vm_location = 'North Europe' # e.g., West US
        azure.ssh_port             = '22'
        azure.tcp_endpoints = '80:80'
      end
      config.ssh.username = ENV['USERNSSH']
      config.ssh.password = ENV['PASSWSSH']
      config.vm.synced_folder ".", "/vagrant",disabled:true #Evitar subir la copia local

# Instalacion ansible sudo pip install ansible
#Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.raw_arguments = ["-vvvv"] #Depurando errores
    ansible.force_remote_user = false
    ansible.playbook = "ansible/webservice.yml"
    #ansible.playbook = ".vagrant/provisioners/ansible/inventory/webservice.yml"
  end
end
