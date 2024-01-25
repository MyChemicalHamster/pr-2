from runge_kut import runge_kutt



def move_point(start_points: tuple, time):
    points = runge_kutt(time_limits=time, points0=start_points, h=0.01)
    return points
