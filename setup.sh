#!/bin/bash
sudo apt-get install python-dev supervisor node -y
sudo pip install flask broadlink --upgrade
sed "s|<dir>|`pwd`|" supervisord.conf > irstar.conf
sudo mv -f irstar.conf /etc/supervisord/conf.d/
sudo systemctl enable supervisor
sudo systemctl start supervisor
sudo supervisorctl start flask
sudo npm install -g homebridge homebridge-http
sudo cp homebridge.config.json ~/.homebridge/config.json
