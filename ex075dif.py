lista = []

for c in range(1, 5):
    try:
        numero = int(input('Digite um valor: '))
    except ValueError:
        print('Tente novamente.', end=' ')
        continue

    lista.append(numero)

tupula = tuple(lista)

print(f'você digitou os valores {" ".join(map(str, tupula))}')
print(f'O valor 9 apareceu {tupula.count(9)} vezes')

if 3 in tupula:
    print(f'O valor 3 foi digitado {tupula.count(3)} vezes')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram ', end='')

for valor in tupula:
    if valor % 2 == 0:
        print(valor, end=' ')
