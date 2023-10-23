n = int(input('Digite um valor inteiro: '))
primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
        break
if primo:
    print(f'O número {n} é um número primo')
else:
    print(f'O número {n} não é um número primo')
