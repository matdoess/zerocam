# zerocam
Python based interface for the pi zero w for timelapse videos and live streaming

## System Info
### User & Password
* Linux - pi:raspberry
* Django - 
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
- testing: code snippets and testing of modules

## TODO
- [ ] Django Webinterface
- [ ] HotSpot
  - [x] Aktiviern über Button
  - [x] Script um zwischen AP und Wifi zu wechseln
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


