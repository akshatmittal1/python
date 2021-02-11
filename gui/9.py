import tkinter as t
#from tkinter import *
import ntpath
from tkinter.filedialog import  askopenfilename,asksaveasfilename

def openfilefunction():
    a=askopenfilename(filetypes =[('Python Files', ['*.py','*.csv'])])#initialdir=""

    x=open(a,"r")
    data=x.read()
    print(data)
    x.close()
openfilefunction()

#print(root.wm title())
#def undofun():
