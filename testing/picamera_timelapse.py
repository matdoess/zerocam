from time import sleep
from picamera import PiCamera

camera = PiCamera(resolution=(1280, 720), framerate=30)
# Set ISO to the desired value
camera.iso = 800
print('Camera ISO =',camera.iso)
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
print('Camera Shutter Speed = ', camera.shutter_speed)
camera.exposure_mode = 'off'
g = camera.awb_gains
print('Camera AWB Gains = ',g)
camera.awb_mode = 'off'
camera.awb_gains = g
# Finally, take several photos with the fixed settings
camera.capture_sequence(['img/timelapse/image2%02d.jpg' % i for i in range(10)])