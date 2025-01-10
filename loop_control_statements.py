# # while
# count =1
# while count <=10:
#     print(count)
#     count +=1
#     if count==7:
#         break
#     print('hi')
# print("out from the loop")

#Nested loops
list1=['hi','hello','welcome']
names =['Krishn','Ram','Madhav']

for item in list1:
    for name in names:
        print(item,name)
        if item =="hello" and name =='Ram':
            break
    print("out from inner loop")
print("out from outer loop")

