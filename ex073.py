times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Atlhetico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
         'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
         'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')


print('-=' * 15)
print(f'Lista de times do Brasileirão: {", ".join(times)}')
print('-=' * 15)
print(f'Os 5 primeiros times são: {", ".join(times[0:5])}')
print('-=' * 15)
print(f'Os 4 últimos são: {", ".join(times[-4:])}')
print('-=' * 15)
print(f'Times em ordem alfabética: {", ".join(sorted(times))}')
print('-=' * 15)
print(f'O {times[4]} está na {len(times[4])}ª posição')
