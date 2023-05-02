import os
import numpy as np
import matplotlib.pyplot as plt

from PSO import PSO
from TARGET import TARGET
from utils import plot_2d_pso, plot_3d_pso, make_gif_from_folder

n_particles = 100
T = [TARGET(4, -4, 6),
     TARGET(3, 1, 1),
     TARGET(-4, -2, 3, animate=0)]

# Make range grid
X = np.arange(-10, 10, 0.1)
Y = np.arange(-10, 10, 0.1)
meshgrid = np.meshgrid(X, Y)

# where x0,y0 define the coordinate plane and x1,y1 define the target
f = lambda x0, y0, x1, y1, w: (((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5) - w


def f0(x, y):
    """ minimization function for n targets"""
    func_list = []
    for a in range(len(T)):
        func_list.append(f(x, y, T[a].x, T[a].y, T[a].weight))

    min_list = func_list[0] if len(func_list) > 0 else np.zeros((200, 200))
    for b in range(0, len(func_list)):
        min_list = np.minimum(min_list, func_list[b])
    return min_list


def fitness_function(pos):
    x, y = pos.swapaxes(0, 1)
    return f0(x, y)


def main():

    particles = np.random.uniform(-5, 5, (n_particles, 2))
    # particles = np.random.uniform(0, 0, (n_particles, 2))
    velocities = (np.random.random((n_particles, 2)) - 0.5) / 10
    pso_1 = PSO(particles.copy(), velocities.copy(), fitness_function, T.copy(),
                w=0.25, c_1=2.0, c_2=2.0, max_iter=100, auto_coef=False)
    pso_2 = PSO(particles.copy(), velocities.copy(), fitness_function, T.copy(),
                w=0.73, c_1=2.0, c_2=2.0, max_iter=100, auto_coef=False)
    pso_3 = PSO(particles.copy(), velocities.copy(), fitness_function, T.copy(),
                w=0.9, c_1=2.0, c_2=2.0, max_iter=100, auto_coef=False)

    root = 'src/'
    filename = '_tmp.gif'
    save = True

    if save:
        tmp_dir = os.path.join(root, '_tmp')
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)

    fig = plt.figure()

    while pso_1.next():
        """pso_2.next()
        pso_3.next()"""
        fig.clear()
        save_path = None if not save else os.path.join(tmp_dir, f'{pso_1.iter:05d}.png')

        ax = fig.add_subplot(1, 3, 2, projection='3d')
        plot_3d_pso(meshgrid, f0, pso_1.particles, pso_1.velocities, ax=ax)
        ax = fig.add_subplot(1, 3, 1)
        plot_2d_pso(meshgrid, f0, pso_1.particles, pso_1.velocities, ax=ax)
        ax.set_title(str(pso_1))

        """ax = fig.add_subplot(1, 3, 2, projection='3d')
        plot_3d_pso(meshgrid, f0, pso_1.particles, pso_1.velocities, ax=ax)
        ax = fig.add_subplot(1, 3, 1)
        plot_2d_pso(meshgrid, f0, pso_1.particles, pso_1.velocities, ax=ax)
        ax.set_title(str(pso_1))

        ax = fig.add_subplot(1, 3, 2, projection='3d')
        plot_3d_pso(meshgrid, f0, pso_1.particles, pso_1.velocities, ax=ax)
        ax = fig.add_subplot(1, 3, 1)
        plot_2d_pso(meshgrid, f0, pso_1.particles, pso_1.velocities, ax=ax)
        ax.set_title(str(pso_1))"""

        if save_path is None:
            plt.show()
        else:
            plt.savefig(save_path)

    make_gif_from_folder(tmp_dir, os.path.join(root, filename))


if __name__ == "__main__":
    main()
