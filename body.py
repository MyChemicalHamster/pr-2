from point import Point
import numpy as np


class Body:
    def __init__(self, x: float = -11, y: float = 11, side_length: float = 2, num_points: int = 200): # начальные значения центра масс
        self.x = x
        self.y = y
        self.side_length = side_length
        self.body_points = []
        self.num_points = num_points

    def add_points(self) -> list[Point]:
        points = [Point(self.x, self.y), Point(self.x, self.y + self.side_length/2),  Point(self.x - self.side_length/2, self.y + self.side_length/2), Point(self.x - self.side_length/2, self.y)]
        for i in range(self.num_points):
            x = np.random.uniform(0, -self.side_length/2)+self.x
            y = np.random.uniform(0, self.side_length/2)+self.y
            points.append(Point(x, y))
        return points
