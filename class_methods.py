class Instructor:
    followers = 0 # class- object variable
    def __init__(self, name, address):
        self.name =name
        self.address =address
        # self.followers =0
    # Method
    def display(self,subject_name):
        print(f'Hi, I am {self.name} and I teach {subject_name}')

    def update_followers(self,follower_name):
        self.followers+=1

instructor_1 =Instructor("Jenny","Gurgaon")
print(instructor_1.name)
instructor_1.display("Python")
instructor_1.update_followers("Payal")
print(instructor_1.followers)
instructor_2 =Instructor("Jiya","Gurgaona")
# print(instructor_2.followers)
instructor_2.update_followers("Jay")
print(instructor_2.followers)



