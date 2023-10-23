n = int(input('Digite um número: '))
cont = 0
for i in range(1, n + 1):
    if n % i == 0:
        cont += 1
        print('\033[31m', end=' ')
    else:
        print('\033[m', end=' ')
    print(f'{i}', end=' ')
print(f'\n\033[mO número {n} foi divisível {cont} vezes')
if cont == 2:
    print(f'O número {n} é um número primo')
else:
    print(f'O número {n} não é um número primo')
