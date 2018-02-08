import matplotlib.pyplot as plt



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
