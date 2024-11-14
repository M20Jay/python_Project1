size = input("What piza size you want (S/M/L)?")
bill = 0
if size == "S" or size == 's':
    bill += 100
    print("Small Pizza price is 100$.")
elif size == 'M' or size == 'm':
    bill +=200
    print("Medium Pizza price is 200$.")
else:
    bill += 300
    print("Large Pizza price is 100$")

add_pepperoni = input("Do you want pepperoni(Y/N)?")
if add_pepperoni == 'y' or add_pepperoni =='Y':
    if size == "S" or size == 's':
        bill +=30
    else:
        bill += 50

extra_cheese = input("Do you want extra cheese(Y/N)?")
if extra_cheese == "y" or extra_cheese =="Y":
    bill +=20
print(f"your total bill is {bill}")

