from tkinter import ttk

import tkinter as t
root=t.Tk()
root.title("Untitled - NOTEPAD")

#z=b["text"]
#b["text"]=""
menuobj=t.Menu(root)
root.config(menu=menuobj)

filemenu = t.Menu(menuobj,tearoff=False)
menuobj.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As...")
filemenu.add_separator()
# a=textbox1.get('1.0','end')
# a=textbox1.get('1.0','end-1c')
# textbox1.insert('1.0',value)
# textbox1.delete('1.0','end')
root.mainloop()