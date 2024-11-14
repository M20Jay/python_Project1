# Functions

# - A block of reusable code
def happy_birthday(name,age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old")

happy_birthday("Bro",20)
happy_birthday("Steve", 30)
happy_birthday("Joe",40 )

# A function to display an invoice

def display_invoice(username, amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due:{due_date}")

display_invoice("Brocode", 42.50, "01/01")

# return statement- used to end a function
#   and send a result back to the caller

def add(x,y):
    z=x+y
    return z
print(add(-5,8))

# Complex
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("bob","colymore")

print(full_name)

print("\n")

# key words arguments

def hello (greeting, title, first, last):
    print(f"{greeting}{title} {first} {last}")

hello("hello","Mr.",'Spongebob',"Squarepants")

print("\n")
# Exercise
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}_{last}"

phone_num = get_phone(country=1, area =123, first = 456, last =7890)

print(phone_num)
print("\n")
# Arbitrary positional arguments
def add(*args):
    c=0
    for i in args:
        c +=i
    print(f"sum is {c}")

add(1,2)
add(6,5,6)
add(1,2,3,4,56,8)

print("\n")
# Arbitrary key word argument
def info_person(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

info_person(name='Ram', age = 30, dept='CSE')
info_person(name="Shyam", dept= 'CSE')

print("\n")
#Logical Operators
a,b=4,3
c=True
print(a<4 or c)

#string manipulation
print("Hello world\nHello world\nHello world")

print('Hello ' + "Jenny")

print("\n")
print("Martin" +' '+ "James")

# input function
#print ("Hey"+ " "+ input("what is your name?")+ ","+"how are you")

#name=input("what is your name?")
#print(name)

