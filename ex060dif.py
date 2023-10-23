x = int(input("Digite um número: "))
fat = 1
i = x
print(f"{x}! = ", end="")
while i >= 1:
    fat *= i
    if i == 1:
        print(f"{i} = {fat}")
    else:
        print(f"{i} * ", end="")
    i -= 1
