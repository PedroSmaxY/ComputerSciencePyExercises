print('Se quiser sair do programa é só digitar um número menor que zero')

while True:
    try:
        num = int(input('Quer ver a tabuada de qual valor? '))
    except ValueError:
        print('Valor invalido, digite um número inteiro!!!')
        continue

    if num < 0:
        break

    print('=' * 15)

    for i in range(1, 11):
        print(f'{num:2} x {i:2} = {num * i:2}')

    print('=' * 15)

print('Programa finalizado!')
