class Human:
    def __init__(self, num_heart):
        self.num_eyes = 2
        self.num_noses = 1
        self.heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

#Inheritance
class Male(Human):
    def __init__(self,name, heart):
        # super().__init__()
        self.name = name
        super().__init__(heart)
    def flirt(self):
       print("I can flirt")
    def work(self):
       super().work()
       print("I can code")
    def display(self):
        print(f'Hi, I am {self.name}, and I have {self.heart} heart')

male_1 = Male("Aakash",1)
# male_1.flirt()
# male_1.work()
print(male_1.num_eyes)
print(male_1.name)
print(male_1.heart)
male_1.display()