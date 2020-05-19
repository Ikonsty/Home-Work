from pprint import pprint
import matplotlib.pyplot as plt
from point import Point
from graph import Graph
from math import atan, degrees


def read_letter_keys_file(filename):
    """
    str -> dict
    Read file by filename where letter keys are and make a dictionary
    {Letter : coordinate}
    """
    keys = {}

    lk_file = open(filename, 'r')
    data = lk_file.readlines()
    for ln in data:
        l1 = ln.rstrip().split(" ")
        cord = l1[1].split(",")
        tup_l = int(cord[0][1:])
        tup_r = int(cord[1][:-1])
        keys[l1[0]] = (int(tup_l), int(tup_r))
    return keys


def read_file_data(filename):
    """
    str -> str
    Read the txt file and return string with content of it
    """
    f = open(filename, 'r')
    fl_data = f.readlines()
    data = ''
    for ln in fl_data:
        l1 = ln.rstrip().split(" ")
        data += ' '.join(l1) + ' '
    return data


def message_to_points(message, keys):
    """
    str, dict -> lst[lst]
    Translate message into list of points for making graph.
    Function use dictionary of letter keys.
    """
    points = []
    word_point = []
    sentence = message.split(" ")

    for word in sentence:
        for let in word:
            if let not in keys:
                continue
            word_point.append(keys[let])
        if len(word_point) > 0:
            points.append(word_point)
        word_point = []
    return points


def create_related_points(points, key_symbol):
    """
    lst, int -> lst
    Return list of point where each coordinates are related to
    coordinates the point before.
    Also rotate every point on angle _alpha relative to the privious one.
    """
    all_points = []
    let_angle = 0
    start_point = (0, 0)
    _alpha = key_symbol[2]

    for word in points:
        related_points = [start_point]
        i = 0
        for p in word:
            x = p[0] + related_points[i][0]
            y = p[1] + related_points[i][1]
            point1 = Point(x, y)
            point2 = Point(related_points[i][0], related_points[i][1])
            point1.rotate(let_angle, point2)
            related_points.append(tuple(point1.listing()))

            try:
                diff = (y - related_points[i][1]) / (x - related_points[i][0])
                let_angle += degrees(atan(diff))
            except ZeroDivisionError:
                let_angle += 0

            i += 1

        all_points.append(related_points)
        let_angle += _alpha
        last_point = Point(related_points[-1][0], related_points[-1][1])
        start_point = Point(related_points[-1][0] + word[-1][0] + key_symbol[0], related_points[-1][1] + word[-1][1] + key_symbol[1])
        start_point.rotate(let_angle, last_point)
        start_point = tuple(start_point.listing())

    return all_points


def main():
    keys = read_letter_keys_file('letter_key.txt')

    print("This program will convert your text into Graph")
    print("Do you want to chose text file or write by yourself instead?")
    print("-file")
    print("-text")
    choise = input("Your choise: ")

    while True:
        if choise == "file":
            filename = input("Give the name of file: ")
            try:
                text = read_file_data(filename)
            except FileNotFoundError:
                print("File does not exist")
                continue
            break

        elif choise == "text":
            massege = input("Give text to convertation: ")
            text = ' '.join(massege.split())
            break

        print()
        print("You need to write 'file' or 'text'")
        print("-file")
        print("-text")
        choise = input("Your choise: ")

    print()
    print("Do you want to see graph or dawnload png?")
    print("-window")
    print("-file")
    choise = input("Your choise: ")
    while True:
        points = message_to_points(text, keys)
        points = create_related_points(points, (0, 0, 0))
        chiper_graph = Graph(points)

        if choise == "window":
            chiper_graph.draw()
            break
        elif choise == "file":
            filename = input("Give a filename: ")
            filename += ".png"
            chiper_graph.save(filename)
            print("Your file was created")
            break
        print()
        print("Do you want to see graph or dawnload png?")
        print("-window")
        print("-file")
        choise = input("Your choise: ")
    print("Thanks for using this program!")

if __name__ == "__main__":
    main()
