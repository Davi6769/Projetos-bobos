palavra = "jogo"
local = []
for letra in palavra:
    local.append("_")

while True:
    escolha = input("Chutar letra ou palavra?: ")

    if escolha == "letra":
        chute = input("chute: ")
        for numero, letra in enumerate(palavra):
            if chute == letra:
                local[numero] = chute

        print(local)

    else:
        chute = input("Chute a palavra: ")
        if chute == palavra:
            print("Voce acertou")
            print(palavra)
            break

        else:
            print("voce errou")