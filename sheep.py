from tkinter import *
import tkinter as tk

root = Tk()

canvas = Canvas(root,height=480,width=900) # Canvas is rectangle space that is for complex elements
canvas.pack

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8) #.place is to put elements ontop of eachother

label = Label(frame,text="Sheep Entry")
label.grid(row=0,column=1)


root.mainloop()
