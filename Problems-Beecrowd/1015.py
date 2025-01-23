from math import sqrt

values1 = input().split(' ')
values2 = input().split(' ')

x1 = float(values1[0])
y1 = float(values1[1])
x2 = float(values2[0])
y2 = float(values2[1])

distancia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f'{distancia:.4f}')