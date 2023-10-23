from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
Lista = [n1, n2, n3, n4]
shuffle(Lista)
print('A ordem de apresentação será \n {}'.format(Lista))



