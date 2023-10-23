print('-' * 30)
print('      BANCO SMAXY')
print('-' * 30)

while True:
    try:
        valor = int(input('Qual valor você deseja sacar? R$'))
    except ValueError:
        print('Digite um número inteiro!!')
        continue

    if valor % 2 != 0 and valor % 5 != 0:
        print('Valor inválido, o valor solicitado deve ser divisível por 2.')
        continue

    if valor <= 0 or valor > 10000:
        print('Valor inválido. O valor solicitado deve estar entre R$ 1 e R$ 10.000.')
        continue

    cedulas = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}
    total_cedulas = 0

    while valor > 0:
        if valor >= 100:
            cedulas[100] += 1
            valor -= 100

        elif valor >= 50:
            cedulas[50] += 1
            valor -= 50

        elif valor >= 20:
            cedulas[20] += 1
            valor -= 20

        elif valor >= 10:
            cedulas[10] += 1
            valor -= 10

        elif valor >= 5:
            cedulas[5] += 1
            valor -= 5

        elif valor >= 2:
            cedulas[2] += 1
            valor -= 2

        total_cedulas += 1

    print('-' * 30)

    if total_cedulas == 1:
        print('Você receberá 1 cédula.')
    else:
        print(f'Você receberá {total_cedulas} cédulas.')

    for cedula, quantidade in cedulas.items():
        if quantidade > 0:
            print(f'{quantidade} cédula(s) de R${cedula:.2f}.')
    print('-' * 30)
    break

print('Volte sempre ao BANCO SMAXY!, Tenha um bom dia!')
