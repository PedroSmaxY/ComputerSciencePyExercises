x = int(input('Digite um número: '))
fatorial = 1
i = x
print(f'{x}! = ', end='')
while i >= 1:
    fatorial *= i
    if i == 1:
        print(f'{i} = {fatorial}', end='')
    else:
        print(f'{i} x ', end='')
    i -= 1
