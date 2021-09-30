from scipy import integrate

func = lambda x: x**3

answer = integrate.quad(func, 1, 2)
print(round(answer[0], 5))
