km = int(input('Velocidade do carro em Km/h: '))
if km >= 80:
    m = (km - 80) * 7
    print('Você foi multado!')
    print('A multa vai custar R${:.2f}'.format(m))
else:
    print('Você não ultrapassou o limite de velocidade!')
