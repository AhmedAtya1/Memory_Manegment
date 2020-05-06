from tkinter import  *


class displayMem:
    def drawMem(self,Master,List_of_Sigments=[]):
        x = 0
        for i in List_of_Sigments:
            s = i.name + "\n" + " ( "+str(i.start)+" : " + str(i.start + i.size) + " )"
            e = Label(Master, text=s, borderwidth=1, relief="solid", width=20 , height= 2,bg="grey",font="arial 15 italic" )
            e.grid(row=int(x), column=0)
            if x == int(x + (i.end - i.start)):
                x = x + 1
            else:
                x = x + (i.end - i.start)
