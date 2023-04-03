"""
Functions for running Particle Swarm Optimization
"""
from math import sqrt


def checkEuclid(targetCoords, antCoords, dimensions=2):  # each coord is a list of 2 integers
    """ Calculates the distance between two points in a 2D coordinate plane"""
    sum = 0
    for x in range(dimensions):
        sum += (targetCoords[x] - antCoords[x]) ** 2

    return sqrt((targetCoords[0] - antCoords[0]) ** 2 + (targetCoords[1] - antCoords[1]) ** 2)


