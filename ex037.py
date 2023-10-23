n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('o primeiro valor é maior!, {}!'.format(n1))
elif n2 > n1:
    print('o segundo valor é maior!, {}!'.format(n2))
elif n1 == n2 or n2 == n1:
    print('Não existe valor maior,\n o primeiro valor: {} e o segundo valor: {} são iguais!!!'.format(n1, n2))
