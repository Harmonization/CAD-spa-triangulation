from Geometry.triangulation import Triangulation

# Тест работоспособности библиотеки Geometry

if __name__ == '__main__':
    cone = Triangulation(18, 17, 23)

    cone.calculate_vertexes()
    cone.print()
    cone.verify()
