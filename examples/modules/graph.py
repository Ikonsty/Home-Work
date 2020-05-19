from arrays import Array2D
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, _list=[[]]):
        """
        type(_list) = list[lists]
        Giving a list of lists of tuples and initialize a graph
        Each inside list represent one word
        """
        word_len = []
        for word in _list:
            for p in word:
                if type(p) != tuple or len(p) != 2:
                    raise TypeError("List must contains only points")
            word_len.append(len(word))

        self.graph_lst = _list
        len_rows = len(_list)
        len_cols = max(word_len)
        self.graph = Array2D(len_rows, len_cols)
        for r in range(len(_list)):
            for c in range(len(_list[r])):
                self.graph[(r, c)] = _list[r][c]

    def __getitem__(self, index_tuple):
        """
        Get item from graph
        """
        return self.graph[index_tuple]

    def __setitem__(self, index_tuple, value):
        """
        Set the contents of the element at position [i,j] to value
        """
        self.graph[index_tuple] = value

    def draw(self):
        """
        This method draws a graph with matplotlib
        """
        xlim_max = max([find_max(0, self.graph), 0])
        xlim_min = min([find_min(0, self.graph), 0])
        ylim_max = max([find_max(1, self.graph), 0])
        ylim_min = min([find_min(1, self.graph), 0])

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
        for i in range(self.graph.num_rows()):
            x1, y1 = [], []
            for j in range(self.graph.num_cols()):
                if self.graph[(i, j)]:
                    x1.append(self.graph[(i, j)][0])
                    y1.append(self.graph[(i, j)][1])

            plt.plot(x1, y1, 'b', marker='o')
        plt.show()

    def save(self, filename):
        """
        Save graph in file named filename
        """
        xlim_max = max([find_max(0, self.graph), 0])
        xlim_min = min([find_min(0, self.graph), 0])
        ylim_max = max([find_max(1, self.graph), 0])
        ylim_min = min([find_min(1, self.graph), 0])

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
        for i in range(self.graph.num_rows()):
            x1, y1 = [], []
            for j in range(self.graph.num_cols()):
                if self.graph[(i, j)]:
                    x1.append(self.graph[(i, j)][0])
                    y1.append(self.graph[(i, j)][1])

            plt.plot(x1, y1, 'b', marker='o')
        plt.savefig(filename, dpi=300)


def find_max(pos, lst):
    """
    lst[lst] -> int
    Find max in list of lists
    """
    try:
        all_pos = []  # All numbers in tuples with this pos
        for i in range(lst.num_rows()):
            for j in range(lst.num_cols()):
                if lst[(i, j)]:
                    all_pos.append(lst[(i, j)][pos])
        return max(all_pos)
    except IndexError:
        raise IndexError('Not list in list')


def find_min(pos, lst):
    """
    lst -> int
    Find min in list of lists
    """
    try:
        all_pos = []  # All numbers in tuples with this pos
        for i in range(lst.num_rows()):
            for j in range(lst.num_cols()):
                if lst[(i, j)]:
                    all_pos.append(lst[(i, j)][pos])
        return min(all_pos)
    except IndexError:
        raise IndexError('Not list in list')
