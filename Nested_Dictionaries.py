# student_data ={
#     "Ram":{"roll_no": 10, "age": 20, "course":"Python"},
#     "Mohan":{"roll_no": 20, "age": 22, "course":"Java"}
#  }

# Accessing Mohan details
# print(student_data["Mohan"])

# Accessing Mohan's roll_no

# print(student_data["Mohan"]["roll_no"])

# Adding data
# student_data["Mohan"]["phone_no"]=98786
# print(student_data["Mohan"])

# #Deleting from nested dictionaries
# # del student_data ["Mohan"]["phone_no"]
#
# # Popping from nested dictionaries
# print(student_data["Mohan"].pop("phone_no"))
# print(student_data["Mohan"])

# # Nesting a list within a dictionary
# travel_data = {
#     'Kenya': ["Nairobi",'Nyeri',"Eldoret","Nakuru"],
#     "Uganda":['Entebe']
# }
#
# print(travel_data)
#
# # Accesing the values of Kenya
# print(travel_data["Kenya"])

# Nesting a dictionary within a list
student_data =[
    {"Name": "Ram", "roll_no": 10, "age": 20, "course":"Python"},
    {"Name":"Mohan", "roll_no": 20, "age": 22, "course":"Java"}
]

# we use indexing to access values in a list. In dictionaries, we use keys
print(student_data[1])


