from .point import Point
from .triangle import Triangle
from numpy import cos, sin, pi, fromfunction

class Triangulation:

    def __init__(self, h=1, R=5, N=50):
        # h-высота конуса, R-радиус, N-кол-во сегментов (треугольников)
        self._h = h
        self._R = R
        self._N = N
        self.A = Point(0, 0, h)
        self.B = Point(0, 0, -R**2/h)
        self.multiplier = 2 * pi / N
        self.A_norm = Point(0, 0, 1)

    @property
    def h(self):
        return self._h
    
    @h.setter
    def h(self, h):
        if h > 0: 
            self._h = h
            self.A.z = h
    
    @property
    def R(self):
        return self._R
    
    @R.setter
    def R(self, R):
        if R > 0: self._R = R
    
    @property
    def N(self):
        return self._N
    
    @N.setter
    def N(self, N):
        if N > 0: self._N = N

    def calculate_vertexes(self):
        array = fromfunction(lambda i: self.multiplier * i, (self.N,))
        x = self.R * cos(array)
        y = self.R * sin(array)
        del array
        
        self.triangles = []
        self.normals = []
        point_start = point_next = Point(x[0], y[0])
        
        ni_start = ni_next = Point.calculate_normal(point_start, self.B)
        for i in range(self.N):
            point_cur = point_next
            point_next = Point(x[j := (i+1)%self.N], y[j]) if i != self.N - 1 else point_start
            self.triangles.append(Triangle(point_cur, point_next, self.A))

            # Нормалью для A считаем [0, 0, 1]
            ni_cur = ni_next
            ni_next = Point.calculate_normal(point_next, self.B) if i != self.N - 1 else ni_start
            self.normals.append(Triangle(ni_cur, ni_next, self.A_norm))

    def verify(self):
        # Проверка, что треугольники разделяют (не дублируют) точки между собой
        print(all([self.triangles[i].p2 is self.triangles[(i+1)%self.N].p1 for i in range(self.N)]))
    
    def print(self):
        print(*self.triangles, sep='\n')

    def get_points(self):
        # Сервер должен передавать данные клиенту о треугольниках 
        triangle_points = []
        normals_points = []
        for triangle, normal in zip(self.triangles, self.normals):
            triangle_points += triangle.get_xyz()
            normals_points += normal.get_xyz()

        return triangle_points, normals_points