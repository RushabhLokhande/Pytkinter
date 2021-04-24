import tkinter
from tkinter import  *

m = Tk()
m.geometry("200x200")

redBtn = Button(m,text="Red",fg="red")
redBtn.pack(side= RIGHT)

redBtn = Button(m,text="Orange",fg="black")
redBtn.pack(side= LEFT)

redBtn = Button(m,text="Blue",fg="blue")
redBtn.pack(side= TOP)

redBtn = Button(m,text="Black",fg="Pink")
redBtn.pack(side= BOTTOM)


C = Canvas(m,bg="SkyBlue",height="200",width="300")
C.pack()

m.title("Home page")

m.mainloop()
