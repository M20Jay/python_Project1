import math
def paint_calculation (height,width,cover):
    area = height*width
    no_of_cans=math.ceil(area/cover)


    print(f"You will need {no_of_cans} of paints")

h=int(input(" Enter the height of wall in meter:\n"))
w=int(input(" Enter the width of wall in meter:\n"))
coverage = 7

paint_calculation(width=w,height=h, cover=coverage)