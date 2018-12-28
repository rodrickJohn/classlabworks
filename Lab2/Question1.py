

class BasicTwoIntegerOperations:  #Define a blueprint object for the problem

    try:
        x = int(input("Enter Number 1: \n"))  #input function returns a string therefore we are typecasting explicitly
        y = int(input("Enter Number 2: \n"))
    except ValueError:
        print ("Invalid entry, please enter a valid Number")

    def sum(self):
        return self.x + self.y

    def difference(self):
       return self.x - self.y

    def product(self):
        return self.x * self.y

    def quotient(self):
        return self.x//self.y


opi=BasicTwoIntegerOperations()

print("Sum is: ", opi.sum())
print("Product is: ", opi.product())
print("Difference: ", opi.difference())
print("Quotient is: ", opi.quotient())

