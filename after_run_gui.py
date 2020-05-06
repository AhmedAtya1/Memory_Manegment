from tkinter import *
class running :
    def __init__(self, master):
        self.left_frame=Frame(master)
        self.mem_frame=Frame(master)
        self.left_frame.pack(side=LEFT)
        self.mem_frame.pack(side=RIGHT)
        self.add_process_b = Button(self.left_frame, text=" allocate new process ", command=self.add_process)
        self.add_process_b.grid(row=0, column=0)
        self.del_process_b = Button(self.left_frame, text=" deallocate process ", command=self.del_process)
        self.del_process_b.grid(row=0, column=1)
        self.table_b = Button(self.left_frame, text=" table ", command=self.show_table)
        self.table_b.grid(row=0, column=2)
        # draw mem
        hhh="hhhh"




    def add_process(self):
        self.add_process_b["state"] = "disabled"
        self.table_b["state"] = "disabled"
        self.del_process_b["state"] = "disabled"
        self.process_frame=Frame(self.left_frame)
        self.process_frame.grid(row=1)
        self.no_of_segment = Label(self.process_frame, text=" no of segment ")
        self.no_of_segment.grid(row=0, column=0)
        self.no_of_segment_entry = Entry(self.process_frame)
        self.no_of_segment_entry.grid(row=0, column=1)
        self.no_of_segment_b = Button(self.process_frame, text=" ok ", command=self.fill_process)
        self.no_of_segment_b.grid(row=0, column=3)

    def fill_process(self):
        self.num_of_seg=int(self.no_of_segment_entry.get())
        self.process_frame.pack_forget()
        self.process_frame.destroy()
        self.startseg()


    def startseg(self):
        if self.num_of_seg > 0 :
            self.num_of_seg = self.num_of_seg -1
            self.segs_frame = Frame(self.left_frame)
            self.segs_frame.grid(row=1)
            self.segs_name = Label(self.segs_frame, text=" name of segment ")
            self.segs_name.grid(row=0, column=0)
            self.segs_name_entry = Entry(self.segs_frame)
            self.segs_name_entry.grid(row=0, column=1)
            self.segs_sizee = Label(self.segs_frame, text=" segment size ")
            self.segs_sizee.grid(row=1, column=0)
            self.segs_sizee_entry = Entry(self.segs_frame)
            self.segs_sizee_entry.grid(row=1, column=1)
            self.seg_b = Button(self.segs_frame, text=" ok  ", command=self.str_seg)
            self.seg_b.grid(row=2, columnspan=2)

        else :
            # update and draw flag
            flag = FALSE
            if flag is TRUE : pass


    def str_seg(self):
        hhhh="hhhh"
        name_of_seg = self.segs_name_entry.get()
        size_of_seg = float(self.segs_sizee_entry.get())
        #5od ma3lomat l seg
        self.segs_frame.pack_forget()
        self.segs_frame.destroy()
        self.startseg()





    def show_table(self):
        hhh="hhh"


    def del_process(self): pass



