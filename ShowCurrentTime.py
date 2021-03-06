#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 21:42:43 2016

@author: Sandro R DeSouza

Porpose: show hours from the system
"""

from time import time
import os

# Clear screen
os.system('clear')

# Get the current time
currentTime = time()

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Get the current seconds
currentSecond = totalSeconds % 60

# Obtain the total minuts
totalMinutes = totalSeconds // 60

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtein the total hours
totalHours = totalMinutes // 60

# Compute the current hours
currentHour = totalHours % 24


print('Show Time')
print('=========\n')

print('This program show the local time from machine.')

TimeZone = eval(input('Enter your time zone (e.g. -3): '))

# Display results
print('\nCurrent time is', currentHour, ':',
      currentMinute,':', currentSecond, 'GMT')

# Display result, adjusting local time using modular arithmetic 
currentHourLocal = (currentHour + TimeZone) % 24
print('Current time is', currentHourLocal, ':',
      currentMinute,':', currentSecond, 'Local\n')
