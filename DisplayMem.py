from tkinter import  *


class displayMem:
    def drawMem(self,Master,List_of_Sigments=[]):
        x = 0
        for i in List_of_Sigments:
            s = i.getName() + "\n" + " ( "+str(i.getStartingAddress())+" : " + str(i.getStartingAddress() + i.getSize()) + " )"
            e = Label(Master, text=s, borderwidth=1, relief="solid", width=20 , height= 2,bg="grey",font="arial 15 italic" )
            e.grid(row=int(x), column=0)
            if x == int(x + (i.getEndingAddress() - i.getStartingAddress())):
                x = x + 1
            else:
                x = x + (i.getEndingAddress() - i.getStartingAddress())
