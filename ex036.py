v = float(input('Qual é o valor da casa? '))
s = float(input('Qual é o seu salário? '))
t = int(input('Em quantos anos deseja pagar? '))
meses = t * 12
parcela = v / meses
if parcela > (30 / 100 * s):
    print('O empréstimo no valor de {:.2f} mensais foi negado!!'.format(parcela))
else:
    print('O empréstimo no valor de R${:.2f} mensais foi aceito'.format(parcela))
