#fg=""
#bg=""
#format=("Arival ")
#grid attribute  padx pady row column sticky columnspan
import tkinter as t
root=t.Tk()
def calc():
    a=textbox.get()
    print (a)
    b=textbox1.get()
    c=int(a)+int(b)
    textbox.delete(0,'end')
    textbox1.delete(0, 'end')
    textbox2.insert(0,c)
label1=t.Label(root,text="value1")
label1.grid(padx=10,pady=10,row=0,column=0)
label2=t.Label(root,text="value2")
i=1
label2.grid(padx=100,pady=40,row=i,column=0)
label3=t.Label(root,text="result")
label3.grid(padx=10,pady=10,row=2,column=0)

textbox=t.Entry(root)
textbox.grid(row=0,column=1)
textbox1=t.Entry(root)
textbox1.grid(row=1,column=1)
textbox2=t.Entry(root)
textbox2.grid(row=2,column=1)

button1=t.Button(root,text="sum",command=calc)
button1.grid(row=3,column=1)
root.state('zoomed')
root.mainloop()
