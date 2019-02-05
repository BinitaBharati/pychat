#This is a sample Image 
#docker unbuntu image 
FROM ubuntu:16.04 
MAINTAINER binita.bharati@gmail.com 

RUN mkdir -p /home/vagrant/dockerws/chatServerInstaller/scripts/
RUN mkdir -p /home/vagrant/dockerws/chatServerInstaller/src/
WORKDIR /home/vagrant/dockerws/chatServerInstaller

#Copy all the required files from host's file system to the container file system.
COPY setup/target/scripts/install_django2.sh scripts/
COPY setup/target/scripts/install_chatserver_container.sh scripts/
COPY setup/target/scripts/install_python3.sh scripts/
COPY setup/target/scripts/install_redis.sh scripts/
COPY src/ src/



RUN apt-get update;apt-get -y install dos2unix


RUN dos2unix scripts/install_chatserver_container.sh scripts/install_chatserver_container.sh;chmod +x scripts/install_chatserver_container.sh

ENTRYPOINT ["/home/vagrant/dockerws/chatServerInstaller/scripts/install_chatserver_container.sh"]
