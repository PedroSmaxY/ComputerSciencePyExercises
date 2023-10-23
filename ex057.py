sexo = True
while sexo:
    pergunta = str(input('Informe o seu sexo? [M/F] ')).strip().upper()[0]
    if pergunta == 'M' or pergunta == 'F':
        sexo = False
    else:
        print('Valor errado, tente novamente!')
print(f'Sexo {pergunta} registrado com sucesso!')
