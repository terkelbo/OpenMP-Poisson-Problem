# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:15:51 2019

@author: terkelbo-pc
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from tqdm import tqdm

font = {'size'   : 14}

mpl.rc('font', **font)


N = 100
h = 2/(N + 1)

X = np.arange(-1, 1, 2/(N+2))
Y = np.arange(-1, 1, 2/(N+2))
X, Y = np.meshgrid(X, Y)

u_old = np.zeros((N+2,N+2))
u_new = np.zeros((N+2,N+2))
f = np.zeros((N+2,N+2))

for i in range(N+2):
    for j in range(N+2):
        if j == (N + 1) or i == 0 or i == (N + 1):
            u_old[i][j] = u_new[i][j] = 20
        elif j == 0:
            u_old[i][j] = u_new[i][j] = 0

for i in range(N+2):
    for j in range(N+2):
        x = -1 + h*j
        y = -1 + h*i
        if y >= 0 and y <= 0.33 and -0.66 <= x and x <= -0.33:
            f[i][j] = 200
        elif j == 0:
            f[i][j] = 0

fig = plt.figure(figsize=(15,10))
ax = fig.gca(projection='3d')
# Plot the surface.
surf = ax.plot_surface(X, Y, f, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.ylabel('x')
plt.xlabel('y')
plt.savefig('radiator_plot.png',bbox_inches='tight')

#run jacobi
for k in tqdm(range(5000)):
    for i in range(1,N+1):
        for j in range(1,N+1):
            u_new[i][j] = 0.25*(u_old[i-1][j] + u_old[i+1][j] + u_old[i][j-1] + u_old[i][j+1] + h*h*f[i][j])
    u_old = u_new.copy()

fig = plt.figure(figsize=(15,10))
ax = fig.gca(projection='3d')
# Plot the surface.
surf = ax.plot_surface(X, Y, u_new, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.view_init(elev=10., azim=-25)
plt.xlim(1,-1)
plt.ylim(1,-1)
plt.ylabel('x')
plt.xlabel('y')
plt.savefig('radiator_sol.png',bbox_inches='tight')