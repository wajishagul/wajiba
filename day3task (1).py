#importing library
from tkinter import *
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('600x600')
#Declaring Window Color
window.configure(background = "blue")
label_0= Label(window,text="Registration form",width=15,font = ("bold",20))
label_0.grid(row =0,column = 4)
#below four fields are declared
Firstname = Label(window ,text = "First Name").grid(row = 2,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 3,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 4,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 5,column = 0)
a1 = Label(window ,text = "Contact Number").grid(row = 6,column = 0)
pan = Label(window ,text = "pan Number").grid(row = 7,column = 0)
adhaar = Label(window ,text = "adhaar Number").grid(row = 8,column = 0)
tele = Label(window ,text = "telephone Number").grid(row = 9,column = 0)
college = Label(window ,text = "college name").grid(row = 10,column = 0)
school = Label(window ,text = "school name").grid(row = 11,column = 0)
insta = Label(window ,text = " instagram id").grid(row = 12,column = 0)
roll = Label(window ,text = "roll number").grid(row = 13,column = 0)
age = Label(window ,text = "age").grid(row = 14,column = 0)
pnr = Label(window ,text = "pnr Number").grid(row = 15,column = 0)

Firstname1 = Entry(window).grid(row = 2,column = 1)
Lastname1 = Entry(window).grid(row = 3,column = 1)
Email1 = Entry(window).grid(row = 4,column = 1)
Mobile1 = Entry(window).grid(row = 5,column = 1)
a11= Entry(window).grid(row = 6,column = 1)
pan1 = Entry(window).grid(row = 7,column = 1)
adhaar1 = Entry(window).grid(row = 8,column = 1)
tele1 = Entry(window).grid(row = 9,column = 1)
college1 = Entry(window).grid(row = 10,column = 1)
school1 = Entry(window).grid(row = 11,column = 1)
insta1 = Entry(window).grid(row = 12,column = 1)
roll1 = Entry(window).grid(row = 13,column = 1)
age1 = Entry(window).grid(row = 14,column = 1)
pnr1 = Entry(window).grid(row = 15,column = 1)
var1=IntVar()
Checkbutton(window,text= "accept terms and condition", variable=var1).place(x=230,y=330)
#fubction declaration
def clicked():
        res = "Welcome to " + txt.get()
        lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").place(x = 70,y=380)
window.mainloop()

