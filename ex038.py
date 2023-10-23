from datetime import date
ano = int(input('Qual o ano que você nasceu? '))
idade = (date.today().year - ano)
if idade < 18:
    tempo = 18 - idade
    print('Você ira se alistar daqui a {} ano(s)!!'.format(tempo))
elif idade == 18:
    print('Você vai se alistar esse ano!!!.')
elif idade > 18:
    tempo = idade - 18
    print('Já se passaram {} ano(s) do tempo do seu alistamento.'.format(tempo))
