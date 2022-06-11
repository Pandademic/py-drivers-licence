from tkinter import *
import sv_ttk
from datetime import date
import random
from faker import Faker

root=Tk()
root.title("Driver's licence")
root.geometry("300x300")
sv_ttk.set_theme("dark")

class Person():    
    def __init__(self):
        fake = Faker()
        fake = Faker(['it_IT', 'en_US','de_CH'])
        todays_date = date.today()
        self.name = fake.name()
        _age = random.randint(0,99)
        self.age=str(_age)
        self.atd=str(bool(random.getrandbits(1)))
        self.dob="January 1st "+str(todays_date.year - _age)
        self.id=str(random.randint(10000, 99999999))
        self.address = fake.address()
        self.num = fake.phone_number()

p = Person()

name=Label(root,text="NAME: "+ p.name)
age=Label(root,text="AGE: "+ p.age)
fit=Label(root,text="FIT TO DRIVE: "+ p.atd)
dob=Label(root,text="DOB: "+p.dob)
id=Label(root,text="ID: "+p.id)
address=Label(root,text="ADRESS:"+p.address)
phoneNum=Label(root,text="PHONE NUMBER:"+p.num)

name.pack()
age.pack()
fit.pack()
dob.pack()
id.pack()
address.pack()
phoneNum.pack()

root.mainloop()
