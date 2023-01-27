import math

import matplotlib.pyplot as plt
import numpy as np
from ant import Ant

na = 50  # number of ants
nt = 1  # number of targets
nb = 1  # number of "home bases"/ ant colonies
jump = .5  # distance an ant moves in a frame/epoch (speed)
ants: [Ant] = []

sd = 1  # standard deviation
mu = 0  # mean of angles (from -180 -> 180 degrees)
dmin = 0  # minimum angle in degrees
dmax = 359  # maximum angle in degrees
rng = np.random.default_rng(seed=37)
rngNorm = np.random.normal(mu, sd)

# make data:
x = np.random.uniform(0, 10, na)
y = np.random.uniform(0, 10, na)
targetsX = np.random.uniform(0, 10, nt)
targetsY = np.random.uniform(0, 10, nt)
homeX = np.random.uniform(0, 10, nb)
homeY = np.random.uniform(0, 10, nb)

# plot:
fig, ax = plt.subplots()

ax.plot(x, y, 'o', markersize=2, color='grey')
ax.plot(targetsX, targetsY, 'o', markersize=4, color='red')
ax.plot(homeX, homeY, 'o', markersize=4, color='blue')

ax.set(xlim=(0, 10), ylim=(0, 10))

plt.show()


def normalize(angle, xmin=0, xmax=359):
    """converts degrees to val between [0,1]"""
    return (angle - xmin) / (xmax - xmin)


def denormalize(norm, xmin=0, xmax=359):
    return (norm * (xmax - xmin)) + xmin


def wander(ant: Ant):
    newAngle = denormalize(normalize(ant.getAngle()) + rngNorm)  # denormalized angle [0,359]
    ant.setCoords(newPoint(newAngle, ant.getSpeed()))
    ant.setAngle(newAngle)


def newPoint(angle, hypotenuse=1):
    """gets the new coordinate from the angle. Hypotenuse = 1 """
    yp = math.sin(angle) * hypotenuse
    xp = math.cos(angle) * hypotenuse
    return [xp, yp]


def euclideanDist(p1, p2):
    """ p1, p2 are lists where the first element is the x coord and the second is the y coord"""
    return math.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1]))
