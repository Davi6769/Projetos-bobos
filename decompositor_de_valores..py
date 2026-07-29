#DECOMPOSITOR

#FUNÇÕES

def mostrar(valor, moeda):
    print(f"{valor // moeda} moedas de {moeda}")

def decompositor(valor, moeda):
    mostrar(valor, moeda)
    return valor % moeda

#MENU
dinheiro = [500, 200, 100, 50, 20, 10, 5, 1]

print("Bem vindo ao conversedor de moedas")
print()
print("Vamos separar os valores entre: ")
for i in dinheiro:
    print(i)
print()

while True:
    valor = int(input("Digite o valor: "))

    moeda_500 = decompositor(valor, 500)
    moeda_200 = decompositor(moeda_500, 200)
    moedas_100 = decompositor(moeda_200, 100)
    moedas_50 = decompositor(moedas_100, 50)
    moedas_20 = decompositor(moedas_50, 20)
    moedas_10 = decompositor(moedas_20, 10)
    moedas_5 = decompositor(moedas_10, 5)
    moedas_1 = decompositor(moedas_5, 1)

    pergunta = input("gostaria de repetir o programa ? [n/y]: ")

    while pergunta not in ["y", "n"]:
        print("Resposta invalida")
        pergunta = input("gostaria de repetir o programa ? [n/y]: ")

    if pergunta == "y":
        print("certo, repetindo")

    else:
        break
