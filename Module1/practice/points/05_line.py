class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist_to(self, other_point):
  return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]
l = 0
i=0
j=i+1
for Point in points:
    dist = dist_to(points[i], points[j])
l += dist


# TODO: Найдите длину ломаной линии

print("Длина ломаной линии = ", l)
