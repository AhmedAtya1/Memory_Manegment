from tkinter import  *
class table():
    def draw (self,master,row,column,text="",width=12):
        s = text
        e = Label(master, text=s, borderwidth=1, relief="solid", width=width, height=2,
                  font="arial 16 italic")
        e.grid(row=row, column=column)

    def drawTable(self, List_of_Sigments=[]):
        Master = Tk()
        x = 1
        self.draw(Master,0,0,"Segments",17)
        for i in List_of_Sigments:
            self.draw(Master, int(x), 0, i.name,17)
            if x == int(x + (i.end - i.start)):
                x = x + 1
            else:
                x = x + (i.end - i.start)
        self.draw(Master, 0, 1, "Size")
        x = 1
        for i in List_of_Sigments:
            self.draw(Master, int(x), 1, i.size)
            if x == int(x + (i.end - i.start)):
                x = x + 1
            else:
                x = x + (i.end - i.start)
        self.draw(Master, 0, 2, "Start")
        x = 1
        for i in List_of_Sigments:
            self.draw(Master, int(x), 2, i.start)
            if x == int(x + (i.end - i.start)):
                x = x + 1
            else:
                x = x + (i.end - i.start)

        Master.mainloop()