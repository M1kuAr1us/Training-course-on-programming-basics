import math

class Circle:
    def __init__(self, radius=1.0, color='red'):
        self.__radius = radius
        self.__color = color

    def get_radius(self):
        return self.__radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_color(self):
        return self.__color

circle_default = Circle()
print(circle_default.get_radius())
print(circle_default.get_color())
print(circle_default.get_area())
print("\n")

circle_user = Circle(2.5, 'green')
print(circle_user.get_radius())
print(circle_user.get_color())
print(circle_user.get_area())