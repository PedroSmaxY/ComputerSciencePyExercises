lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON')

for palavra in lista:
    vogais = ""
    for letra in palavra:
        if letra in "aeiouAEIOU":
            vogais += letra + " "
    print(f"Vogais na palavra '{palavra}': {vogais}")
