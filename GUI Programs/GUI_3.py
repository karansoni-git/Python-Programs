from tkinter import *

window = Tk()

window.title("Student")
window.geometry("300x300")

name = Label(window,text="Name : ")
entery1 = Entry(window)
name.place(x=50,y=50)
entery1.place(x=100 , y=50)

password = Label(window,text="Password : ")
entery2 = Entry(window)
password.place(x=50,y=100)
entery2.place(x=120 , y=100)

window.mainloop()