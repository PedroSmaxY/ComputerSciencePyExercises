from math import pow
peso = float(input('Digite seu peso em kilos: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / pow(altura, 2)
if imc < 18.5:
    print('O seu imc é de {:.2f}, isso o configura como abaixo do peso!'.format(imc))
if 18.5 < imc < 24.9:
    print('O seu imc é de {:.2f}, isso o configura com o peso ideal!!'.format(imc))
if 25 < imc < 29.9:
    print('O seu imc é de {:.2f}, isso o configura com sobrepeso!!'.format(imc))
if 30 < imc < 39.9:
    print('O seu imc é de {:.2f}, isso o configura com obesidade!!'.format(imc))
if imc > 40:
    print('O seu imc é de {:.2f}, isso o configura com obesidade mórbida!!'.format(imc))
