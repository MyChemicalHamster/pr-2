import numpy as np
from function import dif_sys_func


def runge_kutt(time_limits, points0, h):
    time = np.arange(time_limits[0], time_limits[1], h)
    points = np.zeros((len(time), len(points0)))
    points[0] = points0
    for i in range(1, len(time)):
        t = time[i]
        k1 = h * dif_sys_func(t, points[i - 1])
        k2 = h * dif_sys_func(t + h / 2, points[i - 1] + k1 / 2)
        k3 = h * dif_sys_func(t + h, points[i - 1] - k1 + 2 * k2)
        points[i] = points[i - 1] + (k1 + 4 * k2 + k3) / 6
    return points
