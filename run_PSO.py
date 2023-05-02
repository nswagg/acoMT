import os
import numpy as np
import matplotlib.pyplot as plt

from PSO import PSO
from TARGET import TARGET
from utils import plot_2d_pso, plot_3d_pso, make_gif_from_folder

n_particles = 100
T0 = [TARGET(4, -4, 6, animate=1),
      TARGET(3, 1, 1),
      TARGET(-4, -2, 3, animate=2)]

T1 = [TARGET(4, -4, 6, animate=1),
      TARGET(3, 1, 1),
      TARGET(-4, -2, 3, animate=2)]

T2 = [TARGET(4, -4, 6, animate=1),
      TARGET(3, 1, 1),
      TARGET(-4, -2, 3, animate=2)]

# Make range grid
X = np.arange(-10, 10, 0.1)
Y = np.arange(-10, 10, 0.1)
meshgrid = np.meshgrid(X, Y)

# where x0,y0 define the coordinate plane and x1,y1 define the target
f = lambda x0, y0, x1, y1, w: (((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5) - w


def main():
    particles = np.random.uniform(-10, 10, (n_particles, 2))
    # particles = np.random.uniform(0, 0, (n_particles, 2))
    velocities = (np.random.random((n_particles, 2)) - 0.5) / 10
    pso_1 = PSO(particles.copy(), velocities.copy(), T0,
                w=0.25, c_1=2.0, c_2=2.0, max_iter=100, auto_coef=False)
    pso_2 = PSO(particles.copy(), velocities.copy(), T1,
                w=0.73, c_1=2.0, c_2=2.0, max_iter=100, auto_coef=False)
    pso_3 = PSO(particles.copy(), velocities.copy(), T2,
                w=0.9, c_1=2.0, c_2=2.0, max_iter=100, auto_coef=False)

    root = 'src/'
    filename = '_tmp.gif'
    save = True

    if save:
        tmp_dir = os.path.join(root, '_tmp')
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)

    fig = plt.figure(layout="constrained")

    while pso_1.next():
        pso_2.next()
        pso_3.next()
        fig.clear()
        save_path = None if not save else os.path.join(tmp_dir, f'{pso_1.iter:05d}.png')

        ax = fig.add_subplot(3, 2, 1)
        plot_2d_pso(meshgrid, pso_1.f0, pso_1.particles, pso_1.velocities, ax=ax)
        ax = fig.add_subplot(3, 2, 2, projection='3d')
        plot_3d_pso(meshgrid, pso_1.f0, pso_1.particles, pso_1.velocities, ax=ax)
        ax.set_title(str(pso_1))

        ax = fig.add_subplot(3, 2, 3)
        plot_2d_pso(meshgrid, pso_2.f0, pso_2.particles, pso_2.velocities, ax=ax)
        ax = fig.add_subplot(3, 2, 4, projection='3d')
        plot_3d_pso(meshgrid, pso_2.f0, pso_2.particles, pso_2.velocities, ax=ax)
        ax.set_title(str(pso_2))

        ax = fig.add_subplot(3, 2, 5)
        plot_2d_pso(meshgrid, pso_3.f0, pso_3.particles, pso_3.velocities, ax=ax)
        ax = fig.add_subplot(3, 2, 6, projection='3d')
        plot_3d_pso(meshgrid, pso_3.f0, pso_3.particles, pso_3.velocities, ax=ax)
        ax.set_title(str(pso_3))

        if save_path is None:
            plt.show()
        else:
            plt.savefig(save_path)

    make_gif_from_folder(tmp_dir, os.path.join(root, filename))


if __name__ == "__main__":
    main()
