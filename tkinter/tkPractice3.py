#!/anaconda/bin/python


import Tkinter as tk
import tkMessageBox as mb

#I'm making a window and defining some labels for it
the_window = tk.Tk()
label = tk.Label(the_window, text='Practice Window')
label.pack(side ='left')




def helloCallBack():
   mb.showinfo( "Hello Python", "Hello World")

def practiceCommand(mass, acceleration):
    force = mass*acceleration
    return force

button = tk.Button(the_window, text ="Hello", command = helloCallBack)

entry=tk.Entry(the_window)

entry.pack()
button.pack()
the_window.mainloop()