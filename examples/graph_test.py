import sys
sys.path.append('/home/ilya/Документи/UCU/CS/CourseWork/')
from modules.graph import Graph

words = [[(0, 0), (4, 3)], [(5, 8), (5, 9), (4, 11)], [(2, 13), (-7, 21), (-12, 16), (-12, 15), (-2, 12), (6, 11), (10, 13), (9, 21), (-1, 22), (-6, 13)], [(-1, 4), (3, -2), (8, -4), (16, -6), (27, 2)], [(28, 15), (31, 19), (34, 24), (27, 31)]]
g1 = Graph(words)
g1.draw()
g1.save('test_graph')
# print(g1[(0, 1)])
