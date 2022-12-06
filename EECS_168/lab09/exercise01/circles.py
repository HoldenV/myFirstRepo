#circles.py

from math import pi

class Circle:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.rad = 1
    def diameter(self):
        return self.rad*2

    def area(self):
        return (self.rad**2)*pi

    def circum(self):
        return 2*pi*self.rad

    def orginDist(self):
        return ((self.xpos**2)+(self.ypos**2))**1/2

    def inter(self, otherCircle):
        return self.rad - otherCircle.rad < (((self.xpos-otherCircle.xpos)**2)+((self.ypos-otherCircle.ypos)**2))**1/2 < self.rad + otherCircle.rad
