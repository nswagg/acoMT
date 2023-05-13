import numpy as np
import matplotlib.pyplot as plt

from utils import plot_2d_pso, plot_3d_pso

""" Test function for initializing the data. Does not iterate, just creates a static image """

n_particles = 100

target_weight = 1
T = [[4, -4, 6],
     [3, 1, 2],
     [-4, -2, 3]]
hazard_weight = 100
H = [[0, 0, 1]]

# where x0,y0 define the coordinate plane and x1,y1 define the target
f = lambda x0, y0, x1, y1, w: (((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5) - w


def f0(x, y):
    """ minimization function for n targets"""
    func_list = []
    for a in range(len(T)):
        func_list.append(f(x, y, T[a][0], T[a][1], T[a][2]))

    min_list = func_list[0]
    for b in range(1, len(func_list)):
        min_list = np.minimum(min_list, func_list[b])

    return min_list


# Make range grid
X = np.arange(-10, 10, 0.05)
Y = np.arange(-10, 10, 0.05)
meshgrid = np.meshgrid(X, Y)
# f = lambda x, y: x ** 2 + (y + 1) ** 2 - 5 * np.cos(1.5 * x + 1.5) - 3 * np.cos(2 * y - 1.5)

particles = np.random.uniform(-10, 10, (n_particles, 2))
velocity = None
""" Will run in plt if None is set (interactive). Will save the png if not"""
# save_path = 'src/0_particle.png'
save_path = None

fig = plt.figure()
ax = fig.add_subplot(1, 2, 2, projection='3d')
plot_3d_pso(meshgrid, f0, particles, velocity, ax=ax)
ax = fig.add_subplot(1, 2, 1)
plot_2d_pso(meshgrid, f0, particles, velocity, ax=ax)
fig.suptitle(r'Random initialization of $N=%d$ particles' % n_particles)

if save_path is not None:
    plt.savefig(save_path)
else:
    plt.show()
