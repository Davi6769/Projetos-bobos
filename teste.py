def escolha(operacao):
    n1 = int(input("digite um numero: "))
    n2 = int(input("digite outro numero: "))
    if operacao == "+":
        print(f"{n1} + {n2} = {n1 + n2}")
    elif operacao == "-":
        print(f"{n1} - {n2} = {n1 - n2}")
    elif operacao == "*":
        print(f"{n1} X {n2} = {n1 * n2}")
    elif operacao == "/":
        print(f"{n1} / {n2} = {n1 / n2}")

escolha("-")