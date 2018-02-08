import numpy as np
from lib import rungekutta
from lib import duffing
from lib import visualization

#System Parameters
A = 0.
B = 1.
C = 0.5

#Initial Data
y = np.zeros(2)
y[0] = 1. + 0.000002
y[1] = 0. - 0.000002

#Time window
t = 0.
dt = 0.001
n = 100000


#Simulation
g = duffing.make_g_duffing(A,B,C)
print( g(y,t))

print('Simulating ...')
dat = rungekutta.rk(g, y, t, dt, n)


#if B < 0. :
#    plt.plot( np.sqrt(1/(-B)), 0, marker='o', markersize=3, color="red")

#Visualization
title = 'Duffing A='+str(A)+' B='+ str(B) + ' C=' + str(C)
visualization.phasegraph( dat, title)
visualization.timegraph(dat, title)

