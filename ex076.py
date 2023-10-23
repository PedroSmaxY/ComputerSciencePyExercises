listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90,
            'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
            'Compasso', 9.90, 'Mochila', 120.32, 'Canetas', 22.30)

print('-' * 30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-' * 30)

for pos in range(0, len(listagem), 2):
    item = listagem[pos]
    preco = listagem[pos + 1]
    print(f'{item:<20} R${preco:>6.2f}')

print('-' * 30)
