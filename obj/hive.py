from typing import List
import numpy as np
from obj.ant import Ant


class Hive:
    def __init__(self, plot, pos, AIH=25, need=0, xbound=[0, 10], ybound=[0, 10]):
        self.ants: List[Ant] = []
        self.coords: List[int] = pos  # position of the Hive in the environment
        self.need: int = need  # the amount of food the hive needs. 0 if not using Knapsack
        self.plot = plot    # the mathplotlib plot obj
        self.nAnts = AIH    # AIH = ants in hive
        self.acoords = []

        """ Initialize the ants in the colony """
        self.newColony(plot, AIH, xbound, ybound)  # list of Ants in the environment
        """ Plot the Hive onto the plot"""
        self.plot(self.coords[0], self.coords[1], 'o', markersize=4, color='blue')

    def newColony(self, AIH, xbound, ybound):
        ants: List[Ant] = []
        x = np.random.uniform(xbound[0], xbound[1], AIH)
        y = np.random.uniform(ybound[0], ybound[1], AIH)
        self.acoords = [x, y]

        for i in range(AIH):
            ant = Ant([x[i], y[i]])  # coords
            ants.append(ant)
            # The following line can be written more efficiently, but is written out for convenience
            self.plot(ant.coords[0], ant.coords[1], 'o', markersize=2, color='grey')

        self.ants = ants

