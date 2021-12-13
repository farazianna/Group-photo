import picamera
print ("About to take a picture.")
with picamera.PiCamera() as camera:
     camera.start_preview()
     camera.resolution = (1280, 720)
     camera.capture("/home/pi/Group-photo/Group-photo/Group4.jpg")
     camera.stop_preview()
     print("Picture taken.")

