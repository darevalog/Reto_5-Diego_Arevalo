from shape_each.point import *

class line(point):
    def __init__(self, start_point, end_point, length):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length