from point import Point


class Space:
    def __init__(self, points: [Point]):
        self.points = points
        self.x = []
        self.y = []

    def initial_limits(self):
        x, y = [], []
        for point in self.points:
            x.append(point.x)
            y.append(point.y)

        self.x.append(min(x))
        self.x.append(max(x))
        self.y.append(min(y))
        self.y.append(max(y))
