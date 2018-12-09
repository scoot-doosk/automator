#!/bin/python


#import everything from the lifx module and sys to handle arguements
import sys
import time
from lifxlan import *

#ensure correct number of arguments are passed in
if len(sys.argv) != 2:
    print("please use this format:  sunrise.py <time_in_minutes>")
    exit()

#assign aguements to variables
script_name=sys.argv[0]
wake_time=int(sys.argv[1])


#create LAN object
lifx = LifxLAN()

# get devices and store in array
#devices = lifx.get_lights()
light = Light("D0:73:D5:21:C8:34", "10.0.2.61")


light.set_color([0,0,65535,3500], 1, 1)
light.set_power(True)

light.set_color([0,65535,0,3500], (wake_time * 60 * 1000), 1)
time.sleep(waketime*60)
light.set_power(False)
