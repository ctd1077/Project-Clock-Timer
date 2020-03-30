#!/usr/bin/env python3
# UI for Project Countdown
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
        self.master.geometry('500x150')
        self.frame = tk.Frame(self.master)
        self.newproj('Create New Project', ProjectWin)
        self.quit = tk.Button(self.frame, text = 'Exit', command = self.close_window)
        self.run = pct.main()
        print(self.run)
        self.label_day = tk.Label(text=self.run[0])
        self.label_hr = tk.Label(text=self.run[1])
        self.label_min = tk.Label(text=self.run[2])
        self.label_sec = tk.Label(text=self.run[3])
        self.quit.pack()
        self.label_day.pack()
        self.label_hr.pack()
        self.label_min.pack()
        self.label_sec.pack()
        self.frame.pack()
        global x
        x = True
        self.update_sec()
        self.update_min()
        self.update_hour()
        self.update_day()
        

    def newproj(self, text, _class):
        tk.Button(self.frame, text=text, command=lambda: self.proj_win(_class)).pack()

    def proj_win(self, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new)

    def update_sec(self):
        if x == True:
            self.run = pct.main()
            self.label_sec.configure(text="%i s" % self.run[3])
            self.label_sec.after(1000, self.update_sec)

    def update_min(self):
        if x == True:
            self.run = pct.main()
            self.label_min.configure(text="%i m" % self.run[2])
            self.label_min.after(1000, self.update_min)

    def update_hour(self):
        if x == True:
            self.run = pct.main()
            self.label_hr.configure(text="%i h" % self.run[1])
            self.label_hr.after(1000, self.update_hour)

    def update_day(self):
        if x == True:
            self.run = pct.main()
            self.label_day.configure(text="%i d" % self.run[0])
            self.label_day.after(1000, self.update_day)

    def close_window(self):
        x = False
        self.master.destroy()

class ProjectWin:
    '''Second GUI window for creating a new project'''
    def __init__(self, master): 
        self.master = master
        self.master.geometry('200x200')
        self.frame = tk.Frame(self.master)
        self.date = tk.Button(self.frame, text = 'Enter Date', command = self.pick_date_dialog)
        self.quit = tk.Button(self.frame, text = 'Save', command = self.close_window)
        self.pName = tk.Text(self.frame, height=4, width=50)
        self.pName.pack()
        self.date.pack()
        self.quit.pack()
        self.frame.pack()

    def pick_date_dialog(self):
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
# 1. Call date script for countdown
# 2. Show/print in GUI
# 3. Format to look nice
# 4. Create icon and exe
# 5. Update comments and README 

window = tk.Tk()
app = MainWin(window)
window.mainloop()
time.sleep(1)




































# root = Tk()
# root.title('Project Countdown')
# days = Entry(root, width=35, borderwidth=5)
# hours = Entry(root, width=35, borderwidth=5)
# days.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
# hours.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# # The onlick function should submit the data
# def onClick(number):
#     current = e.get() # First save the current number displayed
#     e.delete(0, END) # Next delete the current number displayed
#     e.insert(0, str(current) + str(number)) # Make sure the 

# # Clear the data second func to delete the project
# def onClear():
#     days.delete(0,END)
#     hours.delete(0,END)

# # def onAdd():
# #     first_num = e.get()
# #     global f_num
# #     global math
# #     math = 'addition'
# #     f_num = int(first_num)
# #     e.delete(0,END)

# # Define Buttons
# button_1 = Button(root, text='Submit', command=lambda: onClick(1), padx=40, pady=20)
# button_2 = Button(root, text='Clear', command=lambda: onClear(), padx=40, pady=20)
# button_3 = Button(root, text="Exit", command=root.destroy, padx=40, pady=20)

# # Add the button on the screen
# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)

# root.mainloop()