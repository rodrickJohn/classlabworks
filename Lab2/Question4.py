import math

class FourVariableOperations:

    x=math.cos(math.pi/5)
    y=92
    z=0.78
    m=45

    def compute_g(self):
        g = 2 * ((self.x + self.y + self.z + self.m) ** 0.5)
        return g

    def compute_n(self):
        n = 3 + (((self.y + self.m) / 2) ** (1 / 3))
        return n

    def min_max(self):
        min4 = min(self.x, self.y, self.z, self.m)
        max4 = max(self.x, self.y, self.z, self.m)
        return min4, max4

co=FourVariableOperations()
print ("The value of g is: %.3f "%co.compute_g())
print ("The value of n is: %.3f " %co.compute_n())
print ("Minimum and Maximum values are respectively: ", co.min_max())