from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = y = np.linspace(-3, 3, 74)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(4 * R) / R

fig, ax = plt.subplots(1, 3, figsize= (14, 4), subplot_kw=dict(projection='3d'))

norm = mpl.colors.Normalize(-abs(Z).max(), abs(Z).max())
p = ax[0].plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, antialiased=False, norm=norm, cmap=mpl.cm.inferno)
cb = fig.colorbar(p, ax=ax[0], shrink=0.6)

ax[0].set_xlabel("$x$", fontsize=16)
ax[0].set_ylabel("$x$", fontsize=16)
ax[0].set_zlabel("$x$", fontsize=16)

ax[1].plot_wireframe(X, Y, Z, rstride=3, cstride=3)
ax[1].set_title("plot wireframe")

ax[2].contour(X, Y, Z, zdir='z', offset=0, cmap=mpl.cm.inferno)
ax[2].set_title('countour')

ax[2].set_xlabel("$x$", fontsize=16)
ax[2].set_ylabel("$x$", fontsize=16)
ax[2].set_zlabel("$x$", fontsize=16)

plt.show()
