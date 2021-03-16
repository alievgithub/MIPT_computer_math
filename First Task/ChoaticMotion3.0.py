from matplotlib import pyplot as plt

def MakePlot(r, x, n):
    dev_x = []
    dev_r = []
    for i in range(n):
        r += 1/100
        if i > 10:
            dev_x.append(x)
            dev_r.append(r)
        x = 4 * r * x * (1 - x)
    plt.plot(dev_r, dev_x)
"""
print("Enter r, x0, n separated by space:", end = " ")
r, x, n = input().split()
r = float(r)
x = float(x)
n = int(n)
"""
MakePlot(0, 0.6, 100)
#MakePlot(0.76, 0.4, 1000)
#MakePlot(0.8, 0.4, 1000)
#MakePlot(0.862, 0.4, 1000)
#MakePlot(0.8922, 0.4, 1000)
#MakePlot(0.748, 0.4, 15)

plt.show()
