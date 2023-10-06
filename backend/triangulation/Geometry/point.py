import numpy as np

def around(number):
    # Округление числа до 3 знаков после запятой (используется для вывода)
    return np.around(number, 3)

class Point:
    
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({around(self.x)}, {around(self.y)}, {around(self.z)})'
    
    def xyz(self):
        return [self.x, self.y, self.z]
    
    @staticmethod
    def calculate_normal(point_1, point_2):
        Ni = np.array(point_1.xyz()) - np.array(point_2.xyz())
        return Point(*list(Ni / np.linalg.norm(Ni)))