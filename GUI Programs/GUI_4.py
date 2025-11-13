from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Student Form")
window.geometry("400x400")

name = Label(window,text="Name : ")
nameEntry = Entry(window)
name.grid(row=0,column=0)
nameEntry.grid(row=0,column=1)

rollno = Label(window,text="Rollno : ")
rollnoEntry = Entry(window)
rollno.grid(row=1,column=0)
rollnoEntry.grid(row=1,column=1)

branch = Label(window,text="Branch : ")
bca = Checkbutton(window,text="BCA")
bba = Checkbutton(window,text="BBA")
mca = Checkbutton(window,text="MCA")
mba = Checkbutton(window,text="MBA")

branch.grid(row=2,column=0)
bca.grid(row=3,column=0)
bba.grid(row=4,column=0)
mca.grid(row=5,column=0)
mba.grid(row=6,column=0)

plk = Label(window,text="Programming Language Know : ")
plk.grid(row=7,column=1)

languageList = Listbox(window,height=3,selectmode=MULTIPLE)
languageList.insert(1,"Java")
languageList.insert(2,"C++")
languageList.insert(3,"Javascript")
languageList.grid(row=8,column=1)

male = Radiobutton(window,text="Male",value=1)
male.grid(row=9,column=0)
female = Radiobutton(window,text="Female",value=2)
female.grid(row=9,column=1)
other = Radiobutton(window,text="Other",value=3)
other.grid(row=9,column=2)

def sub():
    messagebox.showinfo("Submitted","Your application sent successfully")

submit = Button(window,text="Submit",command=sub)
submit.grid(row=10,column=1)



window.mainloop()