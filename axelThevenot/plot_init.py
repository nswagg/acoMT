import numpy as np
import matplotlib.pyplot as plt

from utils import plot_2d_pso, plot_3d_pso

""" Test function for initializing the data. Does not iterate, just creates a static image """

n_particles = 50

# Make range grid
X = np.arange(-5, 5, 0.05)
Y = np.arange(-5, 5, 0.05)
meshgrid = np.meshgrid(X, Y)
f = lambda x, y: x ** 2 + (y + 1) ** 2 - 5 * np.cos(1.5 * x + 1.5) - 3 * np.cos(2 * y - 1.5)

particles = np.random.uniform(-5, 5, (n_particles, 2))
velocity = None
""" Will run in plt if None is set (interactive). Will save the png if not"""
# save_path = 'src/0_particle.png'
save_path = None

fig = plt.figure()
ax = fig.add_subplot(1, 2, 2, projection='3d')
plot_3d_pso(meshgrid, f, particles, velocity, ax=ax)
ax = fig.add_subplot(1, 2, 1)
plot_2d_pso(meshgrid, f, particles, velocity, ax=ax)
fig.suptitle(r'Random initialization of $N=%d$ particles' % n_particles)

if save_path is not None:
    plt.savefig(save_path)
else:
    plt.show()
