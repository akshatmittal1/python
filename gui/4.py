import tkinter as t
root=t.Tk()
root.title("MY TILE")
v1=t.IntVar()
v2=t.IntVar()
r1=t.Checkbutton(root,text='python',variable=v1)
r1.grid()
r2=t.Checkbutton(root,text='java',variable=v2)
r2.grid()
root.state('zoomed')

root.mainloop()



