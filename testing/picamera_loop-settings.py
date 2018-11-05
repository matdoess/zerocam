from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.framerate = 15
camera.resolution = (2592, 1944)

camera.start_preview()
sleep(2)
#camera.capture('img/effect_0-none.jpg')
#Loop over Effects
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    camera.capture('img/effect_%s.jpg' % effect)
    sleep(2)
camera.image_effect = "none"

for awbmode in camera.AWB_MODES:
    camera.awb_mode = awbmode
    camera.annotate_text = "AWB Mode: %s" % awbmode
    camera.capture('img/awb_%s.jpg' % awbmode)
    sleep(2)
camera.awb_mode = "auto"

for exposuremode in camera.EXPOSURE_MODES:
    camera.exposure_mode = exposuremode
    camera.annotate_text = "Exposure Mode: %s" % exposuremode
    camera.capture('img/exposure_%s.jpg' % exposuremode)
    sleep(2)
camera.exposure_mode = "auto"

for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    camera.capture('img/brightness%s.jpg' % i)
    sleep(0.1)
camera.brightness = 50

for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    camera.capture('img/contrast%s.jpg' % i)
    sleep(0.1)
camera.contrast = 50

camera.stop_preview()

