#!/bin/bash
sudo apt-get install python-dev supervisor node -y
sudo pip install flask broadlink --upgrade
sudo cp -f supervisor.conf /etc/supervisord/conf.d/
sudo supervisorctl start flask
sudo npm install -g homebridge homebridge-http
sudo cp homebridge.config.json ~/.homebridge/config.json
