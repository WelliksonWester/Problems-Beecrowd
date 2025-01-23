values = input().split(' ')

A = float(values[0])
B = float(values[1])
C = float(values[2])

MaiorAB = (A + B + abs(A - B)) // 2
Maior = (MaiorAB + C + abs(MaiorAB - C)) // 2

print(f'{Maior:.0f} eh o maior')