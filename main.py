"""
 1/27/2023 Nick Waggoner
 Ant colony optimization uses a probabalistic approach to create "good pathing" through graphs
"""
from axelThevenot import PSO
from math import cos

epochs = 100
nAnts = 25  # number of ants per hive
nHive = 1  # number of hives in env
nTargets = 1  # number of targets in env


def main():
    # plt.style.use('_mpl-gallery-nogrid')
    # setup using provided algorithm
    def fit(x, y):
        return x**2 + (y + 1)**2 - 5*cos(1.5*x + 1.5) - 3*cos(2*x - 1.5)

    pso = psoClass(50, [1] * 50, fit)


    """ Initialize Targets """

    """ Initialize Hives """

    """ Initialize Environment"""

    # plt.show()

    return 0


if __name__ == "__main__":
    main()
