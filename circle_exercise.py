class Circle:
    pi = 3.14159265359
    def __init__(self, radius =6):
        self.radius = radius
        self.area = Circle.pi * radius ** 2.
    def get_circumference(self):
       return 2 * self.pi*self.radius

    def get_area(self, radius):
        return self.pi * self.radius ** 2


circle_1 = Circle(4)
print(circle_1.get_circumference())
circle_2 = Circle(14)
print(circle_2.get_circumference())
print(circle_1.area)