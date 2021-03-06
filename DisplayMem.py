from tkinter import  *
from math import *

class displayMem:
    def check_int(self,number):
        if int(number) == number:
            return int(number)
        else:
            return number

    def reshape(self,number):
        if number >=2:
            number=int(number)
            number=abs(number)
            return int (log(number,2))
        else:
            return int(log(2, 2))





    def drawMem(self,Master,List_of_Sigments=[]):

        def myfunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=250, height=750)

        canvas = Canvas(Master)
        frame = Frame(canvas)
        myscrollbar = Scrollbar(Master, command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)
        canvas.create_window((0, 0), window=frame, anchor='nw')
        frame.bind("<Configure>", myfunction)

        myscrollbar.pack(side=RIGHT,fill="y")
        canvas.pack(side=RIGHT)
        x = 0
        for i in List_of_Sigments:
            s = i.getName() + " " + " ( "+str(self.check_int(i.getStartingAddress()))+" : " + str(self.check_int(i.getEndingAddress())) + " )"
            if i.getName() == "Hole":
                e = Label(frame, text=s, borderwidth=1, relief="solid", width=25, height=2 + self.reshape(i.getSize()),
                          bg="white", font="arial 10 italic")
            elif i.getName()[0:11]=="Old Process":
                e = Label(frame, text=s, borderwidth=1, relief="solid", width=25, height=2 + self.reshape(i.getSize()),
                          bg="grey", font="arial 10 italic")
            else:
                e = Label(frame, text=s, borderwidth=1, relief="solid", width=25 , height= 2 + self.reshape(i.getSize()),bg="green",font="arial 10 italic" )
            e.pack(side="top")
            if x == int(x + (i.getEndingAddress() - i.getStartingAddress())):
                x = x + 1
            else:
                x = x + (i.getEndingAddress() - i.getStartingAddress())

 #row=int(x), column=0