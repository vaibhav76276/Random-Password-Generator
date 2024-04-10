import random 
import pyperclip 
from tkinter import *
from tkinter.ttk import *
 
def password_generator(): 
	entry.delete(0, END) 
 
	length = var1.get() 
	i=0
	alpha="abcdefghijklmnopqrstuvwxyz"
	ALPHA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	character="!@#$%^&*()_+-=\/?"
	numbers="1234567890"
	characters = alpha+ALPHA+character+numbers
	password = ""  
	x=random.randint(0,26)
	password+=alpha[x]
	y=len(characters)
	while i != length-2:
    		b=random.choice(characters)
    		password+=b
    		i=i+1
	A=random.randint(0,26)
	password+=ALPHA[A]
	return password
def generate():	   
	password1 = password_generator() 
	entry.insert(10, password1) 
 
def copy(): 
	random_password = entry.get() 
	pyperclip.copy(random_password) 


root = Tk() 
var = IntVar() 
var1 = IntVar() 
 
root.title("Random Password Generator") 

Random_password = Label(root, text="Password") 
Random_password.grid(row=0) 
entry = Entry(root) 
entry.grid(row=0, column=1) 
 
c_label = Label(root, text="Length") 
c_label.grid(row=1) 
 

generate_button = Button(root, text="Generate", command=generate) 
generate_button.grid(row=0, column=2) 
copy_button = Button(root, text="Copy", command=copy) 
copy_button.grid(row=0, column=3)
combo = Combobox(root, textvariable=var1)
combo['values'] = (12, 13, 14, 15, 16, 
				17, 18, 19, 20, 21, 22, 23, 24, 25, 
				26, 27, 28, 29, 30, 31, 32,) 
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1)
 
 
root.mainloop() 
