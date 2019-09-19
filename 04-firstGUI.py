# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:20:47 2019

@author: Ishita
"""

import tkinter as tk
from tkinter import *

def hello():
    name_user = entry1.get()
    output_string = "Hello, " + name_user
    #label2 = Label(coolframe)
    label2["text"] = output_string
    #label2.grid(row = 1, column = 1)
"""
#resizable GUI
instance1 = tk.Tk()
instance1.title("My first GUI")
instance1.mainloop()

#non-resizable GUI
instance2 = tk.Tk()
instance2.title("Non-resizable GUI")
#put false for x and False for y directions
instance2.resizable(False, False)
instance2.mainloop()
"""

#adding widgets
instance3 = tk.Tk()
instance3.title("Widgets")

coolframe = tk.Frame(instance3)
coolframe.pack()

label1 = tk.Label(coolframe, text="Enter your name.")
button1 = tk.Button(coolframe, text="Message Me", command=hello)
entry1 = tk.Entry(coolframe)
label2 = tk.Label(coolframe)

label1.grid(row = 0, column = 0)
entry1.grid(row = 0, column = 1)
button1.grid(row = 1, column = 0)
label2.grid(row = 1, column = 1)

instance3.mainloop()
 