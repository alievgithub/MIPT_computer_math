from math import *


def find_determinant(a, rev):
    det = 1
    for i in range(len(a)):
        det *= a[i][i]
    # print("Было", rev, "перестановок")
    return det if rev % 2 == 0 else -det


def solve(a, b, n):
    a_start = a
    b_start = b
    rev = 0
    for i in range(n - 1):
        if a[i][i] == 0:
            out = False
            for j in range(i + 1, n):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]
                    out = True
                    break
            if not out:
                print("Система не имеет решений или имеет бесконечно много")
                return
        l = i
        for m in range(i + 1, n):
            if abs(a[m][i]) > abs(a[l][i]):
                l = m
        if l != i:
            for j in range(i, n):
                a[i][j], a[l][j] = a[l][j], a[i][j]
            rev += 1
            b[i], b[j] = b[j], b[i]
        for k in range(i + 1, n):
            c = a[k][i] / a[i][i]
            a[k][i] = 0
            for j in range(i + 1, n):
                a[k][j] -= c * a[i][j]
            b[k] -= c * b[i]
    x = []
    det = find_determinant(a, rev)
    if det == 0:
        print("Система не имеет решений или имеет бесконечно много")
        return
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            # При j=i+1 нам нужен x[0], j=i+2 x[1], поэтому x[j-i-1]
            s += a[i][j] * x[j - i - 1]
        # Поскольку мы вычисляем переменные с конца, новое значение ставим в начало
        x.insert(0, (b[i] - s) / a[i][i])
    # print("Определитель равен", det)
    # output_matrix(a, b)
    # output_x(x)
    # output_nev(a_start, b_start, x)
    return x


def quadratic_interpolation(massx, massy, x):
    min = abs(massx[0] - x) + abs(massx[1] - x) + abs(massx[2] - x)
    min_i = 1
    for i in range(2, len(massx) - 1):
        if abs(massx[i - 1] - x) + abs(massx[i] - x) + abs(massx[i + 1] - x) < min:
            min = abs(massx[i - 1] - x) + \
                      abs(massx[i] - x) + abs(massx[i + 1] - x)
            min_i = i
    a, b, c = solve([[massx[min_i - 1] ** 2, massx[min_i - 1], 1], [massx[min_i] ** 2, massx[min_i], 1],
                          [massx[min_i + 1] ** 2, massx[min_i + 1], 1]],
                         [massy[min_i - 1], massy[min_i], massy[min_i + 1]], 3)
    return a * x ** 2 + b * x + c


X = [0.205, 0.2052, 0.2065, 0.2069, 0.2075]
F = [0.20792, 0.20813, 0.20896, 0.20990, 0.21053]

print(quadratic_interpolation(X, F, 0.2062))
