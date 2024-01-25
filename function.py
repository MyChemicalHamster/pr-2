import math
import numpy as np


def function_a(t) -> float:
    return -math.log(t)


def function_b(t) -> float:
    return t


def dif_sys_func(t: float, point_coordinates: tuple) -> np.ndarray:
    return np.array([function_a(t) * point_coordinates[0], function_b(t) * point_coordinates[1]])
