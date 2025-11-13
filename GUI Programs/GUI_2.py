# import tkinter

# window = tkinter.Tk()

# window.title("Welcome")
# window.geometry("300x300")

# b1 = tkinter.Button(window,text="TOP")
# b1.pack(side=tkinter.TOP)

# b2 = tkinter.Button(window,text="RIGHT")
# b2.pack(side=tkinter.RIGHT)

# b3 = tkinter.Button(window,text="BOTTOM")
# b3.pack(side=tkinter.BOTTOM)

# b4 = tkinter.Button(window,text="RIGHT")
# b4.pack(side=tkinter.LEFT)

# window.mainloop()


from tkinter import *

window = Tk()

window.title("Welcome")
window.geometry("400x400")

b1 = Button(window,text="top")
b2 = Button(window,text="right")
b3 = Button(window,text="bottom")
b4 = Button(window,text="left")

b1.pack(side=TOP)
b2.pack(side=RIGHT)
b3.pack(side=BOTTOM)
b4.pack(side=LEFT)

window.mainloop()


