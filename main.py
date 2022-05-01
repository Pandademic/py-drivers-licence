from tkinter.ttk import *
import sv_ttk
from datetime import date
import random
from faker import Faker
root=Tk()
fake = Faker()
fake = Faker(['it_IT', 'en_US','de_CH'])
todays_date = date.today()
root.title("Driver's licence")

root.geometry("300x300")

sv_ttk.set_theme("dark")
name=Label(root,text="NAME: "+fake.name())
name.pack()
personAge=random.randint(0,99)
age=Label(root,text="AGE: "+str(personAge))
age.pack()
fit=Label(root,text="FIT TO DRIVE: "+str(bool(random.getrandbits(1))))
fit.pack()
dob=Label(root,text="DOB: January 1st "+str(todays_date.year-personAge))
dob.pack()
id=Label(root,text="ID: "+str(random.randint(10000, 9999999))+" (random id)")
id.pack()
address=Label(root,text="ADRESS:"+fake.address())
address.pack()
phoneNum=Label(root,text="PHONE NUMBER:"+fake.phone_number())
phoneNum.pack()
job=Label(root,text="OCUPATTION:"+fake.job())
root.mainloop(
