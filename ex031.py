d = float(input('Digite a distancia de sua viagem em KM/H: '))
pc = d * 0.50
if d >= 200:
    pd = d * 0.45
    print('O preço de sua passagem será de R${:.2f}'.format(pd))
else:
    print('O preço de sua passagem será de R${:.2f}'.format(pc))
