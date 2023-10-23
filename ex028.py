from random import randint
p = int(input('Vou pensar em um número entre 0 e 5, tente advinhar: '))
a = randint(0, 5)
if p == a:
    print('Parabéns você advinhou!!!')
else:
    print('!!!ERRADO!!!')
    print('tente outra vez!')
#Alternativo: print('Parabéns você advinhou!!!' if p == a else '!!!ERRADO!!!')

