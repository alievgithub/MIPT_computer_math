from matplotlib import pyplot as plt

def MakePlot(r, x, n):
    dev_x = []
    dev_n = []
    for i in range(n):
        dev_x.append(x)
        dev_n.append(i + 1)
        x = 4 * r * x * (1 - x)
    plt.plot(dev_n, dev_x)
"""
print("Enter r, x0, n separated by space:", end = " ")
r, x, n = input().split()
r = float(r)
x = float(x)
n = int(n)
"""
MakePlot(0.752, 0.4, 1000)
#MakePlot(0.76, 0.4, 1000)
#MakePlot(0.8, 0.4, 1000)
#MakePlot(0.862, 0.4, 1000)
#MakePlot(0.8922, 0.4, 1000)
#MakePlot(0.748, 0.4, 15)

plt.show()
