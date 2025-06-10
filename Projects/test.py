import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Lotka-Volterra equations
def model(y, t, r, a, b, m):
    N, P = y
    dNdt = r * N - a * N * P
    dPdt = b * a * N * P - m * P
    return [dNdt, dPdt]

# Solve ODE
y0 = [40, 9]  # Initial prey=40, predator=9
t = np.linspace(0, 50, 1000)
params = (1, 0.1, 0.02, 0.3)  # r, a, b, m
solution = odeint(model, y0, t, args=params)
N, P = solution.T

# Plot
plt.plot(t, N, label='Prey')
plt.plot(t, P, label='Predator')
plt.xlabel('Time'); plt.legend()
plt.show()
