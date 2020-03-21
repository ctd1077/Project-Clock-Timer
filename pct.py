# Project Clock Timer
import time
import sys

# Snippet I took from SO, works for what I need it to do.

print('Enter lenght of time for project')
print(' ')

dy=input('Enter # of days: ')
hr=input('Enter # of hours: ')
print(' ')

day=int(dy)
hour=int(hr)
min = 0
sec= 60


# Take a look at the while statements. Can this be written better?


while day > -1:
    while hour > -1:
        sec=sec-1
        time.sleep(1)
        sec1 = ('%02.f' % sec)  # format
        min1 = ('%02.f' % min)
        hour1 = ('%02.f' % hour)
        day1 = ('%02.f' % day)
        sys.stdout.write('\r' + str(day1) + ':' + str(hour1) + ':' + str(min1) + ':' + str(sec1))

    hour=hour-1
    sec=60
day=day-1
min=59

Print('Countdown Complete.')
time.sleep(30)

