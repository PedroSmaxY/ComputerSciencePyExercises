from random import randint
print('-=-' * 10)
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
print('-=-' * 10)
escolha = int(input('Qual é a sua jogada? '))
pc = randint(0, 2)
if escolha == 0 and pc == 0:
    print('-=-' * 10)
    print('Computador jogou PEDRA')
    print('Jogador jogou PEDRA')
    print('-=-' * 10)
    print('EMPATE')
elif escolha == 1 and pc == 0:
    print('-=-' * 10)
    print('Computador jogou PEDRA')
    print('Jogador jogou PAPEL')
    print('-=-' * 10)
    print('JOGADOR VENCE')
elif escolha == 2 and pc == 0:
    print('-=-' * 10)
    print('Computador jogou PEDRA')
    print('Jogador jogou TESOURA')
    print('-=-' * 10)
    print('COMPUTADOR VENCE')
elif escolha == 0 and pc == 1:
    print('-=-' * 10)
    print('Computador jogou PAPEL')
    print('Jogador jogou PEDRA')
    print('-=-' * 10)
    print('COMPUTADOR VENCE')
elif escolha == 0 and pc == 2:
    print('-=-' * 10)
    print('Computador jogou TESOURA')
    print('Jogador jogou PEDRA')
    print('-=-' * 10)
    print('JOGADOR VENCE')
elif escolha == 1 and pc == 1:
    print('-=-' * 10)
    print('Computador jogou PAPEL')
    print('Jogador jogou PAPEL')
    print('-=-' * 10)
    print('EMPATE')
elif escolha == 1 and pc == 2:
    print('-=-' * 10)
    print('Computador jogou TESOURA')
    print('Jogador jogou PAPEL')
    print('-=-' * 10)
    print('COMPUTADOR VENCE')
elif escolha == 2 and pc == 1:
    print('-=-' * 10)
    print('Computador jogou PAPEL')
    print('Jogador jogou TESOURA')
    print('-=-' * 10)
    print('COMPUTADOR VENCE')
elif escolha == 2 and pc == 2:
    print('-=-' * 10)
    print('Jogador jogou TESOURA')
    print('Computador jogou TESOURA')
    print('-=-' * 10)
    print('EMPATE')
else:
    print('ERRO, TENTE NOVAMENTE !!!')
