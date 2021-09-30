''' Don't work
from matplotlib import pyplot as plt
from random import*

def MakePlot(n):
    dev_x = []
    dev_r = []
    dev_r = [r / 100000 for r in range(1, 100001)]
    for r in dev_r:
        arr_x = []
        x = random()
        for i in range(n):
            x = 4 * r * x * (1 - x)
            arr_x.append(x)
        dev_x.append(arr_x)
    plt.scatter(dev_r, dev_x, 0.1)
"""
print("Enter r, x0, n separated by space:", end = " ")
r, x, n = input().split()
r = float(r)
x = float(x)
n = int(n)
"""
MakePlot(2000)
#MakePlot(0.76, 0.4, 1000)
#MakePlot(0.8, 0.4, 1000)
#MakePlot(0.862, 0.4, 1000)
#MakePlot(0.8922, 0.4, 1000)
#MakePlot(0.748, 0.4, 15)

plt.show()
'''

from matplotlib import pyplot as plt
from random import*

f = lambda x: 4 * r * x * (1 - x)
def X(n):
    st = [f(x0)]
    while len(st) < n:
        st.append(f(st[-1]))
    return st[-1]
x = []
dev_r = [z / 100000 for z in range(1, 100001)]
for r in dev_r:
    x0 = random()
    x.append(X(2000))
ax = plt.subplots()
plt.scatter(dev_r, x, 0.1)
plt.show()
