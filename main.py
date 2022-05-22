from tkinter.ttk import *
import sv_ttk
from datetime import date
import random
from faker import Faker

root=Tk()
root.title("Driver's licence")
root.geometry("300x300")
sv_ttk.set_theme("dark")

fake = Faker()
fake = Faker(['it_IT', 'en_US','de_CH'])

todays_date = date.today()

name=Label(root,text="NAME: "+fake.name())
personAge=random.randint(0,99)
age=Label(root,text="AGE: "+str(personAge))
fit=Label(root,text="FIT TO DRIVE: "+str(bool(random.getrandbits(1))))
dob=Label(root,text="DOB: January 1st "+str(todays_date.year-personAge))
id=Label(root,text="ID: "+str(random.randint(10000, 9999999))+" (random id)")
address=Label(root,text="ADRESS:"+fake.address())
phoneNum=Label(root,text="PHONE NUMBER:"+fake.phone_number())
#job=Label(root,text="OCUPATTION:"+fake.job())

name.pack()
age.pack()
fit.pack()
dob.pack()
id.pack()
address.pack()
phoneNum.pack()

root.mainloop()
