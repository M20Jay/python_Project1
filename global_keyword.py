# # a = 10
# def display():
#     a =20
#     def show():
#         global a
#         a = 30
#     print(a)
#     show()
#     print(a)
# display()
# print(a)

name = "Jenny's"

def display():
    global name
    name = name + " Lectures"
print(name)
display()
print(name)