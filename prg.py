import string
import random
alpha="abcdefghijklmnopqrstuvwxyz"
ALPHA="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
character="!@#$%^&*()_+-=\/?"
numbers="1234567890"
i=0
p=0
characters = alpha+ALPHA+character+numbers
length=int(input("Enter the length of password:"))
password =  ""
x=random.randint(0,26)
password+=alpha[x]
y=len(characters)
while i != length-2:
    b=random.choice(characters)
    password+=b
    i=i+1
A=random.randint(0,26)
password+=ALPHA[A]
p=p+1
print(password)
