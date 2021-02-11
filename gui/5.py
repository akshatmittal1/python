import tkinter as t
import mysql.connector
root=t.Tk()
def db():

    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    sql = con.cursor()
    sql.execute("use guidb")
    a=textbox.get()
    b=textbox1.get()
    c=textbox2.get()
    x=int(c)
    d=textbox3.get()
    e=textbox4.get()
    f=v1.get()
    g=v2.get()
    h=v3.get()
    i=v4.get()
    l="-"
    k="-"
    m="-"
    if(g==1):
        l="python-"
    if(h==1):
        k="java-"
    if(i==1):
        m="php-"
    t=l+k+m



    if(f==1):
        y='male'
    else:
        y='female'
    qry = "insert into form values('%s','%s',%d,'%s','%s','%s','%s')" % (a, b, x, d,e,y,t)


    sql.execute(qry)
    con.commit()
    root.destroy()
root.title("MY TILE")
label1=t.Label(root,text="Name")
label1.grid(row=0,column=0)
label2=t.Label(root,text="city")
label2.grid(row=1,column=0)
label3=t.Label(root,text="mobile")
label3.grid(row=2,column=0)
label4=t.Label(root,text="Email")
label4.grid(row=3,column=0)
label5=t.Label(root,text="password")
label5.grid(row=4,column=0)
label5=t.Label(root,text="gender")
label5.grid(row=5,column=0)
label5=t.Label(root,text="courses")
label5.grid(row=7,column=0)

textbox=t.Entry(root)
textbox.grid(row=0,column=1)
textbox1=t.Entry(root)
textbox1.grid(row=1,column=1)
textbox2=t.Entry(root)
textbox2.grid(row=2,column=1)
textbox3=t.Entry(root)
textbox3.grid(row=3,column=1)
textbox4=t.Entry(root,show='*')
textbox4.grid(row=4,column=1)
v1=t.IntVar()
r1=t.Radiobutton(root,text='female',variable=v1,value=2)
r1.grid(row=5,column=1)
r2=t.Radiobutton(root,text='male',variable=v1,value=1)
r2.grid(row=6,column=1)
v2=t.IntVar()
v3=t.IntVar()
v4=t.IntVar()
r1=t.Checkbutton(root,text='python',variable=v2)
r1.grid(row=7,column=1)
r2=t.Checkbutton(root,text='java',variable=v3)
r2.grid(row=8,column=1)
r3=t.Checkbutton(root,text='php',variable=v4)
r3.grid(row=9,column=1)



button1=t.Button(root,text="register",command=db)
button1.grid(row=13,column=1)
root.state('zoomed')

root.mainloop()



