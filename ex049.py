print('-=-' * 14)
n = int(input('Digite um número para ver sua tabuada: '))
print('-=-' * 5)
for c in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(n, c, n * c))
print('-=-' * 5)
