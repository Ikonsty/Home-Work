import sys
sys.path.append('/home/ilya/Документи/UCU/CS/CourseWork/')
from modules.point import Point
from modules.arrays import Array2D
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, _list=[]):
        """
        type(_list) = list[lists]
        Giving a list of lists of tuples and initialize a graph
        Each inside list represent one word
        """
        for word in _list:
            for p in word:
                if type(p) != tuple or len(p) != 2:
                    raise TypeError("List must contains only points")
        self.graph = _list

    def draw(self):
        """
        This method draws a graph with matplotlib
        """
        all_points = self.graph
        xlim_max = max([find_max(0, all_points), 0])
        xlim_min = min([find_min(0, all_points), 0])
        ylim_max = max([find_max(1, all_points), 0])
        ylim_min = min([find_min(1, all_points), 0])

        # Add some parameters to make graph in center of picture
        plt.xlim(xlim_min - 1, xlim_max + 2)
        plt.ylim(ylim_min - 1, ylim_max + 2)
        plt.gca().set_aspect('equal', adjustable='box')

        # Add list with steps on axes to see coordinates of points
        x_steps = []
        y_steps = []
        for i in range(xlim_min - 1, xlim_max + 2):
            x_steps.append(i)
        for i in range(ylim_min - 1, ylim_max + 2):
            y_steps.append(i)

        plt.xticks(x_steps)
        plt.yticks(y_steps)

        start_x = 0
        start_y = 0
        for points in all_points:
            x1, y1 = [], []
            for p in points:
                x1.append(p[0])
                y1.append(p[1])

            plt.plot(x1, y1, 'b', marker='o')
        plt.show()

    def save(self, filename):
        """
        Save graph in file named filename
        """
        all_points = self.graph
        xlim_max = max([find_max(0, all_points), 0])
        xlim_min = min([find_min(0, all_points), 0])
        ylim_max = max([find_max(1, all_points), 0])
        ylim_min = min([find_min(1, all_points), 0])

        # Add some parameters to make graph in center of picture
        plt.xlim(xlim_min - 1, xlim_max + 2)
        plt.ylim(ylim_min - 1, ylim_max + 2)
        plt.gca().set_aspect('equal', adjustable='box')

        # Add list with steps on axes to see coordinates of points
        x_steps = []
        y_steps = []
        for i in range(xlim_min - 1, xlim_max + 2):
            x_steps.append(i)
        for i in range(ylim_min - 1, ylim_max + 2):
            y_steps.append(i)

        plt.xticks(x_steps)
        plt.yticks(y_steps)

        start_x = 0
        start_y = 0
        for points in all_points:
            x1, y1 = [], []
            for p in points:
                x1.append(p[0])
                y1.append(p[1])

            plt.plot(x1, y1, 'b', marker='o')
        plt.savefig(filename)

def find_max(pos, lst):
    """
    lst[lst] -> int
    Find max in list of lists
    """
    try:
        all_pos = [] # All numbers in tuples with this pos
        for part in lst:
            for p in part:
                all_pos.append(p[pos])
        return max(all_pos)
    except IndexError:
        raise IndexError('Not list in list')

def find_min(pos, lst):
    """
    lst -> int
    Find min in list of lists
    """
    try:
        all_pos = [] # All numbers in tuples with this pos
        for part in lst:
            for p in part:
                all_pos.append(p[pos])
        return min(all_pos)
    except IndexError:
        raise IndexError('Not list in list')
