pesos = []
for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa '))
    pesos.append(peso)
menor_peso = min(pesos)
maior_peso = max(pesos)
print(f'O menor peso foi {menor_peso}kg')
print(f'O maior peso foi {maior_peso}kg')
