# def greet(name, subject, dept = "CS"):
#     print(f'Hi {name}')
#     print(f'Do you teach {subject}')
#     print(f"Are you from {dept} department?")
#
# greet ('jenny', subject="English)")

# Arbitrary

def add(*numbers):
    c =0
    for i in numbers:
       c=c+i
    print(f"sum is {c}")
add(4,5,6,90)