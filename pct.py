#!/usr/bin/env python3
# Project Clock Timer
import time
import sys
# from . import countui # import tkinter UI

print('Enter lenght of time for project')
day=input('Enter # of days: ')
hour=input('Enter # of hours: ')

days=int(day)
hours=int(hour)
min = 0
sec= 60

eop = 'Times Up'
unc = 'Under Construction'
 
while days > -1:
    while hours > -1:
        while min > -1:
            while sec > 0:
                sec=sec-1
                time.sleep(1)
                s = ('%02.f' % sec)  # format
                m = ('%02.f' % min)
                h = ('%02.f' % hours)
                d = ('%02.f' % days)
                sys.stdout.write('\r' + str(d) + ':' + str(h) + ':' + str(m) + ':' + str(s))
                print(': '+ unc, end='\r')
            min=min-1
            sec=60
        hours=hours-1
        min=59
    days=days-1
    hours=23

Print(eop)
