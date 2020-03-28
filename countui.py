#!/usr/bin/env python3
# UI for Project Countdown
#from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class MainWin:
    '''Main GUI window to view status of project'''
    def __init__(self, master):
        self.master = master
        self.master.geometry('200x200')
        self.frame = tk.Frame(self.master)
        self.newproj('Create New Project', ProjectWin)
        self.quit = tk.Button(self.frame, text = 'Exit', command = self.close_window)
        self.quit.pack()
        self.frame.pack()

    def newproj(self, text, _class):
        tk.Button(self.frame, text=text, command=lambda: self.proj_win(_class)).pack()

    def proj_win(self, _class):
        self.new = tk.Toplevel(self.master)
        _class(self.new)

    def close_window(self):
        self.master.destroy()

class ProjectWin:
    '''Second GUI window for creating a new project'''
    def __init__(self, master): 
        self.master = master
        self.master.geometry('200x200')
        self.frame = tk.Frame(self.master)
        self.date = tk.Button(self.frame, text = 'Enter Date', command = self.pick_date_dialog)
        self.quit = tk.Button(self.frame, text = 'Save', command = self.close_window)
        self.date.pack()
        self.quit.pack()
        self.frame.pack()

    def pick_date_dialog(self):
        '''Date pick GUI for user to set project date'''
        self.datewin = tk.Tk()
        self.datewin.withdraw()# hide naff extra window
        self.datewin.title('Please choose a date')
        def sav_date():
            self.date = (self.cal.get_date())
            print(self.date) # change to save the datetime object
            self.datewin.destroy()
        self.top = tk.Toplevel(self.datewin)
        # defaults to today's date
        self.cal = Calendar(self.top,font="Arial 10", background='darkblue',foreground='white', selectmode='day')
        self.cal.pack()
        ttk.Button(self.top, text="Save", command=sav_date).pack()
        #ttk.Button(self.datewin, text = 'Exit', command = self.close_window).pack()
       # self.quit.pack()

    def close_window(self):
        self.master.destroy()

# TODO:
# 1. Add Project name option
# 2. Save Project name and date objects
# 3. Call date script for countdown
# 4. Show/print in GUI
# 5. Format to look nice
# 6. Create icon and exe
# 7. Update comments and README 


window = tk.Tk()
app = MainWin(window)
window.mainloop()




































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