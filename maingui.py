from tkinter import *
from user_interface_gui import interface
root=Tk()
f=Frame(root)
f.pack()
i=interface(f)
def reset():
    global f
    f.pack_forget()
    f.destroy()
    f = Frame(root)
    f.pack()
    i = interface(f)
reset_b = Button(root, text=" reset ", command=reset)
reset_b.pack(side=BOTTOM)
root.mainloop()
