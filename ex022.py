nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome) - nome.count(' ')))
di = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(di[0], len(di[0])))


