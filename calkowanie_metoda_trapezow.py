import math

a = 1.4
b = 1.8
n = 6
h = (b-a) / n
result = 0

for i in range(1, 2 * n):
    x = a + (i / n) * (b - a)
    result += math.sin((x / 2) + 0.1) / (2.2 + math.sqrt(0.7 * math.pow(x, 2) + 1.4))


fa = math.sin((a / 2) + 0.1) / (2.2 + math.sqrt(0.7 * math.pow(a, 2) + 1.4))
fb = math.sin((b / 2) + 0.1) / (2.2 + math.sqrt(0.7 * math.pow(b, 2) + 1.4))
wynik = h * ((fa/2) + result + (fb / 2))

print(wynik)
