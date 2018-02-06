import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from rk import *

y0 = np.zeros(2)
t0 = 0.
y0[0] = 0.
y0[1] = 1.
dt = 0.1
n = 1000


dat = rk(g, y0, t0, dt, n)

# Set up formatting for the movie filters
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

fig = plt.figure()
dat2 = phase(dat)
print(dat2.shape)

l, = plt.plot([], [], 'r-')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel('x')
plt.ylabel(r'$\dot{x}$')

def update_line(num,data,line):
    line.set_data(data[...,:num])
    return line,

line_ani = animation.FuncAnimation(fig, update_line, 1000, fargs=(dat2, l), interval=1, blit=True)

line_ani.save('phase.mp4', writer=writer)
