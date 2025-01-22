tuple1= (12,6,-8, 'jenny',True, 12,6)
tuple2= (45,67,90)
tuple3 =(tuple1,tuple2)

tuple4 =tuple1+tuple2
# print(tuple4)

# list1 =[1,2,3,5]
# print(tuple(list1))

tuple2=("Rama","Heena","Raj",
"Mohsin","Aditya")

# print(sorted(tuple2))
tuple3 = (19,12,56,18,9,87,34)

# print(min(tuple3))
#
# print(max(tuple3))

#Program 10-1
#To store records of students in tuple and print them
st=((101,"Aman",98),(102,"Geet",95),(103,"sahil",87),(104,"Pawan",79))
# print("S_No","Roll_No","Name","Marks")
# for i in range(0,len(st)):
    # print((i+1),'\t',st[i][0],'\t', st[i][1], '\t', st[i][2])

# Program 10-2
# Program to swap two numbers
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# print("\nNumbers before swapping:")
# print("First Number:",num1)
# print("Second Number:",num2)
# (num1,num2) = (num2,num1)
# print("\nNumbers after swapping")
# print("First Number:",num1)
# print("Second Number:",num2)

#Program 10-3
#Function to compute area and circumference of the circle.
# def circle(r):
#     area = 3.14 *r*r
#     circumference =2*3.14*r
#     # returns a tuple having two elements area and circumference
#     return(area,circumference)
# # end of function
# radius =int(input('Enter radius of circles:'))
# area,circumference = circle(radius)
# print('Area of circle is:',area)
# print('Circumference of circle is:',circumference)

#Program 10-4
#Program to input n numbers from the user. Store these numbers
#in a tuple. Print the maximum and minimum number from this tuple.
numbers = tuple() #create an empty tuple 'numbers'
n = int(input("How many numbers you want to enter?: "))
for i in range(0,n):
    num = int(input())
    #it will assign numbers entered by user to tuple 'numbers'
    numbers = numbers +(num,)
print('\nThe numbers in the tuple are:')
print(numbers)
print("\nThe maximum number is:")
print(max(numbers))
print("The minimum number is:")
print(min(numbers))