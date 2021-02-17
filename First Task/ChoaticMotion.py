from matplotlib import pyplot as plt

def MakePlot(r, x, n):
    dev_x = []
    dev_n = []
    for i in range(n):
        dev_x.append(x)
        dev_n.append(i + 1)
        x = 4 * r * x * (1 - x)
    plt.plot(dev_n, dev_x)
    return plt.show()

MakePlot(0.5, 0.5, 6)
