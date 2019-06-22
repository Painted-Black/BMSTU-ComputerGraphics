from Point import *
from sympy import *
from PyQt5.QtCore import QPoint

class Circle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        self.center = self.center(p1, p2, p3)
        self.radius = self.rad(self.center, self.point1)

    def __center(self, p1, p2, p3):
        h, k, r = symbols('h k r')
        eq1 = (p1.x() - h) ** 2 + (p1.y() - k) ** 2 - r ** 2
        eq2 = (p2.x() - h) ** 2 + (p2.y() - k) ** 2 - r ** 2
        eq3 = (p3.x() - h) ** 2 + (p3.y() - k) ** 2 - r ** 2
        solve([eq1, eq2, eq3], h, k, r)
        print(h, k, r)

    def rad(self, center, p):
        pass

    def tangent(self, circle):
        pass