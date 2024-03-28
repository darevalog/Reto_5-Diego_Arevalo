class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_distance(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5