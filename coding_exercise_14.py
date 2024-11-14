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
