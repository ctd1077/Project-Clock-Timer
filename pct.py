#!/usr/bin/env python3
# Project Clock Timer
import pickle
from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d-%H-%M-%S")
    d2 = datetime.strptime(d2, "%Y-%m-%d-%H-%M-%S")
    return abs((d2 - d1))

def days_hours_minutes_sec(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60, (td.seconds)%60



if __name__ == '__main__':
    eop = 'Times Up'
    unc = 'Under Construction'
    pickle_in = open('dict.pickle', 'rb')
    open_dict = pickle.load(pickle_in)
    date = open_dict['Date'].split('/')
    year  = date[2]
    day   = date[1]
    month = date[0]
    year = '20'+year # Temp line, need to find a solution 
    dash = '-'
    d1 = year+dash+month+dash+day+dash+'0'+dash+'0'+dash+'0'

    while True:
        current_date_and_time = datetime.now()
        a = str(current_date_and_time.date())
        b = str(current_date_and_time.time())
        rp = b.replace(":", "-")
        sp = rp.split('.')[0]
        d2 = a+'-'+sp
        td = days_between(d1, d2)
        print(days_hours_minutes_sec(td), end='\r')