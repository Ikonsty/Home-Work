import sys
sys.path.append('/home/ilya/Документи/UCU/CS/CourseWork/')
from modules.point import Point

point1 = Point(4, 12)
point2 = Point(1, 1)
point1.rotate(0, point2)
print(str(point1))
