
import math

class Circle:  #Define a circle object

    try:
        r = float(input("Enter Radius: \n")) #radius is a real number
    except ValueError:
        print ("Invalid entry, please enter a valid Number")

    def diameter(self):
        return 2 * self.r

    def area(self):
       return math.pi * self.r * self.r

    def circumference(self):
        return 2 * math.pi * self.r


circle = Circle()

print("Entered radius is: %.2f" %circle.r)
print("Diameter is: %.2f" %circle.diameter())
print("Circumference is: %.2f" %circle.circumference())
print("Area is: %.2f" %circle.area())