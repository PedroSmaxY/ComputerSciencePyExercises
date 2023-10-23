from random import randint
computador = randint(0, 10)
jogador = 0
tentativas = 0

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

while jogador != computador:
    try:
        jogador = int(input('Qual é seu palpite? '))
    except ValueError:
        print('Por favor, insira um número inteiro válido!')
        continue

    tentativas += 1

    if jogador != computador:
        if computador > jogador:
            print('Mais... Tente mais uma vez')
        elif computador < jogador:
            print('Menos... Tente mais uma vez')

print(f'Acertou com {tentativas} tentativa(s). Parabéns!')
