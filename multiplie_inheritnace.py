class Human:
    def __init__(self,num_heart):
        self.num_eyes = 2
        self.num_noses = 1
        self.num_heart = num_heart

    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male:
    def __init__(self, name):
        self.name = name
    def flirt(self):
       print("I can flirt")
    def work(self):
       print("I can code")

class Boy(Human,Male):
    def __init__(self, name,heart, language):
       Human.__init__(self,heart)
       Male.__init__(self, name)
       self.language = language
    def work(self):
       print("I can test")
    def display(self):
        print(f'Hi, I am {self.name}, and I have work on {self.language}.')

boy_1 = Boy("Rahul",1, "Python")
print(boy_1.num_noses)
print(boy_1.num_heart)
print(boy_1.language)
boy_1.display()