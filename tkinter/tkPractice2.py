#!/usr/bin/python2.7


import Tkinter as tk
import tkMessageBox as mb

#I'm making a window and defining some labels for it
the_window = tk.Tk()
the_window.title('Timer')
the_window.geometry("500x150+1+1")
the_window.lift()
the_window.wm_attributes("-topmost", 1)
#the_window.winfo_geometry(
label = tk.Label(the_window, text='Practice Window', font=("Helvetica", 32))
label.pack(side ='top')




#def helloCallBack():
#   mb.showinfo( "Hello Python", "Hello World")

#def practiceCommand(mass, acceleration):
#    force = mass*acceleration
#    return force

#B = tk.Button(the_window, text ="Hello", command = helloCallBack)
#here is the button that i'm trying
#exampleButton = tk.Button(the_window, text="This is what's UP!!",
#command = practiceCommand)

#exampleButton.pack()
#B.pack()
the_window.mainloop()