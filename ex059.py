from random import randint
from time import sleep

numero1 = randint(0, 99)
numero2 = randint(0, 99)
funcao = 0
loop = True

while loop:
    print('=' * 50)
    sleep(0.5)
    print('Digite [ 1 ] para somar')
    print('Digite [ 2 ] para multiplicar')
    print('Digite [ 3 ] para descobrir o maior número')
    print('Digite [ 4 ] para gerar novos números')
    print('Digite [ 5 ] para sair do programa')
    print('=' * 50)
    sleep(0.5)
    print(f'valor 1 = {numero1}')
    print(f'valor 2 = {numero2}')
    print('=' * 50)

    try:
        funcao = int(input('Digite a função desejada: '))
    except ValueError:
        print('Por favor, insira um valor válido!!')
        sleep(2)
        print('=' * 50)
        continue

    if funcao == 1:  # soma os valores
        print(f'A soma entre {numero1} + {numero2} é {numero1 + numero2}')
        sleep(4)
        print('=' * 50)

    elif funcao not in [1, 2, 3, 4, 5]:
        print('Opção inválida. Tente novamente')

    elif funcao == 2:  # multiplica os valores
        print(f'A multiplicação entre {numero1} x {numero2} é {numero1 * numero2}')
        sleep(4)
        print('=' * 50)

    elif funcao == 3:  # descobre qual o valor maior
        if numero1 > numero2:
            print(f'{numero1} é o maior que {numero2}')
            sleep(4)
            print('=' * 50)

        elif numero1 == numero2:
            print(f'{numero1} é igual a {numero2}')
        else:
            print(f'{numero2} é o maior que {numero1}')
            sleep(4)
            print('=' * 50)

    elif funcao == 4:  # gera novos valores
        numero1 = randint(0, 99)
        numero2 = randint(0, 99)
        print('Novos valores gerados!')
        sleep(2)
        print('=' * 50)

    elif funcao == 5:  # sai do programa
        loop = False

print('Programa encerrado')
print('=' * 50)
