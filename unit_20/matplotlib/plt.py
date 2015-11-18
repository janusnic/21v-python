from numpy import *
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 15
fig = plt.figure ()
ax = fig.gca(projection='3d')

t =  linspace (-2, 2, 100)
x = (1 + t**2) * sin(2 * pi * t)
y = (1 + t**2) * cos(2 * pi * t)
z = t

ax.plot(x, y, z, label='Parametric 3D curve')
ax.legend()
plt.show()