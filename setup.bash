#!/bin/bash
apt update -y
apt install python3 apache2 -y
wget https://raw.githubusercontent.com/PrasanthVR63/cloudcomputingprash/0878a890fc8c3c239c6216889328950611b3d4a2/apache2.conf -O /etc/apache2/apache2.conf
apache2ctl restart
wget https://raw.githubusercontent.com/PrasanthVR63/cloudcomputingprash/main/simpleprint.py -P /var/www/html/
chmod 755 /var/www/html/simpleprint.py
