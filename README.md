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
1. sudo apt-get install python3-venv
2. Im zerocam Ordner python3 -m venv python_env ausführen
3. venv starten python_env/bin/activate

## Django
### Setup
1. Virtual Env starten venv starten python_env/bin/activate
2. pip install Django
3. Projekt erstellen django-admin startproject zerocam_ui
4. In zerocam_ui Ordner wechseln
5. Django App erstellen python manage.py startapp wifi_setup
6. Anleitung befolgen https://docs.djangoproject.com/en/2.1/intro/tutorial01/
7. Admin User erstellen python manage.py createsuperuser