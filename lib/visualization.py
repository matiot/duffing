import matplotlib.pyplot as plt

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
