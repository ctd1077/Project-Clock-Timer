#!/usr/bin/env python3
# UI for Project Countdown
#from tkinter import *
import tkinter as tk


class MainWin:
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
    def __init__(self, master):
        self.master = master
        self.master.geometry('200x200')
        self.frame = tk.Frame(self.master)
        # self.new_proj('Create New Project')
        self.quit = tk.Button(self.frame, text = 'Exit', command = self.close_window)
        self.quit.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()

# create the application
#myapp1 = MainWin()
#myapp1.master.title('Project Countdown')
#days = tk.Entry(myapp1, width=35, borderwidth=5)
#hours = tk.Entry(myapp1, width=35, borderwidth=5)
#days.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
#hours.grid(row=1, column=0, columnspan=5, padx=10, pady=10)




# here are method calls to the window manager class

#myapp.master.title("My Do-Nothing Application")
#myapp.master.maxsize(1000, 400)

# start the program
#myapp.mainloop()
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