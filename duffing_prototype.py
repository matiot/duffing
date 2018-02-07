import numpy as np
from lib import rungekutta
from lib import duffing

import matplotlib.pyplot as plt

def graph(data):
    plt.clf()
    t = []
    y = []
    v = []
    for i in range(len(data)):
        t.append(data[i][0])
        y.append(data[i][1][0])
        v.append(data[i][1][1])
    plt.plot(t,y,'r-',label='position')
    plt.plot(t,v,'b.',label='velocity')
    plt.xlabel(r'$2\pi t/T$')
    plt.legend(loc=1)
    plt.show()
    return

def phasegraph(data):
    plt.clf()
    t = []
    y = []
    v = []
    for i in range(len(data)):
        t.append(data[i][0])
        y.append(data[i][1][0])
        v.append(data[i][1][1])
    plt.plot(y,v,'b-')
    plt.xlabel('Position')
    plt.ylabel('Velocity')

    return

y = np.zeros(2)


A = 1.
B = -1
C = 1.

y[0] = 0.1
y[1] = 0.


t = 0.
dt = 0.001
n = 100000


g = duffing.make_g_duffing(A,B,C)
dat = rungekutta.rk(g, y, t, dt, n)
phasegraph( dat)
plt.plot(0, 0, marker='o', markersize=3, color="red")
plt.plot( np.sqrt(1/(-B)), 0, marker='o', markersize=3, color="red")
plt.show()

graph(dat)

