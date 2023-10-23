maioridade = mulheres = homens = vinteanos = 0

while True:

    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)

    try:  # Pergunta a idade e corrige alguma digitação errada por parte do usuário
        idade = int(input('Idade: '))
    except ValueError:
        print('Valor Inválido, tente novamente!')
        continue

    print('-' * 25)

    if idade >= 18:
        maioridade += 1

    while True:  # Pergunta o sexo da pessoa e se o valor for diferente de (M) ou (F) entra em loop
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

        print('-' * 25)

        if sexo in ['M', 'F']:
            break

        print('Valor Inválido, tente novamente!')
        print('-' * 25)

    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        vinteanos += 1

    while True:  # Pergunta se o usuário quer continuar, e se o valor for diferente de (S) ou (N) entra em loop
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]

        print('-' * 25)

        if continuar in ['S', 'N']:
            break

        print('Valor Inválido, tente novamente!')

    if continuar == 'N':
        break

print('=' * 10, 'FIM DO PROGRAMA', '=' * 10)

print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {vinteanos} mulheres com menos de 20 anos')
