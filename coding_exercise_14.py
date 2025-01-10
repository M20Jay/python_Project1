<<<<<<< HEAD
heights=input("enter all heights separated by space:")
height_list= heights.split()
count=0
for height in height_list:
    count =count+1
print(count)
for i in range(count):
    height_list[i]=int(height_list[i])
# print(height_list)

total=0
for person in height_list:
    total +=person

avg= total/count
print(round(avg))
=======
heights =input("Enter all heights separated by a comma:")

height_list = heights.split()
count = 0
for height in height_list:
    count +=1
print(count)
for i in range(count): # 0 1 2 3 4
    height_list[i] = int(height_list[i])
total = 0
for j in height_list:
    total +=j

avg =total/count
print(round(avg))
print(height_list)
>>>>>>> d2f791b7029521a7e163bfbf50fc87035f2c9568
