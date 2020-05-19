# import sys
# sys.path.append('../CourseWork/')
from modules.point import Point

point1 = Point(4, 12)
point2 = Point(1, 1)
point1.rotate(0, point2)
print(str(point1))
