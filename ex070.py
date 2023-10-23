nome_menor_valor = []
nome_maior_valor = []

soma = mil = maiorvalor = menorvalor = 0

print('-' * 30)
print('      LOJA SUPER BARATÃO')
print('-' * 30)

while True:

    nomedoproduto = str(input('Nome do Produto: '))
    try:
        price = float(input('Preço: R$'))
    except ValueError:
        print('Digite um valor inteiro!')
        continue

    soma += price

    if price >= 1000:
        mil += 1

    if menorvalor == 0 or price < maiorvalor:
        menorvalor = price
        nome_menor_valor.append(nomedoproduto)

    if price > maiorvalor:
        maiorvalor = price
        nome_maior_valor.append(nomedoproduto)

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if continuar in ['S', 'N']:
            break

        print('Valor Inválido, digite S ou N')
    print('-' * 30)

    if continuar == 'N':
        break

print('=' * 15, 'FIM DO PROGRAMA', '=' * 15)
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais caro foi {nome_maior_valor[-1]} que custa R${maiorvalor:.2f}')
print(f'O produto mais barato foi {nome_menor_valor[-1]} que custa R${menorvalor:.2f}')
