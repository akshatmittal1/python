from PIL import Image,ImageFilter
import os
import tkinter as t
import ntpath
from tkinter import ttk
from tkinter.filedialog import  askopenfilename,asksaveasfilename
root=t.Tk()
a=""
image1 = Image
value = t.StringVar()
def openfilefunction():
    a=askopenfilename()
    fp,fn=ntpath.split(a)
    os.chdir(fp)
    image1 = Image.open(fn)

button1=t.Button(root,text="openfile",command=openfilefunction)
button1.grid(row=0,column=0)
def filterfunction():
    b= value.get()
    # if(b=='filter'):
    #     image1.rotate(360)
    if(b=='dotted_image'):
        image1.convert(mode='1')
    if(b=='black_and_white'):
        image1.convert(mode='L')
    if(b=='blur'):
        image1.filter(ImageFilter.GaussianBlur(15))

box = ttk.Combobox(root, textvariable=value, state='readonly')
box['values'] = ('filter', 'dotted_image', 'black_and_white','blur')
box.current(0)
box.grid(column=0, row=2)
filterfunction()
def savefilefunction():
    c=asksaveasfilename()
    fp, fn = ntpath.split(c)
    os.chdir(fp)
    image1.save(fn,'.jpg')


button2=t.Button(root,text="savefile",command=savefilefunction)
button2.grid(row=5,column=0)
# button1=t.Button(root,text="apply",command=db)
# button1.grid(row=0,column=0)
root.mainloop()