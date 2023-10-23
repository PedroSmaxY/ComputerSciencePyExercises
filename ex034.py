s = float(input('Qual é o seu salário? R$'))
if s > 1250:
    sa = s + (10 / 100 * s)
else:
    sa = s + (15 / 100 * s)
print('O seu salário será atualizado para R${:.2f}'.format(sa))
