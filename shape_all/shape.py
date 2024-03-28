import math
import os

os.system("cls")

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_distance(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
    
class line(point):
    def __init__(self, start_point, end_point, length):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length

class shape:
    def __init__(self, is_regular):
        self.is_regular = is_regular

    def vertices(self):
        pass

    def edges(self):
        pass

    def inner_angle(self):
        pass

    def compute_area(self):
        pass
        
    def compute_perimeter(self):
        pass

    def compute_inner_angle(self):
        pass

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

class triangle(shape):
    def __init__(self, is_regular):
        self.is_regular = is_regular

    def vertices(self):
        return 3

    def edges(self):
        return 3

    def inner_angle(self):
        pass
    
class isoceles(triangle):
    def __init__(self, side1, side2, center):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side2
        self.center = center
        self.is_regular = False

    def vertices(self):
        point1 = point(self.center.x, self.center.y + self.side1)
        point2 = point(self.center.x - self.side2/2, self.center.y - self.side1/2)
        point3 = point(self.center.x + self.side2/2, self.center.y - self.side1/2)
        print(f"Vertices (points): {point1.x, point1.y}, {point2.x, point2.y}, {point3.x, point3.y}")
    
    def edges(self):
        edge1 = line(point(self.center.x, self.center.y + self.side1), point(self.center.x - self.side2/2, self.center.y - self.side1/2), self.side1)
        edge2 = line(point(self.center.x - self.side2/2, self.center.y - self.side1/2), point(self.center.x + self.side2/2, self.center.y - self.side1/2), self.side2)
        edge3 = line(point(self.center.x + self.side2/2, self.center.y - self.side1/2), point(self.center.x, self.center.y + self.side1), self.side1)
        print(f"Edges (lengths): {(edge1.length, edge2.length), (edge2.length, edge3.length), (edge3.length, edge1.length)}")
    
    def compute_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return round(math.sqrt(s * (s - self.side1) * (s - self.side2)), 2)

    def compute_perimeter(self):
        return round(2 * self.side1 + self.side2, 2)

    def compute_inner_angle(self):
        angle1 = round(math.degrees(math.acos((self.side1**2 + self.side2**2 - self.side3**2)/(2 * self.side1 * self.side2))), 2)
        angle2 = angle1
        angle3 = 180 - 2 * angle1
        return angle1, angle2, angle3
    
class equilateral(triangle):
    def __init__(self, side, center):
        self.side = side
        self.center = center
        self.is_regular = True

    def vertices(self):
        point1 = point(self.center.x, self.center.y + self.side)
        point2 = point(self.center.x - self.side/2, self.center.y)
        point3 = point(self.center.x + self.side/2, self.center.y)
        print(f"Vertices (points): {point1.x, point1.y}, {point2.x, point2.y}, {point3.x, point3.y}")
    
    def edges(self):
        edge1 = line(point(self.center.x, self.center.y + self.side), point(self.center.x - self.side/2, self.center.y), self.side)
        edge2 = line(point(self.center.x - self.side/2, self.center.y), point(self.center.x + self.side/2, self.center.y), self.side)
        edge3 = line(point(self.center.x + self.side/2, self.center.y), point(self.center.x, self.center.y + self.side), self.side)
        print(f"Edges (lengths): {(edge1.length, edge2.length), (edge2.length, edge3.length), (edge3.length, edge1.length)}")
    
    def compute_area(self):
        s = self.compute_perimeter() / 2
        return round(math.sqrt(s * (s - self.side) * (s - self.side) * (s - self.side)), 2)

    def compute_perimeter(self):
        return round(3 * self.side, 2)

    def compute_inner_angle(self):
        return 60, 60, 60
    
class scalene(triangle):
    def __init__(self, side1, side2, side3, center):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.center = center
        self.is_regular = False

    def vertices(self):
        point1 = point(self.center.x, self.center.y + self.side1)
        point2 = point(self.center.x - self.side2/2, self.center.y - self.side1/2)
        point3 = point(self.center.x + self.side2/2, self.center.y - self.side1/2)
        print(f"Vertices (points): {point1.x, point1.y}, {point2.x, point2.y}, {point3.x, point3.y}")
    
    def edges(self):
        edge1 = line(point(self.center.x, self.center.y + self.side1), point(self.center.x - self.side2/2, self.center.y - self.side1/2), self.side1)
        edge2 = line(point(self.center.x - self.side2/2, self.center.y - self.side1/2), point(self.center.x + self.side2/2, self.center.y - self.side1/2), self.side2)
        edge3 = line(point(self.center.x + self.side2/2, self.center.y - self.side1/2), point(self.center.x, self.center.y + self.side1), self.side1)
        print(f"Edges (lengths): {(edge1.length, edge2.length), (edge2.length, edge3.length), (edge3.length, edge1.length)}")
    
    def compute_area(self):
        s = self.compute_perimeter() / 2
        return round(math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)), 2)

    def compute_perimeter(self):
        return round(self.side1 + self.side2 + self.side3, 2)

    def compute_inner_angle(self):
        angle1 = round(math.degrees(math.acos((self.side1**2 - self.side2**2 + self.side3**2)/(2 * self.side1 * self.side3))), 2)
        angle2 = round(math.degrees(math.acos((self.side2**2 - self.side1**2 + self.side3**2)/(2 * self.side2 * self.side3))), 2)
        angle3 = 180 - angle1 - angle2
        return angle1, angle2, angle3
    
class TriRectangle(triangle):
    def __init__(self, opposite, adjacent, hypotenuse, center):
        self.opposite = opposite
        self.adjacent = adjacent
        self.hypotenuse = hypotenuse
        self.center = center   
        self.is_regular = False

    def vertices(self):
        point1 = point(self.center.x, self.center.y + self.opposite)
        point2 = point(self.center.x - self.adjacent/2, self.center.y - self.opposite/2)
        point3 = point(self.center.x + self.adjacent/2, self.center.y - self.opposite/2)
        print(f"Vertices (points): {point1.x, point1.y}, {point2.x, point2.y}, {point3.x, point3.y}")
    
    def edges(self):
        edge1 = line(point(self.center.x, self.center.y + self.opposite), point(self.center.x - self.adjacent/2, self.center.y - self.opposite/2), self.opposite)
        edge2 = line(point(self.center.x - self.adjacent/2, self.center.y - self.opposite/2), point(self.center.x + self.adjacent/2, self.center.y - self.opposite/2), self.adjacent)
        edge3 = line(point(self.center.x + self.adjacent/2, self.center.y - self.opposite/2), point(self.center.x, self.center.y + self.opposite), self.hypotenuse)
        print(f"Edges (lengths  ): {(edge1.length, edge2.length), (edge2.length, edge3.length), (edge3.length, edge1.length)}")
    
    def compute_area(self):
        return round(0.5 * self.opposite * self.adjacent, 2)

    def compute_perimeter(self):
        return round(self.opposite + self.adjacent + self.hypotenuse, 2)
    
    def compute_inner_angle(self):
        angle1 = round(math.degrees(math.acos(self.opposite/self.hypotenuse)), 2)
        angle2 = round(math.degrees(math.acos(self.adjacent/self.hypotenuse)), 2)
        angle3 = 90
        return angle1, angle2, angle3
