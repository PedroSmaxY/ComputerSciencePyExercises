from random import randint
from time import sleep
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

contador = 0

while True:
    try:
        jogador = int(input('Diga um valor: '))
    except ValueError:
        print('Valor inválido!!!')
        continue

    while True:
        pergunta = str(input('Par ou Ímpar?[P/I] ')).strip().upper()[0]
        if pergunta in ['P', 'I']:
            break
        print('Valor inválido!!!')

    computador = randint(1, 10)
    soma = jogador + computador
    resultado = 'PAR' if soma % 2 == 0 else 'IMPAR'

    print('-' * 50)
    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print(f'Total de {soma}, DEU {resultado}.')
    print('-' * 50)

    if resultado[0] == pergunta:
        print('Você VENCEU!')
        contador += 1
        print('Vamos jogar novamente...')
        sleep(1)
    else:
        print('Você PERDEU!')
        sleep(1)
        break

    sleep(1)

print(f'GAME OVER! Você venceu {contador} vezes.')
