import math
import sys


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle
        Formula: pi * radius squared
        :return: value of the area of circle
        """
        return math.pi * self.radius**2

    def perimeter(self):
        """
        Calculates the perimeter of the circle
        Formula: 2 * pi * r
        :return: value of the perimeter of the circle
        """
        return 2 * math.pi * self.radius


if len(sys.argv) > 1:
    radius = int(sys.argv[1])
    circle_object = Circle(radius)
    print('Radius is {}'.format(radius))
    print('Area of circle: {}'.format(circle_object.area()))
    print('Perimeter of circle: {}'.format(circle_object.perimeter()))
else:
    circle_object = Circle(8)
    print('Radius is 8')
    print('Area of circle: {}'.format(circle_object.area()))
    print('Perimeter of circle: {}'.format(circle_object.perimeter()))
