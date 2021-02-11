import tkinter as t
import tkinter.ttk as tt
from tkinter import messagebox
import time
root=t.Tk()
root.geometry("500x500")
progress=tt.Progressbar(root,orient=t.HORIZONTAL,length="500",mode='determinate')
progress.grid()
label1=t.Label(root,text="0%")
label1.grid()
def bar():


    progress['value']=10
    label1.configure(text="10%")
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 20
    label1.configure(text="20%")
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 30
    label1.configure(text="30%")
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 40
    label1.configure(text="40%")
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 50
    label1.configure(text="50%")
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 60
    label1.configure(text="60%")
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 70
    label1.configure(text="70%")
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 80
    label1.configure(text="80%")
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 90
    label1.configure(text="90%")
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    label1.configure(text="100%")
    root.update_idletasks()

    messagebox.showinfo("title", "completed")
b1=t.Button(root,text='foo', command=lambda :test(2,3))
b1.grid()
#bar()
root.after(10,bar)
def test(a,b):
    print(a+b)
root.mainloop()
