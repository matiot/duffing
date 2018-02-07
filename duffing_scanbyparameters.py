import numpy as np
from lib import rungekutta
from lib import duffing
from lib import visualization

#initìial data
y = np.zeros(2)
y[0] = 1.
y[1] = 1.

#simulation window
t = 0.
dt = 0.1
n = 10


for A in np.arange(0,10):
    for B in np.arange(0,10):
        for C in np.arange(0,10):
            print("printing")
            g = duffing.make_g_duffing(A,B,C)
            dat = rungekutta.rungekutta(g, y, t, dt, n)
            filename = 'data/scanbyParam_ABC.dat'
            np.savetxt(filename, dat)
"""

g = duffing.make_g_duffing(1,1,1)
dat = rungekutta.rk(g, y, t, dt, n)
print(dat)

dat = rungekutta.rungekutta(g, y, t, dt, n)
print(dat)
np.savetxt('data/test.out', dat)

"""

