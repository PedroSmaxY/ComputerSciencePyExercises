print('Descubra se suas retas formam um triangulo: ')
r1 = float(input('Quantos cm tem a primeira reta? '))
r2 = float(input('Quantos cm tem a segunda reta? '))
r3 = float(input('Quantos cm tem a terceira reta? '))
if r3 + r2 >= r1 and r1 + r2 >= r3 and r1 + r3 >= r2:
    print('pode-se formar um triângulo')
else:
    print('não se pode formar um triângulo')
