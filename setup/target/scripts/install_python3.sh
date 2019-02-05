#!/bin/bash
set -x

#Ref: https://askubuntu.com/questions/798123/how-do-i-install-python-3-5-2
apt-get update
apt-get install -y python3
#Set python -V command to return python 3.5.2 version using virtual env
#Now, since you have set virtualenv , you can use normal python command instead of python3 command.
#you dont need python virtualenv settings, as docker image itself makes it like a virtual env.The related docker image
#this script has been called from explicitly install python 3 alone. You can have another docker image to install another
#version of python.
#apt-get install python3-venv
#python3 -m venv MYVENV && source MYVENV/bin/activate

#install pip3
apt-get install -y python3-pip
#Upgrade pip3 to latest version
#sudo pip3 install --upgrade pip
#sudo apt-get -y remove python3-apt
#sudo apt-get -y install python3-apt

