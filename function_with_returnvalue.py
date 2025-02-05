# def add(a,b):
#     c= a+b
#     return c
#
# output= add(5,4)
# print(output)

# Quiz -covert the arguments into title case

def format_name(f_name, l_name):
    formatted_f_name =f_name.title()
    formatted_l_name= l_name.title()
    return f'{formatted_f_name} {formatted_l_name}'

formatted_name =format_name("Jenny",'KHATRI')
print(  formatted_name)