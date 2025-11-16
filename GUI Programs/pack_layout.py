from tkinter import *
parent = Tk(className="pack layout")
parent.geometry("300x300")

bluebtn = Button(parent,text="Blue Button" ,bg="blue", fg="white",height=5)

bluebtn.pack(fill=X ,expand=True)
parent.mainloop()