import tkinter as t
root=t.Tk()
root.title("MY TILE")
v1=t.IntVar()
r1=t.Radiobutton(root,text='female',variable=v1,value=1)
r1.grid()
r2=t.Radiobutton(root,text='male',variable=v1,value=2)
r2.grid()
r3=t.Radiobutton(root,text='female',variable=v1,value=3)
r3.grid()
r4=t.Radiobutton(root,text='male',variable=v1,value=4)
r4.grid()
v1.set(1)
root.state('zoomed')

root.mainloop()