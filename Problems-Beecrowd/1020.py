dias = int(input())

ano = dias // 365
meses = (dias % 365) // 30
dias = (dias % 365) % 30

print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
