from trace import Trace



class CurrentLines:
    def __init__(self, trajectory: Trace):
        self.trajectory = trajectory
        self.tangents = []

    def tg(self):
        self.tangents = []
        for trajectory in self.trajectory.points:
            tangents_for_trajectory = []
            for i in range(0, len(trajectory) - 1, 5):
                dx = trajectory[i + 1][0] - trajectory[i][0]
                dy = trajectory[i + 1][1] - trajectory[i][1]
                tangents_for_trajectory.append((dx, dy))
            self.tangents.append(tangents_for_trajectory)

