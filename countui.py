#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import pct
import pickle
import time

class MainWin:
    '''Main GUI window to view status of project'''
    def __init__(self, master):
        self.master = master
        self.master.configure(background = '#8da0c7')
        self.master.title('Project Timer')
        #self.master.geometry('325x170')
        self.frame = tk.Frame(self.master)
        self.frame.grid(row=3, columnspan=6)
        self.newproj('Create New Project', ProjectWin)
        self.quit = tk.Button(self.frame, text = 'Exit', 
        command = self.close_window, bg='#000000',fg='white')
        self.run = pct.main()
        self.pname = pct.prod_name()
        try:
            self.prod_name = tk.Label(text=self.pname, bd=1,font='Times 14 bold')
            self.prod_name.configure(background = '#8da0c7')
            self.prod_name.grid(column = 2, row = 0, columnspan = 2)

            self.label_day = tk.Label(text=self.run[0],bd=4,relief='sunken',font='Times 14')
            tDay = tk.Label(text='Days',bd=4,relief='flat',font='Times 12')
            tDay.configure(background = '#8da0c7')
            tDay.grid(column=1, row=2)
            self.label_day.configure(background = '#d1dbf0')
            self.label_day.grid(column=1, row=1,ipady="20",ipadx="20")

            self.label_hr = tk.Label(text=self.run[1],bd=4,relief='sunken',font='Times 14')
            tHr = tk.Label(text='Hours',bd=4,relief='flat',font='Times 12')
            tHr.configure(background = '#8da0c7')
            tHr.grid(column=2, row=2)
            self.label_hr.configure(background = '#d1dbf0')
            self.label_hr.grid(column=2, row=1,ipady="20",ipadx="20")

            self.label_min = tk.Label(text=self.run[2],bd=4,relief='sunken',font='Times 14')
            tMin = tk.Label(text='Minutes',bd=4,relief='flat',font='Times 12')
            tMin.configure(background = '#8da0c7')
            tMin.grid(column=3, row=2)
            self.label_min.configure(background = '#d1dbf0')
            self.label_min.grid(column=3, row=1,ipady="20",ipadx="20")

            self.label_sec = tk.Label(text=self.run[3],bd=4,relief='sunken',font='Times 14')
            tSec = tk.Label(text='Seconds',relief='flat',font='Times 12')
            tSec.configure(background = '#8da0c7')
            tSec.grid(column=4, row=2)
            self.label_sec.configure(background = '#d1dbf0')
            self.label_sec.grid(column=4, row=1,ipady="20",ipadx="20")

            self.quit.grid(column=3, row=3)
            global x
            x = True
            self.update_sec()
            self.update_min()
            self.update_hour()
            self.update_day()
        except:
            self.frame.grid(row=2, columnspan=4)
            self.quit.grid(column=1, row=2)

    def newproj(self, text, _class):
        tk.Button(self.frame, text=text, bg='#000000', fg='white',
        command=lambda: self.proj_win(_class)).grid(column=4, row=3)

    def proj_win(self, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new)

    def update_sec(self):
        if x == True:
            self.run = pct.main()
            self.label_sec.configure(text="%i" % self.run[3])
            self.label_sec.after(1000, self.update_sec)

    def update_min(self):
        if x == True:
            self.run = pct.main()
            self.label_min.configure(text="%i" % self.run[2])
            self.label_min.after(1000, self.update_min)

    def update_hour(self):
        if x == True:
            self.run = pct.main()
            self.label_hr.configure(text="%i" % self.run[1])
            self.label_hr.after(1000, self.update_hour)

    def update_day(self):
        if x == True:
            self.run = pct.main()
            self.label_day.configure(text="%i" % self.run[0])
            self.label_day.after(1000, self.update_day)

    def close_window(self):
        x = False
        self.master.destroy()

class ProjectWin:
    '''Second window for creating a new project'''
    def __init__(self, master): 
        self.master = master
        self.master.title('New Project')
        self.frame = tk.Frame(self.master)
        self.frame.configure(background = '#8da0c7')
        self.date = tk.Button(self.frame, text = 'Enter Date', bg='#000000', fg='white',
        command = self.pick_date)
        self.quit = tk.Button(self.frame, text = 'Save', bg='#000000', fg='white',
        command = self.close_window)
        self.pTitle = tk.Label(self.frame,text='Enter Project Name: ',
        bd=2,relief='groove',font='Times 12 bold',bg = '#8da0c7')
        self.pTitle.grid(column=0, row=0,ipady="8",ipadx="20")
        self.pName = tk.Text(self.frame, height=2, width=30,bd=2,relief='sunk')
        self.pName.configure(background = '#d1dbf0')
        self.pName.grid(column=1, row=0)
        self.date.grid(column=0, row=1)
        self.quit.grid(column=1, row=1)
        self.frame.grid(row=1, columnspan=1)

    def pick_date(self):
        '''Date pick GUI for user to set project date'''
        self.datewin = tk.Tk()
        self.datewin.withdraw()# hide naff extra window
        self.datewin.title('Please choose a date')
        self.top = tk.Toplevel(self.datewin)
        self.cal = Calendar(self.top,font="Arial 10", background='darkblue',foreground='white', selectmode='day')
        self.cal.pack()
        ttk.Button(self.top, text="ok", command=self.datewin.destroy).pack()

    def sav_date(self):
        '''Saves the date selected.
        If none is selected the default date is today'''
        global date
        self.date = (self.cal.get_date())
        date = self.date
        print(self.date) # change to save the datetime object

    def retieve_text(self):
        '''Save textbox values if no value is select
        a newline char is saved'''
        global inputValue
        inputValue = self.pName.get('1.0','end-1c')
        print(inputValue)

    def close_window(self):
        '''Save Text and Date values on save button
        write try except if no date is selected'''
        self.sav_date()
        self.retieve_text()
        self.master.destroy()
        dict = {'Project_name':inputValue,'Date':date}
        pickle_out = open('dict.pickle', 'wb')
        pickle.dump(dict, pickle_out)
        pickle_out.close()
        print(dict)


# TODO:
# 1. Added Message for first time users (Save new project and restart)
# 2. Clean up code and use pystyle
# 3. Create icon and exe
# 4. Update comments and README 

window = tk.Tk()
app = MainWin(window)
window.mainloop()
time.sleep(1)
