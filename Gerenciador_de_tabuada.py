
while True:
    print("Bem vindo ao criador de tabuada (ate o 10)")
    numero = int(input("Digite o numero que você deseja ver a tabuada: "))

    for i in range(1, 11):
        print(f"{i} X {numero} = {i * numero}")
    
    pergunta = input("Gostaria de repetir o programa ? [n/y]: ")

    while pergunta not in ["y", "n"]:
        print("resposta invalida")
        pergunta = input("Gostaria de repetir o programa ? [n/y]: ")

    if pergunta == "n":
        break
    else:
        print("ok")

