class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showDetails(self):
        print(f'Hi, I am {self.name} and I am {self.age} years old')
    def eat(self):
        print("I can eat")

class Male(Human):
    def __init__(self,m_name,age, location):
        Human.__init__(self,m_name,age)
        self.location = location
    def sleep(self):
        print("I can sleep whole day")
class Female(Human):
    def __init__(self,f_name,age,can_dance):
        super().__init__(f_name,age)
        self.can_dance = can_dance
    def showDetails(self):
        Human.showDetails(self)
        print(f'know_dancing: {self.can_dance}')

    def work(self):
        print("I can code")

female_1 = Female("Jiya", 30,True)
female_1.showDetails()
print(female_1.can_dance)
# male_1 =Male("Aakash", 20, "Mumbai")
# print(male_1.location)
# # print(Male.mro())


