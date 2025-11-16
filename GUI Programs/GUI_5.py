from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Form")
window.geometry("300x300")

def log():
    messagebox.showinfo("Login Info","Logged in successfully")

login = Button(window,text="Login",command=log)
login.place(x=130,y=130)

window.mainloop()