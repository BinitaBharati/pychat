#!/bin/bash
set -x

echo "install-chatserver-container.sh : your env are hostIp=$hostIp"

apt-get install -y tzdata

dos2unix scripts/install_python3.sh scripts/install_python3.sh
chmod +x scripts/install_python3.sh
scripts/install_python3.sh

dos2unix scripts/install_django2.sh scripts/install_django2.sh
chmod +x scripts/install_django2.sh
scripts/install_django2.sh

dos2unix scripts/install_redis.sh scripts/install_redis.sh
chmod +x scripts/install_redis.sh
scripts/install_redis.sh

sed "s/^ALLOWED_HOSTS/ALLOWED_HOSTS = ['$hostIp']/g" src/chatproject/chatproject/settings.py
#Not calling makemigrations as the migrations files are already present under loginmodule/migrations
#python3 src/chatproject/manage.py makemigrations loginmodule
python3 src/chatproject/manage.py migrate loginmodule
python3 src/chatproject/manage.py runserver $hostIp:8000

#Run migrations to populate basic user related data. This same thing should be automated for the admin user later.


while true
do
	echo "Press [CTRL+C] to stop.."
	sleep 1
done




