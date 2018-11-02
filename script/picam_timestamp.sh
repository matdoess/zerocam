#!/bin/bash

#https://github.com/iizukanao/picam#overlaying-text-subtitle

# Write Timestamp in Subtitle File
while true
do
time=`date '+%H:%M:%S'`
date=`date '+%Y-%m-%d'`


cat > /home/pi/picam/hooks/subtitle <<EOF
text=$date\n$time
font_name=FreeSans
pt=20
layout_align=top,right
horizontal_margin=30
vertical_margin=30
text_align=right
color=ffffff
stroke_width=1
duration=0
EOF

sleep 1
done

# color: 000000 black / ffffff white
