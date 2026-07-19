import random

numero = random.randint(1,100)

resposta = int(input("tente adivinhar o numero que eu estou pensando: "))
tentativas = 0
while resposta != numero:
    tentativas += 1
    if resposta < numero:
        print("o numero que eu estou pensando é maior")
        resposta = int(input("tente de novo: "))
    else:
        print("o numero que eu estou pensando é menor")
        resposta = int(input("tente de novo: "))

print(f"vc acertou, e demorou so {tentativas} tentativas!!!!")