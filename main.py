from body import Body
from trace_plt import trace_plot
from trace import Trace
from current_lines import CurrentLines
from space import Space
from point import Point

import numpy as np
from velocity_fields import plot_velocity_field

time = (0.1, 0.5)
t = np.arange(time[0], time[1], 0.1)
square = Body(side_length=2, num_points=200)
trajectory = Trace(time)

start_points = trajectory.create_trace_start_points(square)
trajectory.lines()
points = trajectory.all_lines
space_points_list = [Point(-25, 0), Point(0, 25)]
space = Space(space_points_list)
space.initial_limits()
space_bounding_x = space.x
space_bounding_y = space.y
trace_plot(points, space_bounding_x, space_bounding_y)
stream_line = CurrentLines(trajectory)
stream_line.tg()
for t_ in [t[0],t[-1]]:
    plot_velocity_field(t_,x_range = space_bounding_x, y_range = space_bounding_y)