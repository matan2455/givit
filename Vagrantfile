Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.network "forwarded_port", guest: 5000, host: 8000
  config.vm.provider "virtualbox" do |v|
    v.name = "GIVIT"
  end
end
