n = s = c = 0

while True:
    try:
        n = int(input('Digite um número inteiro (999 para parar): '))
    except ValueError:
        print('Insira um valor válido')
        continue

    if n == 999:
        break

    s += n
    c += 1

print(f'A soma dos {c} valores é igual a {s}.')
