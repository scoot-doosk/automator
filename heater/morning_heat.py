#!/usr/bin/python3

#general imports
import time
import sys

#import needed for plug control
from pyHS100 import SmartPlug, SmartBulb
from pprint import pformat as pf

#ensure correct number of arguments are passed in
if len(sys.argv) != 2:
    print("please use this format:  morning_heat.py <time_in_minutes>")
    exit()

#assign aguements to variables
script_name=sys.argv[0]
on_time=int(sys.argv[1])

#abstracted variables
plug_ip = "10.0.2.41"

#instantiate plug object for heater
heater = SmartPlug(plug_ip)

#turn on for specified time
heater.state = "ON"
time.sleep(60 * on_time)
heater.state = "OFF"

