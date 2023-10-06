from .point import Point

class Triangle:

    def __init__(self, p1=Point(0, 0), p2=Point(0, 1), p3 = Point(1, 0)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __str__(self):
        return f'Triangle(p1{self.p1}, p2{self.p2}, p3{self.p3})'

    def get_xyz(self):
        return self.p1.xyz() + self.p2.xyz() + self.p3.xyz()