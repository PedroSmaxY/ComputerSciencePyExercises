from random import randint
print('-=' * 12)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas opções: \n [ 0 ] PEDRA \n [ 1 ] PAPEL \n [ 2 ] TESOURA')
print('-=' * 12)
pessoa = int(input('Qual é a sua jogada? '))
print('-=' * 12)
print('O computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[pessoa]))
print('-=' * 12)
if computador == 0: #Computador jogou pedra
    if pessoa == 0:
        print('EMPATE')
    elif pessoa == 1:
        print('O JOGADOR VENCEU')
    elif pessoa == 2:
        print('O COMPUTADOR VENCEU')
elif computador == 1: #Computador jogou papel
    if pessoa == 0:
        print('O COMPUTADOR VENCEU')
    elif pessoa == 1:
        print('EMPATE')
    elif pessoa == 2:
        print('O JOGADOR VENCEU')
elif computador == 2: #Computador jogou tesoura
    if pessoa == 0:
        print('O JOGADOR VENCEU')
    elif pessoa == 1:
        print('O COMPUTADOR VENCEU')
    elif pessoa == 2:
        print('EMPATE')
