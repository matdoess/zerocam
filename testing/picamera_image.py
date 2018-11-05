from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.rotation = 0
camera.framerate = 15
camera.resolution = (3280, 2464)

camera.capture('picamera_image.jpg')
