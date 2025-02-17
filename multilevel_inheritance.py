class Human:
    can_breath = True
    def __init__(self, num_heart):
        print("calling init from Human class")
        self.eyes = 2
        self.heart = num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self, name):
        self.name =name
    def sleep(self):
        print("I can sleep the whole day")
class Boy(Male):
    def __init__(self, heart, name, can_dance):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.know_dancing = can_dance
    def work(self):
        # Human.work(self)
        super().work()
        print("I can code")

boy_1 = Boy(1,'Rahul', True)
print(boy_1.name)
print(boy_1.know_dancing)
print(boy_1.can_breath)
print(Boy.mro())

