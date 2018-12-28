import math

try:
     R = float(input("Enter value of R: \n"))
     L = float(input("Enter value of L: \n"))
     E = float(input("Enter value of E: \n"))
     C = float(input("Enter value of C: \n"))
     w = float(input("Enter value of \u03C9: \n"))
except ValueError:
     print("Invalid entry, please enter a valid Number")


G = E/((R**2 + ((2 * math.pi * w * L) - (2 * math.pi * w * C)**-1)**2)**0.5)

print ('value of G is %.3f' %G)

