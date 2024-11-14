import random

# names =input("Enter everybody's name separated by comma:")
# names_list = names.split(",")
# #print(names_list)
#
# # length =len(names_list)
# # random_choice = random.randint(0,length-1)
# Person_selected=random.choice(names_list)
# print(f"{Person_selected} will pay the bill")

names=['Jenny','Payal','John']

print(f'Hi {names[2]}')

# Nested List
number =[10,34,90,[45,78,-3],89]
length = len(number)

#print(length)
# print(number[-2])

print(number[3][::2])
