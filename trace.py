from body import Body
from point_move import move_point


class Trace:
    def __init__(self, t):
        self.time = t
        self.points = []
        self.start_points = []
        self.all_lines = []

    def create_trace_start_points(self, body: Body):
        body_points = body.add_points()
        for point_num, target_point in enumerate(body_points):
            point_cords = (target_point.x, target_point.y)
            self.start_points.append(point_cords)

    def lines(self):
        for point_num, point in enumerate(self.start_points):
            self.all_lines.append(move_point(start_points=point, time=self.time))
