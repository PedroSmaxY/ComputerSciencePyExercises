valor = float(input('Digite o valor do produto: R$'))
av = str(input('Vai ser pago à vista no dinheiro ou no cheque? responda com (sim ou não)')).strip().upper()
if 'SIM' in av or 'SIN' in av:
    desconto = (10 / 100 * valor)
    desconto = valor - desconto
    print('O valor a vista no dinheiro ou no cheque com 10% de desconto é de R${:.2f}'.format(desconto))
elif 'NÃO' in av or 'NAO' in av:
    avc = str(input('Vai ser pago à vista no cartão? responda com (sim ou não)')).strip().upper()
    if 'SIM' in avc or 'SIN' in avc:
        desconto = (5 / 100 * valor)
        desconto = valor - desconto
        print('O valor a vista no cartão com desconto de 5% fica por R${:.2f}'.format(desconto))
    elif 'NÃO' in avc or 'NAO' in avc:
        x2 = str(input('Vai ser pago em até 2x no cartão? responda com (sim ou não)')).strip().upper()
        if 'SIM' in x2 or 'SIN' in x2:
            print('o valor a pagar é de R${:.2f} sem desconto!'.format(valor))
        elif 'NÃO' in x2 or 'NAO' in x2:
            x3 = str(input('Vai ser pago em 3x ou mais no cartão? responda com (sim ou não)')).strip().upper()
            if 'SIM' in x3 or 'SIN' in x3:
                juros = (20 / 100) * valor
                juros = juros + valor
                print('O valor a pagar é de R${:.2f} com juros base de 20%!!'.format(juros))
            else:
                print('ERRO, TENTE NOVAMENTE!!')
