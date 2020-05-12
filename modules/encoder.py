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

    lk_file = open(filename,'r')
    data = lk_file.readlines()
    for ln in data:
        l1 = ln.rstrip().split(" ")
        cord = l1[1].split(",")
        tup_l = int(cord[0][1:])
        tup_r = int(cord[1][:-1])
        keys[l1[0]] = (int(tup_l), int(tup_r))
    return keys

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
        points.append(word_point)
        word_point = []
    return points

def create_related_points(points, key_symbol):
    """
    lst, int -> lst
    Return list of point where each coordinates are related to coordinates the point before.
    Also rotate every point on angle _alpha relative to the privious one.
    """
    all_points = []
    let_angle = 0
    start_point = (0, 0)
    _alpha = key_symbol[2]

    for word in points:
        related_points = [start_point]
        i = 0
        # angle = _alpha
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
            # angle += _alpha
            print(let_angle)

        all_points.append(related_points)

        last_point = Point(related_points[-1][0], related_points[-1][1])
        start_point = Point(related_points[-1][0] + word[-1][0], related_points[-1][1] + word[-1][1])
        start_point.rotate(let_angle, last_point)
        start_point = tuple(start_point.listing())

        # try:
        #     diff = (y - related_points[i][1]) / (x - related_points[i][0])
        #     let_angle += degrees(atan(diff))
        # except ZeroDivisionError:
        #     let_angle += 0

        # angle += _alpha
    return all_points

def main():
    keys = read_letter_keys_file('letter_key_part2.txt')
    text = """I stare, at the girl in the mirror
    T-shirt, torn up jeans, no beauty queen
    But the way that you see me
    You get underneath me
    And all my defenses
    Just fall away, fall away

    I am beautiful with you
    Even in the darkest part of me
    I am beautiful with you
    You make it feel the way it's supposed to be
    You're here with me
    Just show me this and I believe
    I am beautiful with you

    I stand naked before you now
    No walls to hide behind, so here am I
    You see all of my scars
    Still here you are
    I bare my soul
    And I'm not afraid, not afraid

    I am beautiful with you
    Even in the darkest part of me
    I am beautiful with you
    You make it feel the way it's supposed to be
    You're here with me
    You show me this and I believe
    I am beautiful with you

    I've been the strong one for so long
    But I was wrong
    Doesn't make you weak if you're needing someone
    I'm not holding back (yeah)
    I know what I want

    I am beautiful with you
    I am beautiful with you
    You want me for myself
    You get me like no one else
    I am beautiful with you

    I am beautiful with you
    Even in the darkest part of me
    I am beautiful with you
    You make it feel the way it's supposed to be
    You're here with me
    You show me this and I believe
    That I am beautiful with you"""

    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("     ", " ")
    ' '.join(text.split())
    # print(text)
    points = message_to_points(text, keys)
    print(points)
    print()
    points = create_related_points(points, (3, 3, 0))
    print(points)
    chiper_graph = Graph(points)
    chiper_graph.draw()

if __name__ == "__main__":
    main()
