from tkinter import ttk
import tkinter as t
root=t.Tk()
value=t.StringVar()
def vget():
    
    a=value.get()
    print(a)
box=ttk.Combobox(root,textvariable=value,state='readonly')
box['values']=('select','a','b')
box.current(1)
box.grid(column=0,row=0)
button1=t.Button(root,text='hello',command=vget)
button1.grid(column=0,row=1)
root.mainloop()
