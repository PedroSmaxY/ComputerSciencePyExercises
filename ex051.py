print('=' * 25)
print('10 TERMOS DE UMA P.A.')
print('=' * 25)
term = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
ten = term + (10 - 1) * raz
for i in range(term, ten + raz, raz):
    print(i, end=' ➡ ')
print('ACABOU')
