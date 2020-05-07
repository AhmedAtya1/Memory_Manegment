from tkinter import *
import tkinter.messagebox
from DisplayMem import displayMem
from MemoryManager import memoryManager
from Table import table
from MemoryManager import memoryManager
class running :
    def __init__(self, master,mmm):
        self.mm=mmm
        self.full_flag=False
        self.left_frame=Frame(master)
        self.mem_frame=Frame(master)
        self.left_frame.pack(side=LEFT)
        self.mem_frame.pack(side=RIGHT)
        space=Label(self.left_frame,text="\t \t \t ")
        space.grid(row=0,column=4)
        self.add_process_b = Button(self.left_frame, text=" Allocate New Process ",font="arial 15 italic",width=18 , height= 2, command=self.add_process)
        self.add_process_b.grid(row=0, column=0)
        self.del_process_b = Button(self.left_frame, text=" Deallocate Process ",font="arial 15 italic",width=15 , height= 2, command=self.del_process)
        self.del_process_b.grid(row=0, column=1)
        self.table_b = Button(self.left_frame, text=" Table ",font="arial 15 italic",width=10 , height= 2, command=self.show_table)
        self.table_b.grid(row=0, column=2)
        self.allocate_binding = Button(self.left_frame, text="  Allocate Binding Process ",font="arial 15 italic",width=20 , height= 2, command=self.binding)
        self.allocate_binding.grid(row=0, column=3)
        self.allocate_binding["state"] = "disabled"
        mem=displayMem()
        mem.drawMem(self.mem_frame,self.mm.getListOfAllPartitions())

    def add_process(self):
        self.add_process_b["state"] = "disabled"
        self.table_b["state"] = "disabled"
        self.del_process_b["state"] = "disabled"
        self.allocate_binding["state"] = "disabled"
        self.process_frame=Frame(self.left_frame)
        self.process_frame.grid(row=1)
        self.no_of_segment = Label(self.process_frame, text=" no of segment ")
        self.no_of_segment.grid(row=0, column=0)
        self.no_of_segment_entry = Entry(self.process_frame)
        self.no_of_segment_entry.grid(row=0, column=1)
        self.fb = Label(self.process_frame, text=" type(firstFit/bestFit) ")
        self.fb.grid(row=1, column=0)
        self.fb_entry = Entry(self.process_frame)
        self.fb_entry.grid(row=1, column=1)
        self.no_of_segment_b = Button(self.process_frame, text=" ok ", command=self.fill_process)
        self.no_of_segment_b.grid(row=2, columnspan=2)

    def fill_process(self):
        num_of_seg=int(self.no_of_segment_entry.get())
        firstorbest=self.fb_entry.get()
        self.mm.setSegmentsAndAlgorithms(num_of_seg, firstorbest)
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
            self.full_flag =not(self.mm.addProcess())
            self.add_process_b["state"] = "normal"
            self.del_process_b["state"] = "normal"
            self.table_b["state"] = "normal"
            if self.full_flag == True:  self.allocate_binding["state"] = "normal"
            if self.full_flag == False :
                # drawmem
                pass
            else :
                self.biind()

    def biind(self):
        tkinter.messagebox.showinfo("error", "the memory isn't empty enough to add this process now , please deallocate any processes")
        self.allocate_binding["state"] = "normal"
        self.add_process_b["state"] = "disabled"

    def str_seg(self):
        name_of_seg = self.segs_name_entry.get()
        size_of_seg = int(self.segs_sizee_entry.get())
        self.mm.addSegment(name_of_seg,size_of_seg)
        self.segs_frame.pack_forget()
        self.segs_frame.destroy()
        self.startseg()

    def show_table(self):
        self.add_process_b["state"] = "disabled"
        self.del_process_b["state"] = "disabled"
        self.table_b["state"] = "disabled"
        self.allocate_binding["state"] = "disabled"
        self.table_frame = Frame(self.left_frame)
        self.table_frame.grid(row=1)
        process_number = Label(self.table_frame, text=" Enter process name ")
        process_number.grid(row=1,column=0)
        ok_button=Button(self.table_frame,text="OK",command=self.delete_frame_show_table)
        ok_button.grid(row=2,column=3)
        self.enter_process_forTable=Entry(self.table_frame)
        self.enter_process_forTable.grid(row=1,column=1)

    def delete_frame_show_table(self):
        if self.full_flag != True: self.add_process_b["state"] = "normal"
        self.del_process_b["state"] = "normal"
        self.table_b["state"] = "normal"
        if self.full_flag == True:  self.allocate_binding["state"] = "normal"
        process_namee=self.enter_process_forTable.get()
        # self.table = table()
        # table.drawTable(listofsegments_of_certainProcess)    self.enter_process_forTable.segmentlist
        # show the table (missing object)
        self.table_frame.pack_forget()
        self.table_frame.destroy()

    def del_process(self):
        self.add_process_b["state"] = "disabled"
        self.del_process_b["state"] = "disabled"
        self.table_b["state"] = "disabled"
        self.allocate_binding["state"] = "disabled"
        self.del_process_frame = Frame(self.left_frame)
        self.del_process_frame.grid(row=1)
        process_no = Label(self.del_process_frame, text=" Enter process name ")
        process_no.grid(row=1, column=0)
        ok_button = Button(self.del_process_frame, text="OK", command=self.delete_frame_update_memDiagram)
        ok_button.grid(row=2, column=3)
        self.enter_process_for_delete = Entry(self.del_process_frame)
        self.enter_process_for_delete.grid(row=1, column=1)

    def delete_frame_update_memDiagram(self):
        if self.full_flag != True: self.add_process_b["state"] = "normal"
        self.del_process_b["state"] = "normal"
        self.table_b["state"] = "normal"
        if self.full_flag == True:  self.allocate_binding["state"] = "normal"
        process_namee = self.enter_process_for_delete.get()
        # m7mod hydeny fn a3ml beha de allocation
        self.del_process_frame.pack_forget()
        self.del_process_frame.destroy()

    def binding(self):
        # call 7oda bind func
        self.full_flag = False
        if self.full_flag == False:
            # drawmem
            self.add_process_b["state"] = "normal"
            self.allocate_binding["state"] = "disabled"
        else:
            self.biind()
