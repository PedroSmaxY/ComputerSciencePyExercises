pi = float(input('Qual é o preço do produto? R$'))
de = float(input('Qual a porcentagem do desconto? '))
pc = de / 100 *pi
po = pi - pc
print('O produto que custava {:.2f}, na promoção de desconto de {:.0f}% vai custar R${:.2f}.'.format(pi, de, po))
