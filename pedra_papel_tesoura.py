

#JOGO
vitorias = 0
derrotas = 0
while True:
    import random
    opcoes_do_pleyer = ["1-pedra","2-papel","3-tesoura", "0-não quero joga"]
    opcoes = ["pedra","papel","tesoura"]

    jogada = random.choice(opcoes)

    print("vamos jogar pedra papel e tesoura")
    print()

    for intem in opcoes_do_pleyer:
        print(intem)


    escolha = int(input("Escolha uma das opções digitando somente o numero da opção desejada: "))

    while escolha not in [1, 2, 3, 0]:
        print("resposta invalida")
        escolha = int(input("Escolha uma das opções digitando somente o numero da opção desejada: "))
        print()

    #se voce joga pedra
    if escolha == 1 and jogada == "pedra":
        print("empate")
    elif escolha == 1 and jogada == "tesoura":
        print("você ganhou!!!")
        vitorias += 1
        print(f"Ate agora você ganhou {vitorias} vezes")
    elif escolha == 1 and jogada == "papel":
        print("Você perdeu")
        derrotas += 1
        print(f"Ate agora você perdeu {derrotas} vezes")

    #se voce joga papel
    elif escolha == 2 and jogada == "pedra":
        print("você ganhou !!")
        vitorias += 1
        print(f"Ate agora você ganhou {vitorias} vezes")
    elif escolha == 2 and jogada == "tesoura":
        print("você perdeu")
        derrotas += 1
        print(f"Ate agora você perdeu {derrotas} vezes")
    elif escolha == 2 and jogada == "papel":
        print("Empare, ninguem ganhou ponto")

    #se voce joga tesoura
    elif escolha == 3 and jogada == "pedra":
        print("Você perdeu")
        derrotas += 1
        print(f"Ate agora você perdeu {derrotas} vezes")
    elif escolha == 3 and jogada == "tesoura":
        print("Empate")
    elif escolha == 3 and jogada == "papel":
        print("Você ganhou !!")
        vitorias += 1
        print(f"Ate agora você ganhou {vitorias} vezes")
    else:
        break


    print(f"Seus pontos: {vitorias}")
    print(f"Meus pontos: {derrotas}")

    pergunta = input("gostaria de jogar de novo ? [y/n]: ")
    while pergunta not in ["y", "n"]:
        print("resposta invalida")
        pergunta = input("gostaria de jogar de novo ? [y/n]: ")
    if pergunta == "y":
        print("ok, vamos la ent")
        print()
    else:
        print("pontuação final:")
        print()
        print(f"Seus pontos: {vitorias}")
        print(f"Meus pontos: {derrotas}")
        if vitorias > derrotas:
            print("você ganhou esse jogo, parabens!")
        elif vitorias < derrotas:
            print("Você perdeu esse jogo, que decepição")
        else:
            print("nossa, empatamos")

        break

