# def add(*args,name):
#     c=0
#     for i in args:
#         c=c+i
#     print(f"sum is {c}")
#     print(f"name is {name}")
#
#
# add(1,2, name='Jenny')
def info_person(**kwargs):
    for i,j in kwargs.items():
        print(i,j)


info_person(name="Ram",age=30,dept="CSE")
info_person(name="Shyam",dept="CSE")