ant = float(input('Qual é o salário do Funcionário? R$'))
aum = float(input('Qual é a porcentagem do aumento? '))
sat = (aum / 100 * ant) + ant
print("Um funcionário que ganhava R${:.2f}, com {:.0f}% de aumento, passa a receber R${:.2f}".format(ant, aum, sat))

