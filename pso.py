import math

import matplotlib.pyplot as plt
import numpy as np

"""
https://towardsdatascience.com/particle-swarm-optimization-visually-explained-46289eeb2e14



x = np.linspace(-2, 2,100)  # sample data
y = np.linspace(-2, 2,100)

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# f(x, y) = x² + (y + 1)² - 5cos(1.5x + 1.5) - 3cos(2x - 1.5)
ax.plot((x, y), x ** 2 + (y + 1) ** 2 - 5 * math.cos(1.5 * x + 1.5) - 3 * math.cos(2 * x - 1.5), label="topograph")
"""



"""********************************************************
# 3D wireframe example
# https://matplotlib.org/stable/plot_types/3D/wire3d_simple.html#sphx-glr-plot-types-3d-wire3d-simple-py
********************************************************"""
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

# Make data
X, Y, Z = axes3d.get_test_data(0.05)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
"""********************************************************
3D Surface example
https://matplotlib.org/stable/plot_types/3D/surface3d_simple.html#sphx-glr-plot-types-3d-surface3d-simple-py
********************************************************"""

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

plt.style.use('_mpl-gallery')

# Make data
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()