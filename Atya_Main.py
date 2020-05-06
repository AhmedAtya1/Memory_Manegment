from tkinter import *
from Segment import segment
from MemoryManager import memoryManager
from DisplayMem import displayMem
from Process import process
from Table import table
x=Tk()
list_segments=[]
for i in range(10):
    a=segment()
    a.setName("seg"+str(i))
    a.setSize(i+1)
    list_segments.append(a)
for i in range(len(list_segments)):
    if i==0:
        list_segments[i].setStartingAddress(0)
        list_segments[i].setEndingAddress( list_segments[i].getStartingAddress()+list_segments[i].getSize())
    else:
        list_segments[i].setStartingAddress(list_segments[i-1].getEndingAddress())
        list_segments[i].setEndingAddress( list_segments[i].getStartingAddress() + list_segments[i].getSize())
mem_display=displayMem()
mem_display.drawMem(x,list_segments)
table=table()
table.drawTable(list_segments)

x.mainloop()
