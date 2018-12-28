import math

factorial=1

while True:
    number = int(input("Enter value of n \n"))
    if (number>=0):
        break
    else:
        print("Number can not be negative")
if (number==0):
    print("Factorial from the program is 1")
    print("Factorial from math module ",math.factorial(number))
else:
    for i in range(1,1+number):
        factorial=factorial*i
    print("Factorial from the program is",factorial)
    print("Factorial from math module",math.factorial(number))


# OUTPUT FOR number is zero
# Enter value of n
# 0
# Factorial from the program is 1
# Factorial from math module 1

# OUTPUT FOR number is 6
# Enter value of n
# 6
# Factorial from the program is 720
# Factorial from math module 720
