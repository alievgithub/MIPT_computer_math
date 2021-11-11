import numpy as np


def linear_interpolation(massx, massy, x):
    for i in range(1, len(massx)):
        if massx[i - 1] <= x <= massx[i]:
            a = (massy[i] - massy[i - 1]) / (massx[i] - massx[i - 1])
            b = massy[i - 1] - a * massx[i - 1]
            return a * x + b


X = [0.205, 0.2052, 0.2065, 0.2069, 0.2075]
F = [0.20792, 0.20813, 0.20896, 0.20990, 0.21053]

print(linear_interpolation(X, F, 0.2062))
