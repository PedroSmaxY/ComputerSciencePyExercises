print('=' * 25)
print('10 TERMOS DE UMA P.A.')
print('=' * 25)
term = int(input('Primeiro termo: '))
raz = int(input('Razão: '))

i = 0
while i < 10:
    print(term, end=' ➡ ')
    term += raz
    i += 1

print('ACABOU')
