from tkinter import *
import os
from tkinter import filedialog
root=Tk()
E1=Entry(root)
E1.pack()
def d():
    test = os.listdir(filepath)
    for item in test:
        if item.endswith(E1.get()):
            os.remove(os.path.join(filepath, item))
def s():
    global filepath
    filepath = filedialog.askdirectory()
    print(filepath)
B1=Button(root,text="select",command=s)
B1.pack()
B2=Button(root,text="delete",command=d)
B2.pack()
root.mainloop()