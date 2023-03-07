import configator, numpy, tqdm

from src.utils import relative_set_difference_distance as rsdd
from itertools import product

configuration = configator.Configator()
radius = configuration.rsdd3D.radius
size = configuration.rsdd3D.size

def around(i,j,r,s):
    return [(i+ri,j+rj) for \
            ri, rj in product(range(-r, r+1), range(-r, r+1)) \
            if ri**2 + rj**2 < r**2 and \
            0 <= i+ri <= s - 1 and \
            0 <= j+rj <= s - 1]

values = numpy.arange(size**2).reshape((size, size))
solset = {values[i,j] for i,j in around(size//2,size//2,radius*2,size)}
result = numpy.zeros((size,size))

for i, j in tqdm.tqdm(product(range(size), range(size)), total=size**2):

    indices = around(i,j, radius, size)
    current = {values[i,j] for i,j in indices}
    result[i,j] = rsdd(solset, solset, current)

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

X, Y = numpy.meshgrid(numpy.arange(-size//2, size//2), numpy.arange(-size//2, size//2))
Z = result
X = X[radius:-radius, radius:-radius]
Y = Y[radius:-radius, radius:-radius]
Z = Z[radius:-radius, radius:-radius]

# make the panes transparent
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# make the grid lines transparent
ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
# plot the surface.
surf = ax.plot_wireframe(X, Y, Z, 
                       linewidth=configuration.rsdd3D.linewidth, 
                       color=configuration.rsdd3D.color,
                       antialiased=True)


X, Y = numpy.meshgrid(numpy.arange(-size//2, size//2), numpy.arange(-size//2, size//2))


if configuration.rsdd3D.show: plt.show()

plt.savefig(configuration.rsdd3D.output_path,
            dpi=configuration.rsdd3D.dpi,
            format=configuration.rsdd3D.format,
            transparent=True)


