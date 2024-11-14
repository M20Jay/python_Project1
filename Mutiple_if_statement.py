height = int(input("What is your height? "))
bill = 0

if height>=3:
    print("can ride")
    age = int(input("What is your age:"))
    if age<12:
        bill =150
        print("Ticket Price is 150$")
    elif age <=18:
        bill =250
        print("Ticket Price is 250$")
    else:
        bill =500
        print("Ticket Price is 500$")
    want_photo = input("Do you want to take photo(Y/N)?")
    if want_photo == 'Y' or want_photo == 'y':
        bill = bill + 50
    print(f"your total bill is {bill} :")
else:
    print("Can't ride")
print("Thank you, enjoy the ride")
