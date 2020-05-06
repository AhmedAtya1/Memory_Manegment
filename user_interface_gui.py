from tkinter import *
class interface :
    def __init__(self,master):
        self.f=Frame(master)
        self.f.pack(side=LEFT)
        self.mem_size=Label(self.f,text=" memory size ")
        self.mem_size.grid(row=0,column=0)
        self.mem_entry=Entry(self.f)
        self.mem_entry.grid(row=0,column=1)
        self.add_hole_b=Button(self.f,text=" add new hole ",command=self.add_hole)
        self.add_hole_b.grid(row=1,columnspan=2)
        self.ok = Button(self.f, text=" run ", command=self.run)
        self.ok.grid(row=3, columnspan=2)


    def add_hole(self):
        self.add_hole_b["state"] = "disabled"
        self.hole_frame =Frame(self.f)
        self.hole_frame.grid(row=2)
        self.hole_start = Label(self.hole_frame, text=" hole starting address ")
        self.hole_start.grid(row=0, column=0)
        self.hole_start_entry = Entry(self.hole_frame)
        self.hole_start_entry.grid(row=0, column=1)
        self.hole_sizee = Label(self.hole_frame, text=" hole size ")
        self.hole_sizee.grid(row=1, column=0)
        self.hole_size_entry = Entry(self.hole_frame)
        self.hole_size_entry.grid(row=1, column=1)
        self.add_hole1_b = Button(self.hole_frame, text=" add  ", command=self.str_hole)
        self.add_hole1_b.grid(row=2, columnspan=2)

    def str_hole(self):
        self.add_hole_b["state"] = "normal"
        hole_start_address= int(self.hole_start_entry.get())
        hole_size=int( self.hole_size_entry.get())
        # 5od ma3lomat l hole
        self.hole_frame.pack_forget()
        self.hole_frame.destroy()
    def run(self): pass

