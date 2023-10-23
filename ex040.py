av1 = float(input('Digite sua nota na AV1: '))
av2 = float(input('Digite sua nota na AV2: '))
media = (av1 + av2) / 2
if media < 5:
    print('A sua média é de {:.1f}, REPROVADO!!!'.format(media))
elif 5 <= media < 6.9:
    print('A sua média é de {:.1f}, RECUPERAÇÃO!!!'.format(media))
elif media >= 7:
    print('A sua média é de {:.1f}, APROVADO!!!'.format(media))
