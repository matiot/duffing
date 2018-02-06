import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def g(y,t):
    # y1 = [ 0, 0 ]
    # y1[0] = y[1]
    # y1[1] = -y[0] #+ y[0]**3
    return np.array([ y[1], -0.01*y[1]-y[0] ])


def rk_step(g, y0, t0, dt):
    c1 = g(y0        , t0        )*dt
    c2 = g(y0 + c1/2., t0 + dt/2.)*dt
    c3 = g(y0 + c2/2., t0 + dt/2.)*dt
    c4 = g(y0 + c3   , t0 + dt   )*dt
    # c1 = np.array([ y[1], -y[0] ])
    # c2 = np.array([ y[1]-y[0], -y[0]-y[1]/2. ])
    # c3 = 
    # c4 = g(y0 + c3   , t0 + dt   )
    return y0 + 1./6.*( c1 + 2.*c2 + 2.*c3 + c4 )


def euler_step(g, y0, t0, dt):
    return y0 + g(y0, t0)*dt


def rk(g, y0, t0, dt, n):
    data = [ [t0, y0] ]
    for i in range(1,n):
        ti,yi = data[i-1]
        data.append( [ti + dt, rk_step(g, yi, ti, dt)] )
    return data


def printdata(data):
    # print(np.array(data).shape)
    for i in data:
        print(i)
    return


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
    plt.show()
    return


def phase(data):
    y = []
    v = []
    for i in range(len(data)):
        y.append(data[i][1][0])
        v.append(data[i][1][1])
    return np.array([ y, v ])


# y0 = np.zeros(2)
# t0 = 0.
# y0[0] = 0.
# y0[1] = 1.
# dt = 0.1
# n = 1000


# dat = rk(g, y0, t0, dt, n)

# # Set up formatting for the movie filters
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

# fig = plt.figure()
# dat2 = phase(dat)
# print(dat2.shape)

# l, = plt.plot([], [], 'r-')
# plt.xlim(-1, 1)
# plt.ylim(-1, 1)
# plt.xlabel('x')
# plt.ylabel(r'$\dot{x}$')

# def update_line(num,data,line):
#     line.set_data(data[...,:num])
#     return line,

# line_ani = animation.FuncAnimation(fig, update_line, 2500, fargs=(dat2, l), interval=1, blit=True)

# line_ani.save('lines.mp4', writer=writer)
