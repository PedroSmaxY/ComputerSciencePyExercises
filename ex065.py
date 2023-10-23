numero = contador = soma = 0
valor = []
a = True

while a:
    try:
        numero = float(input('Digite um valor: '))
    except ValueError:
        print('tente um valor valido!!!')
        continue
    flag = False
    valor.append(numero)
    while not flag:
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()
        if continuar == 'S':
            soma += numero
            contador += 1
            flag = True
        elif continuar == 'N':
            soma += numero
            contador += 1
            a = False
            flag = True
        else:
            print('Valor inválido. Por favor, digite "S" ou "N"')

media = 0

if contador > 0:
    media = soma / contador

print(f'A média dos {contador} valores é {media:.2f}')
print(f'O maior valor foi {max(valor):.2f} e o menor foi {min(valor):.2f}')
