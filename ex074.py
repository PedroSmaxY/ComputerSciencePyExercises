from random import randint

while True:
    lista = (randint(1, 10), randint(1, 10), randint(1, 10),
             randint(1, 10), randint(1, 10))

    print(f'Os valores sorteados foram: {" ".join(map(str, lista))}')
    print(f'O maior valor sorteado foi {max(lista)}')
    print(f'O menor valor sorteado foi {min(lista)}')

    while True:
        pergunta = str(input('Quer gerar novos valores? [S/N] ')).strip().upper()[0]
        if pergunta in ['S', 'N']:
            break
        print('Valor inválido.', end=' ')

    if 'N' in pergunta:
        break

print('Programa encerrado')