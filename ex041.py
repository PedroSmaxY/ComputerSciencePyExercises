from datetime import date
ano = int(input('Qual é o ano que o atleta nasceu? '))
idade = (date.today().year - ano)
if idade <= 9:
    print('Atleta Mirim!!')
elif idade <= 14:
    print('Atleta Infantil!!')
elif idade <= 19:
    print('Atleta Junior!!')
elif idade <= 20:
    print('Atleta Sênior!!')
else:
    print('Atleta Master!!')
    