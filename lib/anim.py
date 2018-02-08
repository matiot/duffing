import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# from rk import *
import rungekutta
import duffing


def update_line(num,data,line):
    line.set_data(data[...,:num])
    return line,


def anim(dat,nframes,name='phase',fps=25):
    # Set up formatting for the movie filters
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=fps, metadata=dict(artist='Me'), bitrate=1800)

    fig = plt.figure()
    # dat2 = phase(dat)
    # print(dat2.shape)
    
    l, = plt.plot([], [], 'r-')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.xlabel('position y')
    plt.ylabel(r'velocity $\dot{y}$')
    plt.title(name)

    line_ani = animation.FuncAnimation(fig, update_line, nframes, fargs=(dat.T, l), interval=10, blit=True)

    line_ani.save('../data/'+name+'.mp4', writer=writer)

    
A = 1.
B = 10.
C = 6.

y0 = np.zeros(2)
t0 = 0.
y0[0] = 0.5
y0[1] = 0.05
dt = 0.01
n = 1000

g = duffing.make_g_duffing(A,B,C)
dat = rungekutta.rungekutta(g, y0, t0, dt, n)

print('making video...')

anim(dat[:,1:],n,'A='+str(round(A,1))+'_B='+str(round(B,1))+'_C='+str(round(C,1)))

print('...done!')
