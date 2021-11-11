from tabulate import tabulate


X = [0.205, 0.2052, 0.2065, 0.2069, 0.2075]
F = [0.20792, 0.20813, 0.20896, 0.20990, 0.21053]
N = len(F) - 1

f = [F]+[[0]*(N-i) for i in range(N)]  # таблица значений f

k = 1
for j in range(1, len(f)):
    for i in range(len(f[j])):
        if (X[i+k] - X[i]) != 0:
            f[j][i] = (f[j-1][i] - f[j-1][i+1]) / (X[i+k] - X[i])
        else:
            print(f"STOP! YOU HAVE EQUAL NODES: {X[i+k]} and {X[i]}")
            exit(0)
    k += 1
    print(tabulate(f, showindex=[
          f"k={i}" for i in range(N+1)], tablefmt="fancy_grid"))
