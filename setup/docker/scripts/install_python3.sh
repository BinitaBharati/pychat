#!/bin/bash
set -x

#Ref: https://askubuntu.com/questions/798123/how-do-i-install-python-3-5-2
#Python 3.5.2 is already installed in Ubuntu Xenial.
#Just set python -V command to return python 3.5.2 version using virtual env
#Now, since you have set virtualenv , you can use normal python command instead of python3 command.
sudo apt-get install python3-venv
python3 -m venv MYVENV && source MYVENV/bin/activate

#install pip3
sudo apt-get install -y python3-pip
#Upgrade pip3 to latest version
#sudo pip3 install --upgrade pip
#sudo apt-get -y remove python3-apt
#sudo apt-get -y install python3-apt

