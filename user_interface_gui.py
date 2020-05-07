from tkinter import *
from after_run_gui import running
from MemoryManager import memoryManager
class interface :
    def __init__(self,master):
        self.mm=memoryManager()
        self.f2=Frame(master)
        self.f=Frame(master)
        self.f.pack()
        self.mem_size=Label(self.f,text=" Memory size ",font="arial 12 italic")
        self.mem_size.grid(row=0,column=0)
        self.mem_entry=Entry(self.f,font="arial 12 italic")
        self.mem_entry.grid(row=0,column=1)
        self.add_hole_b=Button(self.f,text=" Add new hole ",command=self.add_hole,font="arial 12 italic",width=10 )
        self.add_hole_b.grid(row=1,columnspan=2)
        self.ok = Button(self.f, text=" Run ", command=self.run,font="arial 12 italic",width=5 )
        self.ok.grid(row=3, columnspan=2)

    def add_hole(self):
        self.add_hole_b["state"] = "disabled"
        self.ok["state"] = "disabled"
        self.hole_frame =Frame(self.f)
        self.hole_frame.grid(row=2)
        self.hole_start = Label(self.hole_frame, text=" Hole starting address ",font="arial 12 italic")
        self.hole_start.grid(row=0, column=0)
        self.hole_start_entry = Entry(self.hole_frame,font="arial 12 italic")
        self.hole_start_entry.grid(row=0, column=1)
        self.hole_sizee = Label(self.hole_frame, text=" Hole size ",font="arial 12 italic")
        self.hole_sizee.grid(row=1, column=0)
        self.hole_size_entry = Entry(self.hole_frame,font="arial 12 italic")
        self.hole_size_entry.grid(row=1, column=1)
        self.add_hole1_b = Button(self.hole_frame, text=" Add  ", command=self.str_hole,font="arial 12 italic")
        self.add_hole1_b.grid(row=2, columnspan=2)

    def str_hole(self):
        self.add_hole_b["state"] = "normal"
        self.ok["state"] = "normal"
        hole_start_address= int(self.hole_start_entry.get())
        hole_size=int( self.hole_size_entry.get())
        self.mm.addHole(hole_start_address,hole_size)
        self.hole_frame.pack_forget()
        self.hole_frame.destroy()

    def run(self):
        self.mm.setSize(int(self.mem_entry.get()))
        self.mm.divideMem()
        self.f.pack_forget()
        self.f.destroy()
        self.f2.pack()
        r=running(self.f2,self.mm)
