import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#Function: Time law
def timegraph(data,title):
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
    plt.title(title)
    plt.show()
    return

#Function: Phase Diagram
def phasegraph(data,title):
    plt.clf()
    t = []
    y = []
    v = []
    for i in range(len(data)):
        t.append(data[i][0])
        y.append(data[i][1][0])
        v.append(data[i][1][1])
    plt.plot(y[0],v[0],'x',color="red")
    plt.plot(0,0,'x')
    plt.plot(y,v,'b-')
    plt.xlabel('Position')
    plt.ylabel('Velocity')
    plt.title(title)
    plt.show()
    return

# Update line for each frame of the video
def update_line(num,data,line):
    line.set_data(data[...,:num])
    return line,

# create an animation of the trajectory in the phase space
def anim(dat,nframes,name='phase',fps=25,bitrate=1800,interval=10):
    # Set up formatting for the movie filters
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=fps, bitrate=bitrate)

    fig = plt.figure()
    
    l, = plt.plot([], [], 'r-')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.xlabel('position y')
    plt.ylabel(r'velocity $\dot{y}$')
    plt.title(name)

    line_ani = animation.FuncAnimation(fig, update_line, nframes, fargs=(dat.T, l), interval=interval, blit=True)

    line_ani.save('data/'+name+'.mp4', writer=writer)
