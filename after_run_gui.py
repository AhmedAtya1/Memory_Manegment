from tkinter import *
class running :
    def __init__(self, master):
        self.left_frame=Frame(master)
        self.main_frame=Frame(master)
        self.left_frame.pack(side=LEFT)
        self.main_frame.pack(side=RIGHT)
        self.add_process_b = Button(self.left_frame, text=" allocate new process ", command=self.add_process)
        self.add_process_b.grid(row=0, column=0)
        self.del_process_b = Button(self.left_frame, text=" deallocate new process ", command=self.del_process)
        self.del_process_b.grid(row=0, column=1)
        self.table_b = Button(self.left_frame, text=" table ", command=self.show_table)
        self.table_b.grid(row=0, column=2)
        # draw mem

    def show_table(self): pass

    def del_process(self): pass


    def add_process(self):
        self.add_process_b["state"] = "disabled"
        self.table_b["state"] = "disabled"
        self.del_process_b["state"] = "disabled"
        self.process_frame=Frame(self.left_frame)
        self.process_frame.grid(row=1)
        self.no_of_segment = Label(self.process_frame, text=" no of segment ")
        self.no_of_segment.grid(row=0, column=0)
        self.no_of_segment_entry = Entry(self.left_frame)
        self.no_of_segment_entry.grid(row=0, column=1)
        self.no_of_segment_b = Button(self.f, text=" ok ", command=self.fill_process)
        self.no_of_segment_b.grid(row=0, column=3)

    def fill_process(self):

