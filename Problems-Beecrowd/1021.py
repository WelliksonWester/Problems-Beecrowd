n = float(input())  # Entrada do valor
valor = int(n * 100)  # Converte para centavos

print('NOTAS:')
print(f'{valor // 10000} nota(s) de R$ 100.00')
valor %= 10000
print(f'{valor // 5000} nota(s) de R$ 50.00')
valor %= 5000
print(f'{valor // 2000} nota(s) de R$ 20.00')
valor %= 2000
print(f'{valor // 1000} nota(s) de R$ 10.00')
valor %= 1000
print(f'{valor // 500} nota(s) de R$ 5.00')
valor %= 500
print(f'{valor // 200} nota(s) de R$ 2.00')
valor %= 200

print('MOEDAS:')
print(f'{valor // 100} moeda(s) de R$ 1.00')
valor %= 100
print(f'{valor // 50} moeda(s) de R$ 0.50')
valor %= 50
print(f'{valor // 25} moeda(s) de R$ 0.25')
valor %= 25
print(f'{valor // 10} moeda(s) de R$ 0.10')
valor %= 10
print(f'{valor // 5} moeda(s) de R$ 0.05')
valor %= 5
print(f'{valor} moeda(s) de R$ 0.01')
