#!/bin/bash

# First Update
sudo apt-get update
sudo apt-get upgrade

## Setup AP
./init_ap.sh

## Setup Python3
./init_python.sh

## Install Service Files
./init_service.sh

## Setup i2s mems microphon
init_i2s-mems-mic.sh
