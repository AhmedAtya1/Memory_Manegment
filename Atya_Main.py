from tkinter import *
from Segment import segment
from Memory_Manger import  memory_manger
from DisplayMem import displayMem
from Process import process

x=Tk()
mem=memory_manger()
for i in range(10):
    a=segment()
    a.name="seg"+str(i)
    a.size=i+1
    mem.list_segments.append(a)
for i in range(len(mem.list_segments)):
    if i==0:
        mem.list_segments[i].start=0
        mem.list_segments[i].end = mem.list_segments[i].start+mem.list_segments[i].size
    else:
        mem.list_segments[i].start=mem.list_segments[i-1].end
        mem.list_segments[i].end = mem.list_segments[i].start + mem.list_segments[i].size
mem_display=displayMem()
mem_display.drawMem(x,mem.list_segments)


x.mainloop()
