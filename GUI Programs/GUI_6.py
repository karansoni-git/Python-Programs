from tkinter import *

window = Tk()
window.title("Frame Example")
window.geometry("300x300")

f = Frame(window,bg="yellow")
f.pack()

lf = Frame(window,bg="red")
lf.pack(side=LEFT)

rf = Frame(window,bg="blue")
rf.pack(side=RIGHT)

b1 = Button(lf,text="Login")
b2 = Button(rf,text="Register")

b1.pack(side=LEFT)
b2.pack(side=RIGHT)

window.mainloop()