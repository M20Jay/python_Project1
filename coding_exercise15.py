numbers =input('Enter list of numbers:')
#34 45 12 -8 89 67

numbers_List = numbers.split()
count = 0
for number in numbers_List:
    count +=1


print(f'The length of the list is:{count}')

for i in range(count):
    numbers_List[i] = int(numbers_List[i])

maximum_number= numbers_List[0]

for num in numbers_List:
    if num >maximum_number:
        maximum_number = num
print(f'The maximum number is : {maximum_number}')

