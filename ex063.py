n = int(input("Digite o número de termos da sequência de Fibonacci que deseja ver: "))

# verifica se n é menor ou igual a zero
if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    # inicializa os dois primeiros termos da sequência
    primeiro_termo = 0
    segundo_termo = 1
    # imprime o primeiro termo (0) da sequência
    print(primeiro_termo)
    # imprime o segundo termo (1) da sequência
    print(segundo_termo)

    # calcula e imprime os demais termos da sequência
    i = 2
    while i < n:
        # calcula o próximo termo da sequência
        proximo_termo = primeiro_termo + segundo_termo
        # imprime o próximo termo da sequência
        print(proximo_termo)
        # atualiza os valores dos termos anteriores
        primeiro_termo = segundo_termo
        segundo_termo = proximo_termo
        i += 1
