extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco'
           , 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    try:
        numero = int(input('Digite um número entre 0 e 20: '))
        if numero < 0 or numero > 20:
            raise ValueError
    except ValueError:
        print('Tente novamente.', end=' ')
        continue

    if 0 <= numero <= 20:
        print(f'Você digitou o número {extenso[numero]}')

        while True:
            pergunta = str(input('Quer continuar [S/N] ')).strip().upper()[0]
            if pergunta == 'S' or pergunta == 'N':
                break
            else:
                print('Tente novamente.', end=' ')

    if pergunta == 'N':
        break

print(f'Programa finalizado!!!')
