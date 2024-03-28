from shape_each.rectangle import *
from shape_each.point import *

class square(rectangle):
    def __init__(self, side, center):
        self.side = side
        self.center = center
        self.is_regular = True
        
    def vertices(self):
        point1 = point(self.center.x - self.side/2, self.center.y - self.side/2)  
        point2 = point(self.center.x + self.side/2, self.center.y - self.side/2)
        point3 = point(self.center.x + self.side/2, self.center.y + self.side/2)
        point4 = point(self.center.x - self.side/2, self.center.y + self.side/2)
        print(f"Vertices (points): {point1.x, point1.y}, {point2.x, point2.y}, {point3.x, point3.y}, {point4.x, point4.y}")
    
    def edges(self):
        edge1 = line(point(self.center.x - self.side/2, self.center.y - self.side/2), point(self.center.x + self.side/2, self.center.y - self.side/2), self.side)
        edge2 = line(point(self.center.x + self.side/2, self.center.y - self.side/2), point(self.center.x + self.side/2, self.center.y + self.side/2), self.side)
        edge3 = line(point(self.center.x + self.side/2, self.center.y + self.side/2), point(self.center.x - self.side/2, self.center.y + self.side/2), self.side)
        edge4 = line(point(self.center.x - self.side/2, self.center.y + self.side/2), point(self.center.x - self.side/2, self.center.y - self.side/2), self.side)
        print(f"Edges (lengths): {(edge1.length, edge2.length), (edge2.length, edge3.length), (edge3.length, edge4.length), (edge4.length, edge1.length)}")
    
    def compute_area(self):
        return round(self.side**2, 2)

    def compute_perimeter(self):
        return round(4 * self.side, 2)

    def compute_inner_angle(self):
        return 90, 90, 90, 90
