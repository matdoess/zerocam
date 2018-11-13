# zerocam
Python based interface for the pi zero w for timelapse videos and live streaming

## Used Hardware
- [Raspberry Pi Zero W](https://www.exp-tech.de/plattformen/raspberry-pi/8268/raspberry-pi-zero-w)
- [Offizielles Raspberry Pi Zero Gehäuse
](https://www.exp-tech.de/zubehoer/gehaeuse/8860/raspberry-pi-zero-gehaeuse)
- [Raspberry Pi Kameramodul v2
](https://www.exp-tech.de/plattformen/raspberry-pi/7165/raspberry-pi-kameramodul-v2)
- [Adafruit I2S MEMS Mikrofon-Breakout - SPH0645LM4H
](https://www.exp-tech.de/module/audio/8016/adafruit-i2s-mems-mikrofon-breakout-sph0645lm4h)
- [Tactile Button switch (6mm) x 20 pack
](https://www.exp-tech.de/zubehoer/tasterschalter/6974/tactile-button-switch-6mm-x-20-pack)

## System Info
### User & Password
* Linux - pi:raspberry
* Django - 
### Access Point
* SSID: `zerocamap`
* Password: `zerocampw`
* static ip: `192.168.4.1`
* dhcp-range: `192.168.4.2 - 192.168.4.20`
### URL's
* hostname
  * zerocam
  * zerocam.local
* livestream
  * Django: http://zerocam.local:8000/static/video/index.m3u8
  * nginx: http://zerocam.local/hls/index.m3u8
  * node-rtsp-rtmp-server: <rtmp://zerocam.local/live/picam>
* webinterface
  * Django Landing Page: http://zerocam.local:8000/video/
### .service files
`picam.service` | start picam streaming  
`django.service` | Django Webinterface  
`gpiobutton.service` | listen for button press and shutdown pi or activate access point  
`picam-ramdisk.service` | create ramdisk folder on startup  

## folders
- `testing`: code snippets and testing of modules
- `script`: mainly setup and startup scripts
- `media`: folder for videos, images, timelapse, etc.

## Setup
### Basic Raspberry Setup
- Set shared Memory to 256mb  
  Needed for picamera pictures with highest resolution

### ffmpeg installation (with hardware acceleration)
https://github.com/legotheboss/YouTube-files/wiki/(RPi)-Compile-FFmpeg-with-the-OpenMAX-H.264-GPU-acceleration
https://www.reddit.com/r/raspberry_pi/comments/5677qw/hardware_accelerated_x264_encoding_with_ffmpeg/
https://askubuntu.com/questions/87111/if-i-build-a-package-from-source-how-can-i-uninstall-or-remove-completely

Delete previous version of ffmpeg: `sudo apt-get remove ffmpeg`

Install checkinstall: `sudo apt-get install checkinstall`

Download and Compile ffmpeg with Hardware Acceleration on Raspberry Pi:
```
cd /home/pi/
sudo apt-get install libomxil-bellagio-dev -y
git clone https://github.com/FFmpeg/FFmpeg.git
cd FFmpeg
sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-omx --enable-omx-rpi --enable-nonfree
sudo make
sudo checkinstall
```
 
 You can remove it from your system anytime using:  
 `dpkg -r ffmpeg`


# Programming
## TODO
- [ ] Django Webinterface
- [ ] HotSpot
  - [x] Aktiviern über Button
  - [x] Script um zwischen AP und Wifi zu wechseln
  - [ ] Change /etc/hosts with script (add 192.168.4.1 and comment out 127.0.1.1)
- [ ] WiFi
  - [x] aktivieren über Webinterface
- [ ] Stop-Motion Push-Button (in webinterface)
  - https://projects.raspberrypi.org/en/projects/push-button-stop-motion
- [ ] Timelaps Videos

## Python
1. pip3 install --user pipenv (required)

## Django
### Setup Project(for Documentation only)
1. pipenv install
2. Projekt erstellen django-admin startproject zerocam_ui
3. In zerocam_ui Ordner wechseln
4. pipenv shell
5. Django App erstellen python manage.py startapp wifi_setup
6. Anleitung befolgen https://docs.djangoproject.com/en/2.1/intro/tutorial01/
7. Admin User erstellen python manage.py createsuperuser

### Run Application
1. cd zerocam/
2. pipenv install
3. pipenv run zerocam_ui/manage.py runserver
4. Enjoy

### Livestream
-- Symlink anlegen damit django die Files ausliefert ln -s /run/shm/hls /home/pi/zerocam/zerocam_ui/wifi_setup/static/video

## Commands for Testing
### picam
picam with hls streaming / framerate 25 / volume gain 10x:  
`/home/pi/picam/picam --alsadev complex_convert -o /run/shm/hls -f 25 --volume 10`  
picam with timestam  
`/home/pi/picam/picam --alsadev complex_convert -o /run/shm/hls -f 25 --volume 10 --time`  
picam with timeformat "2018-12-01 12:30:05"  
`/home/pi/picam/picam --alsadev complex_convert -o /run/shm/hls -f 25 --volume 10 --time --timeformat "%F %T"`

### ffmpeg
Create timelapse from jpg  
`ffmpeg -framerate 10 -pattern_type glob -i '*.jpg' -r 25 timelapse10.mp4`  
Create timelapse with hardware acceleration  
(Change -framerate value to your needs)    
`ffmpeg -framerate 10 -pattern_type glob -i '*.jpg' -c:v h264_omx -b:v 4000k -r 25 timelapse10.mp4`


# Reference
## picamera
https://picamera.readthedocs.io/en/release-1.13/index.html  

## i2s mems mic
https://github.com/mpromonet/v4l2rtspserver/issues/94#issuecomment-378788356  

## Power Button
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi  


# Programming Basics
## Efficency of while loops

* While: pass  
Bad. 100% CPU

* While: time.sleep(1)  
Better. CPU every 1 sec

* While: Event().wait()  
https://stackoverflow.com/a/48631852  
Python 3.2+ / No Windows / No CPU time

* While: GPIO.wait_for_edge  
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi  
when using while loop to wait for gpio
but can't be used with `GPIO.add_event_detect`


