# Coding Exercise
"""
checking whether a year is leap year or not
"""

year = int(input("which year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")