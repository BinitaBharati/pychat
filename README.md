# pychat

This chat server project makes use of Django channels which is an implenmentation of  web sockets.

## Installation
This project comes with a Docker image. This image will install the entire set up including Python3, Django 2 and any other dependencies.
This image also configures the code and starts the required services within the Docker container.

A sample VM that can be spawned with Vagrant is also provided. This VM has a Ubuntu Xenial image; the Docker package gets installed as part of this VM. 

### Steps
1. To install the base VM, on which Docker container will be run :
```
cd pychat/
vagrant up
```
2. If the base VM with Docker is already installed, we need to copy a particular directory structure into the host VM. The same will already be done, if the base VM is installed with the provided Vagrant file.

Under `/vagrant` directory of host VM, the following directory structure needs to be present:

```

├── setup
│   ├── docker
│   │   ├── Dockerfile
│   │
│   ├── target
│   │   └── scripts
│   │       ├── install_chatserver_container.sh
│   │       ├── install_chatserver_main.sh
│   │       ├── install_django2.sh
│   │       ├── install_python3.sh
│   │       ├── install_redis.sh
│   │       ├── install_vm.sh
│   │       └── start_pyserver.sh
│   └
├── src
│   └── chatproject
│       
```

3.To build the Docker image and run the code:
```
cd /vagrant
dos2unix setup/target/scripts/install_chatserver_main.sh  setup/target/scripts/install_chatserver_main.sh
chmod +x setup/target/scripts/install_chatserver_main.sh
setup/target/scripts/install_chatserver_main.sh
```
