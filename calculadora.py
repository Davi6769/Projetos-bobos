#FUNÇÕES
def escolha1(operacao):
    n1 = int(input("digite um numero: "))
    n2 = int(input("digite outro numero: "))
    if operacao == 1:
        print(f"{n1} + {n2} = {n1 + n2}")
    elif operacao == 2:
        print(f"{n1} - {n2} = {n1 - n2}")
    elif operacao == 3:
        print(f"{n1} X {n2} = {n1 * n2}")
    elif operacao == 4:
        if n1 == 0:
            print("não é possivel dividir 0")
        else:
            print(f"{n1} / {n2} = {n1 / n2}")

def repeticao(operacao):
    while True:
        pergunta = input("gostaria de repetir o codigo ? [y/n]: ")
        while pergunta not in ["y", "n"]:
            print("resposta invalida")
            pergunta = input("gostaria de repetir o codigo ? [y/n]: ")
        if pergunta == "y":
            escolha1(operacao)
        else:
            break


#CALCULADORA
while True:
    print()
    print("CALCULADORA")
    opcoes = ["1-Soma", "2-Subtração", "3-Multiplicação", "4-Divisão", "0-sair"]
    for itens in opcoes:
        print(itens)
    escolha = int(input("Escolha a operação digitando o numero que esta na frente dele: "))

    while escolha not in [1, 2, 3, 4, 0]:
        print("resposta invalida")
        escolha = int(input("Escolha a operação digitando o numero que esta na frente dele: "))

    if escolha == 1:
        print("Você escolheu SOMA")
        escolha1(1)
        repeticao(1)

    elif escolha == 2:
        print("Você escolheu SUBTRAÇÃO")
        escolha1(2)
        repeticao(2)
    
    elif escolha == 3:
        print("Você escolheu MULTIPLICAÇÃO")
        escolha1(3)
        repeticao(3)
    
    elif escolha == 4:
        print("Você escolheu DIVISÃO")
        escolha1(4)
        repeticao(4)
    else:
        break


