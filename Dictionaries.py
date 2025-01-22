import enum

phone_no = {'Ram': 1234,
            'Shym':3456,
            "Mohan":8976
            }

# print(phone_no['Shym'])

# Phone_no=dict([('Ram',1234),('Shyam',3456),('Mohan',8976)])
# print(Phone_no)

phone_no['Madhav'] =[1111,2222,3333]
phone_no['Shym'] ={'Shym_home':5555,'Shym_work':7777}
# print(phone_no['Shym']['Shym_home'])
# print(phone_no.get("Madhav"))

data ={
    1:'Jenny',
    2:'Ram',
    0:'Mohan'
}
# print(data[0])

# Deleting items from a dictionary
del phone_no['Ram']

# print(phone_no)

# print(phone_no.pop('Shym'))
# print(phone_no)

# print(phone_no.popitem())
# print(phone_no)
#
# print(phone_no.keys())
# print(phone_no.values())
# print(phone_no.items())

# for i in phone_no.items():
#     print(i)

phone_no2= phone_no.copy()
print(phone_no2)
print(len(phone_no2))