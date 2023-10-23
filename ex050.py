soma = 0
cont = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i} valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'você informou {cont} número(s) PAR(ES) e a soma foi {soma}')
