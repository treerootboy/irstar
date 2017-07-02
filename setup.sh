#!/bin/bash
sudo apt-get install python-dev supervisor -y
sudo pip install flask broadlink --upgrade
sudo cp -f supervisor.conf /etc/supervisord/conf.d/
sudo supervisorctl start flask
