import numpy as np
from scipy.special import roots_legendre


def gauss_legendre(a, b, n):
    result = 0
    x, w = roots_legendre(n)
    A, B = (b+a)/2, (b-a)/2
    for i in range(n):
        result += w[i] * (np.sin((B * x[i] + A) / 2) + 0.1) / (2.2 + np.sqrt(0.7 * np.power((B * x[i] + A), 2) + 1.4))
    wynik = B * result
    return wynik


print(gauss_legendre(1.4, 1.8, 6))
