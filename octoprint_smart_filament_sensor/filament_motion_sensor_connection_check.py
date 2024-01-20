#!/usr/bin/python3
######################
##                  ##
##  Instructions    ##
##                  ##
######################
##
##  - Run this script on the OctoPi
##  - python3 filament_motion_sensor_connection_check.py
##  - To save some filament you can unload the filament
##      before and move it manually in the sensor
from gpiozero import Button
import time

#CONST
# Configure your GPIO pin
USED_PIN = 17
# Time in seconds
max_not_moving_time = 2
# Set up the GPIO channels - one input and one output

btn = Button(USED_PIN)

# Get current time in seconds
lastMotion = time.time()

def main():
	try: 
		
		lastValue = btn.value
		btn.when_activated = motion
		btn.when_deactivated = motion
  			
		while True:
			timespan = (time.time() - lastMotion)

			if (timespan > max_not_moving_time):
				print("No motion detected")
			else:
				print ("Moving")

			time.sleep(0.250)
		
		
	except KeyboardInterrupt:
		print ("Done")
		pass


def motion():
	lastValue = btn.value
	lastMotion = time.time()
	print(f"Motion detected, value = {lastValue} at {lastMotion}")

main()