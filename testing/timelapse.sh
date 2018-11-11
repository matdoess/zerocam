#!/bin/bash

raspistill -n -t 43200000 -tl 10000 -o img/timelapse2/image%04d.jpg -w 1280 -h 960
