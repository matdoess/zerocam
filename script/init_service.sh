#!/bin/bash

sudo cp service_files/gpiobutton.service /etc/systemd/system/
sudo systemctl enable gpiobutton.service

sudo cp service_files/django.service /etc/systemd/system/
sudo systemctl enable django.service

sudo cp service_files/picam.service /etc/systemd/system/
