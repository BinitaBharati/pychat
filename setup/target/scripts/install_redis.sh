#!/bin/bash

#Ref for ubuntu/xenial: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04

editConfigFiles() {
cp $1 $1.orig
sed -i "/${2}/c\\${3}" $1
}

apt-get update
Shell

apt-get install -y curl
apt-get install -y build-essential tcl
cd /tmp;curl -O http://download.redis.io/redis-stable.tar.gz
tar xzvf redis-stable.tar.gz
cd redis-stable;make;make install
mkdir /etc/redis
cp /tmp/redis-stable/redis.conf /etc/redis
editConfigFiles 'dir ./' 'dir /var/lib/redis'

#start redis
/usr/local/bin/redis-server /etc/redis/redis.conf &
