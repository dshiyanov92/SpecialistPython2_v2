class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = self.get_distance()
        
    def get_distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
max_distance = max(point.distance for point in points)
 
for point in points:
    if point.distance ==  max_distance:
        print("Координаты наиболее удаленной точки = ", point.x, point.y)
# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты


