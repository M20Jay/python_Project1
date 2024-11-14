#print("Hellow")

a=1
b="Viaansh"

print(a)
print(b)

#Bitwise Operators
a,b =5,4
print(a&b)
print(a|b)
print(a^b)
print(~b)
print(a<<2)
print(a>>2)
print('\n')
# Identity Operators
a =5
b ="5"
print(a is not b)
print(id(a))
print(id(b))

#Membership Operators
str = ("Jenny")
print('j' not in str)
print('Jen' in str)

# Coding Exercise
#weight=input ('Enter weight in kg:')
#height=input("Enter height in meter:")
#bmi= int(weight)/float(height)**2

#print(int(bmi))

# round() function
print(round(665,-1))

print(round(-8/3))
print(round(-3/2))
print(round(674.1012))
print(round(1212,-2))

# f_string
name ="Krishna"
age =30
height = 1.6
print(f"My name is{name},I am {age} years old and {height} tall")

# if & if else - conditional statements

# height =int(input("enter height in feet:"))

if(height>3):
    print("Buy token")
    print("Now you can board the metro")
else:
    print("No token required")

# coding Exercise 2
number =int(input("Enter a number:"))

if number % 2 == 0:
    print("This is even number")
else:
    print("this is odd number")

