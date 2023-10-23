lista = []
while True:
    try:
        valor = int(input('Digite um valor: '))
    except ValueError:
        print('Tente novamente')
        continue
    lista.append(valor)
    while True:
        resposta = str(input('Quer continuar [S/N]')).strip().upper()[0]
        if 'S' in resposta or 'N' in resposta:
            break
        else:
            print('Tente novamente')
    if resposta == 'N':
        break
