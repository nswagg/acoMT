from typing import List


class Ant:
    def __init__(self, coords, pBest=None, isLeader=False):
        if pBest is None:
            pBest = coords
        self.isLeader: bool = isLeader  # if designated as a leader will have a greater bias over other ant behavior
        self.coords: [2] = coords  # coordinates of where the ant is
        self.pBest: [2] = pBest  # personal best of the ant in the minimization problem
        # self.velocity: int = velocity   # max speed? Removing for PSO

        self.r1 = 1.0   # personal weight between 0 and 2 (unique on particle and iteration)
        self.r2 = 1.0   # social weight between 0 and 2 (unique on particle and iteration)
        self.c1 = 2.05  # personal bias between 0 and 4
        self.c2 = 2.05  # social bias between 0 and 4
        self.w = 0.72984   # intertia between 0 and 1. w > 1 may lead to divergence; Hi = explore, Lo = converge

    def setNewBest(self, newBest: List[int]):
        self.pBest = newBest

    def setNewCoords(self, coords: List[int]):
        self.coords = coords
