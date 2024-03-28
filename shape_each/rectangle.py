from shape_each.gen_shape import *
from shape_each.point import *
from shape_each.line import *

class rectangle(shape):
    def __init__(self, width, height, center):
        self.width = width
        self.height = height
        self.center = center
        self.is_regular = True

    def vertices(self):
        point1 = point(self.center.x - self.width/2, self.center.y - self.height/2)  
        point2 = point(self.center.x + self.width/2, self.center.y - self.height/2)
        point3 = point(self.center.x + self.width/2, self.center.y + self.height/2)
        point4 = point(self.center.x - self.width/2, self.center.y + self.height/2)
        print(f"Vertices (points): {point1.x, point1.y}, {point2.x, point2.y}, {point3.x, point3.y}, {point4.x, point4.y}")

    def edges(self):
        edge1 = line(point(self.center.x - self.width/2, self.center.y - self.height/2), point(self.center.x + self.width/2, self.center.y - self.height/2), self.width)
        edge2 = line(point(self.center.x + self.width/2, self.center.y - self.height/2), point(self.center.x + self.width/2, self.center.y + self.height/2), self.height)
        edge3 = line(point(self.center.x + self.width/2, self.center.y + self.height/2), point(self.center.x - self.width/2, self.center.y + self.height/2), self.width)
        edge4 = line(point(self.center.x - self.width/2, self.center.y + self.height/2), point(self.center.x - self.width/2, self.center.y - self.height/2), self.height)
        print(f"Edges (lengths): {(edge1.length, edge2.length), (edge2.length, edge3.length), (edge3.length, edge4.length), (edge4.length, edge1.length)}")

    def compute_area(self):
        return round(self.width * self.height, 2)

    def compute_perimeter(self):
        return round(2 * self.width + 2 * self.height, 2)

    def compute_inner_angle(self):
        return 90, 90, 90, 90
    