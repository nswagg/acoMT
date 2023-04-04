import math
import os
import numpy as np
import matplotlib.pyplot as plt

from PSO import PSO
from utils import plot_2d_pso, plot_3d_pso, make_gif_from_folder

n_particles = 100
tg0 = np.array([-2, 2])
tg1 = np.array([3, -2])

# Make range grid
X = np.arange(-5, 5, 0.05)
Y = np.arange(-5, 5, 0.05)
meshgrid = np.meshgrid(X, Y)
""" Testing function f """
f = lambda x, y: x ** 2 + (y + 1) ** 2 - 5 * np.cos(1.5 * x + 1.5) - 5 * np.cos(2 * y - 1.5)
# where x,y define the coordinate plane
fe = lambda x0, y0, x1, y1: ((x0-x1) ** 2 + (y0-y1) ** 2) ** 0.5
fx = lambda x, y: ((x - tg1[0]) ** 2 + (y - tg1[1]) ** 2) ** 0.5


def f0(x, y):
    """ minimization function for 2 targets"""
    func_e = fe(x, y, tg0[0], tg0[1])
    func_x = fe(x, y, tg1[0], tg1[1])
    min_list = np.minimum(func_e, func_x)
    return min_list


def fitness_function(pos):
    x, y = pos.swapaxes(0, 1)
    return f0(x, y)


particles = np.random.uniform(-5, 5, (n_particles, 2))
velocities = (np.random.random((n_particles, 2)) - 0.5) / 10

pso_1 = PSO(particles.copy(), velocities.copy(), fitness_function, w=0.73, c_1=2.0, c_2=2.0, max_iter=100, auto_coef=False)

root = 'src/'
filename = 'test4.0.gif'
save = True

if save:
    tmp_dir = os.path.join(root, '_tmp')
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

fig = plt.figure()

while pso_1.next():
    fig.clear()
    save_path = None if not save else os.path.join(tmp_dir, f'{pso_1.iter:05d}.png')

    ax = fig.add_subplot(1, 2, 2, projection='3d')
    plot_3d_pso(meshgrid, f0, pso_1.particles, pso_1.velocities, ax=ax)
    ax = fig.add_subplot(1, 3, 1)
    plot_2d_pso(meshgrid, f0, pso_1.particles, pso_1.velocities, ax=ax)
    ax.set_title(str(pso_1))

    if save_path is None:
        plt.show()
    else:
        plt.savefig(save_path)

make_gif_from_folder(tmp_dir, os.path.join(root, filename))
