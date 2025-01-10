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