#!/bin/bash

sudo cp service_files/gpiobutton.service /etc/systemd/system/
sudo systemctl enable gpiobutton.service

sudo cp service_files/django.service /etc/systemd/system/
sudo systemctl enable django.service

sudo cp service_files/picam.service /etc/systemd/system/

sudo cp service_files/picam-ramdisk.service /etc/systemd/system/
sudo systemctl enable picam-ramdisk.service

#not used anymore due to picam time option
#sudo cp service_files/picam-timestamp.service /etc/systemd/system/

#TODO: run only when option is missing
sudo tee -a /etc/systemd/logind.conf > /dev/null << EOF
RemoveIPC=no
EOF
