## Author: Feras
## Description: Findin area of a circle using math.pi

import math
def areaOfCircle():
    radius = float(input("Enter a radius of a circle: "))
    area = math.pi * radius ** 2
    print("Area of the circle is: " + str(area))
areaOfCircle()