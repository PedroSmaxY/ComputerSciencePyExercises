extenso = {0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
           6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
           11: 'onze', 12: 'doze', 13: 'treze', 14: 'catorze', 15: 'quinze',
           16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte'}

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente.', end=' ')

print(f'Você digitou o número {extenso[numero]}')
