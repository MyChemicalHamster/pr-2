
import matplotlib.pyplot as plt

import os



image_name = "trace.png"


def trace_plot(point_coordinates: [], x_limits: [] = None, y_limits: [] = None):
    plt.figure(figsize=(10, 10))
    x_vals_init = [cord[0][0] for cord in point_coordinates[:4]]
    y_vals_init = [cord[0][1] for cord in point_coordinates[:4]]
    plt.plot(x_vals_init, y_vals_init, label='Начальное положение', linestyle='--', marker='o')

    for point_num, point in enumerate(point_coordinates[1:]):
        x_vals = [cord[0] for cord in point]
        y_vals = [cord[1] for cord in point]
        plt.plot(x_vals, y_vals)

    if x_limits is not None:
        plt.xlim(x_limits[0], x_limits[1])

    if y_limits is not None:
        plt.ylim(y_limits[0], y_limits[1])

    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(image_name))
    plt.show()