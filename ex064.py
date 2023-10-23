soma = contador = 0
continuar = True

print('para encerrar o laço digite [ 999 ]')

while continuar:
    try:
        numero = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Por favor, digite um valor correto!!')
        continue

    if numero == 999:
        continuar = False
    else:
        soma += numero
        contador += 1

print(f'O laço foi encerrado. Foram digitados um total de {contador} números, e a soma de todos é igual a {soma}.')
