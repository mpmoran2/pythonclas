from tkinter import *
import tkinter as tk

root = Tk()

canvas = Canvas(root,height=480,width=900) # Canvas is rectangle space that is for complex elements
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8) #.place is to put elements ontop of eachother

label = Label(frame,text="Sheep Entry")
label.grid(row=0,column=1)

name = Label(frame,text="Name of Sheep:")
name.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

color = Label(frame,text="Color of Sheep:")
color.grid(row=2, column=0)
entry_color = Entry(frame)
entry_color.grid(row=2,column=1)

age = Label(frame,text="Age of Sheep:")
age.grid(row=3, column=0)
entry_age = Entry(frame)
entry_age.grid(row=3,column=1)

button = Button(frame,text="Submit Sheep")
button.grid(row=4,column=1)

root.mainloop()
