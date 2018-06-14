#!/bin/bash
sudo bash setup_nodejs_8.sh
sudo apt-get install python-dev supervisor nodejs -y
sudo pip install flask broadlink --upgrade
sed "s|<dir>|`pwd`|" supervisord.conf > irstar.conf
sudo mv -f irstar.conf /etc/supervisord/conf.d/
sudo systemctl enable supervisor
sudo systemctl start supervisor
sudo supervisorctl start flask
# homebridge need these packages
sudo apt-get install libavahi-compat-libdnssd-dev
sudo npm install -g --unsafe-perm homebridge homebridge-http homebridge-http-temperature
mkdir ~/.homebridge
cp homebridge.config.json ~/.homebridge/config.json
sudo cp homebridge.service /etc/systemd/system/
