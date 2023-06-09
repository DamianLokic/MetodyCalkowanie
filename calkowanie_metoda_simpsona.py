import math

a = 1.4
b = 1.8
n = 6
h = (b - a) / (2 * n)
x = [a + i * h for i in range(2 * n)]
y = [math.sin((x[i] / 2) + 0.1) / (2.2 + math.sqrt(0.7 * math.pow(x[i], 2) + 1.4)) for i in range(2 * n)]
result = (y[0] + y[n - 1])

for i in range(1, 2 * n , 2):
    result += 4 * y[i]

for i in range(2, 2 * n - 1, 2):
    result += 2 * y[i]

print((h / 3) * result)
