#!/bin/bash

raspistill -n -t 43200000 -tl 1000 -o img/timelapse3/image%04d.jpg -w 1280 -h 960
