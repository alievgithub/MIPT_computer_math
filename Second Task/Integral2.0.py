#For cos(x) (0, pi / 2)

import numpy as np
import matplotlib.pylab as plt
plt.style.use('ggplot')

N = 10**8
x_lim = (0, np.pi / 2)
y_lim = (0, 1)
REAL = 1

def calc_integral(func, x_lim, y_lim, N):
    x_random = np.random.uniform(low=x_lim[0], high=x_lim[1], size=N).reshape((N, 1))
    y_random = np.random.uniform(low=y_lim[0], high=y_lim[1], size=N).reshape((N, 1))

    random_coors = np.concatenate(
        (x_random, y_random),
        axis=1,
        )

    func_coors = np.concatenate(
        (x_random, func(x_random)),
        axis=1
        )

    counter = (random_coors <= func_coors).all(axis=1).sum()

    return ((y_lim[1] - y_lim[0]) * (x_lim[1] - x_lim[0])) * (counter / N)


ns = [10**3, 10**4, 10**5, 10**6, 10**7]
errors = []

for n in ns:
    overall_error = 0
    for _ in range(100):
        calculated_integral = calc_integral(np.cos, x_lim, y_lim, N=n)
        error = np.abs(calculated_integral - REAL) / REAL
        overall_error += error

    errors.append(overall_error / 100)

ns_log = np.log(ns)
errors_log = np.log(errors)

fig, ax = plt.subplots(1, 2, figsize=(15, 5))

ax[0].plot(ns, errors, label='error от n')
ax[0].set_xlabel('n')
ax[0].set_ylabel('error')
ax[0].legend()

ax[1].plot(ns_log, errors_log, label='log(error) от log(n)')
ax[1].set_xlabel('log(n)')
ax[1].set_ylabel('log(error)')
ax[1].legend();

plt.show()

slope, intercept = np.polyfit(ns_log, errors_log, 1)

print(f" Получившийся наклон: {slope}")
