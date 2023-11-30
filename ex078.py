print("====================================")
print("Calculadora Simples")
print("====================================")
numeroUm = int(input('Digite um número: '))
numeroDois = int(input('Digite outro número: '))
print("====================================")
print("Escolha a operação: ")
print("====================================")
print("[ + ] - Soma")
print("[ - ] - Subtração")
print("[ x ] - Multiplicação")
print("[ / ] - Divisão")
print("====================================")
opcao = str(input('Digite a opção: '))
print("====================================")
if opcao == "+":
    print(f"{numeroUm} + {numeroDois} = {numeroUm + numeroDois}")
elif opcao == "-":
    print(f"{numeroUm} - {numeroDois} = {numeroUm - numeroDois}")
elif opcao == "x":
    print(f"{numeroUm} x {numeroDois} = {numeroUm * numeroDois}")
elif opcao == "/":
    if numeroDois == 0:
        print("Não é possível dividir por zero!")
    print(f"{numeroUm} / {numeroDois} = {numeroUm / numeroDois}")
else:
    print("Opção inválida!")
