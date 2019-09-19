# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 12:45:58 2019

@author: Ishita
"""

import tkinter as tk
from tkinter import *

def hi_name():
    string1 = entry1.get()
    string1_display = "Hi, "+ string1
    output1["text"] = string1_display 
    
def my_age():
    string2 = entry2.get()
    string2_display = "So, you are "+ string2 + " years old. I am just 6 months."
    output2["text"] = string2_display

def my_place():
    output3["text"] = "Ha ha ha. I live in your PC."
    
def next_instance():
    instance2 = tk.Tk()
    instance2.title("Message")
    
    frame2 = tk.Frame(instance2)
    frame2.pack()
    
    label00 = tk.Label(frame2, text="Nice talking to you.")
    
    label00.grid()
    
    instance2.mainloop()
        
introGUI = tk.Tk()
introGUI.title("Introduction")

frame1 = tk.Frame(introGUI)
frame1.pack()

label0 = tk.Label(frame1, text="INTRODUCTION")

label1 = tk.Label(frame1, text="Enter your Name")
entry1 = tk.Entry(frame1)
button1 = tk.Button(frame1, text="Message me", command = hi_name)
output1 = tk.Label(frame1)

label2 = tk.Label(frame1, text="How old are you?")
entry2 = tk.Entry(frame1)
button2 = tk.Button(frame1, text="My age", command = my_age)
output2 = tk.Label(frame1)

label3 = tk.Label(frame1, text="Where do you live?")
entry3 = tk.Entry(frame1)
button3 = tk.Button(frame1, text="My place", command = my_place)
output3 = tk.Label(frame1)

button4 = tk.Button(frame1, text="Quit", command = introGUI.destroy)

button5 = tk.Button(frame1, text="Next", command = next_instance)

label0.grid(row = 0, column = 0)

label1.grid(row = 1, column = 0)
entry1.grid(row = 1, column = 1)
button1.grid(row = 2, column = 0, sticky=tk.W, pady = 4)
output1.grid(row = 2, column = 1)

label2.grid(row = 3, column = 0)
entry2.grid(row = 3, column = 1)
button2.grid(row = 4, column = 0, sticky=tk.W, pady = 4)
output2.grid(row = 4, column = 1)

label3.grid(row = 5, column = 0)
entry3.grid(row = 5, column = 1)
button3.grid(row = 6, column = 0, sticky=tk.W, pady = 4)
output3.grid(row = 6, column = 1)

button4.grid(row = 7, column = 0)
button5.grid(row = 7, column = 1)

introGUI.mainloop()

