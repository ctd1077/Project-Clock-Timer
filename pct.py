#!/usr/bin/env python3
# Project Clock Timer
#import time
#import sys
from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d-%H-%M-%S")
    d2 = datetime.strptime(d2, "%Y-%m-%d-%H-%M-%S")
    return abs((d2 - d1))

def days_hours_minutes_sec(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60, (td.seconds)%60



if __name__ == '__main__':
    pn=input("What's the name of project? ")
    year=input('Enter Year the project will be finished: ')
    day=input('Enter # of days: ')
    hour=input('Enter # of hours: ')
    das = '-'
    # Need to fix the format of the date entered
    # go back to JN
    #d1 = year+das+day+das+hour+das+'0'+das+'0'+das+'0'
    d1 = '2020-06-12-0-0-0'
    while True:
        current_date_and_time = datetime.now()
        a = str(current_date_and_time.date())
        b = str(current_date_and_time.time())
        rp = b.replace(":", "-")
        sp = rp.split('.')[0]
        d2 = a+'-'+sp
        td = days_between(d1, d2)
        print(days_hours_minutes_sec(td), end='\r')