#!/bin/bash

sudo cp service_files/gpiobutton.service /etc/systemd/system/
sudo systemctl enable gpiobutton.service
