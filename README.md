# zerocam
Python based interface for the pi zero w for timelapse videos and live streaming

## folders
- testing: code snippets and testing of modules

## TODO
- Django Webinterface
- HotSpot
-- Aktiviern über Button
- WiFi
-- aktivieren über Webinterface

## DONE
- Hotspot
-- Script um zwischen AP und Wifi zu wechseln

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