#!/bin/bash

# Become the homeassistant user
#sudo su -s /bin/bash homeassistant;

# Setup Virtual-env
#source /srv/homeassistant/bin/activate;


# Upgrade
#sudo -H -u homeassistant /bin/bash -c 'source /srv/homeassistant/bin/activate && pip3 install --upgrade homeassistant';
sudo pip3 install --upgrade homeassistant;

# Restart service
sudo systemctl restart home-assistant@homeassistant.service 

# Done
exit
