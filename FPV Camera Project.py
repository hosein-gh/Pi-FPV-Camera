#!/usr/bin/env python3
import picamera
import datetime
import time
import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_SWITCH = 7  # Physical pin 26, switch to GND
GPIO.setup(GPIO_SWITCH,GPIO.IN,pull_up_down = GPIO.PUD_UP)

GPIO.setup(5,GPIO.OUT)
GPIO.output(5,GPIO.HIGH)

def LED_bilking():
	while True:
		if Record == 1:
			GPIO.output(5,GPIO.LOW)
			time.sleep(1)
			GPIO.output(5,GPIO.HIGH)
			time.sleep(1)

thread = threading.Thread(target=LED_bilking)
thread.daemon = True

print ("  Press Ctrl & C to Quit")

Record = 0

try:
	thread.start()
	while True:
		with picamera.PiCamera() as camera:
			camera.resolution = (1280, 720)
			camera.framerate = 60
			camera.rotation = 180
			camera.exposure_mode = 'sports'
			camera.sensor_mode = 5
			camera.video_stabilization = True
			camera.video_denoise = True
			camera.start_preview(fullscreen=False, window=(0, 0, 1, 1))
			while GPIO.input(GPIO_SWITCH) == 1 :
				time.sleep(0.15)
				#listen here for radio control to capture image while not recording video
			Record = 1
			print ("Recording")
			now = datetime.datetime.now()
			timestamp = now.strftime("%y-%m-%d %H:%M:%S")
			camera.start_recording(str(timestamp) + '.h264')
			time.sleep(.5)
			while Record == 1:
				#listen here for radio control to capture image while recording video
				camera.wait_recording(.01)
				if GPIO.input(GPIO_SWITCH) == 0:
					print ("Stopped")
					camera.stop_recording()
					Record = 0
					GPIO.output(5,GPIO.HIGH)
					while GPIO.input(GPIO_SWITCH) == 0:
						time.sleep(0.1)
					time.sleep(.5)
				

except KeyboardInterrupt:
	print ("Quit")
	GPIO.cleanup() 
