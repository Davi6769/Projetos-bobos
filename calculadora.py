from colorama import Fore, Style
from time import sleep

opcoes = ["(1)-Soma", "(2)-Subtração", "(3)-Multiplicação", "(4)-Divisão", "(X)-Sair"]
fim = 0


def voltar():
    volta = input("Digite qualuqer tecla para voltar a area inicial: ")

def menu():
    for i in opcoes:
        print(f"\n{i}")

    escolha = input("\nEscolha digitando somente o numero da opção desejada: ").lower()

    while escolha not in ["1", "2", "3", "4", "x"]:
        print(f"{Fore.RED}Resposta invalida{Style.RESET_ALL}")
        escolha = input("Escolha digitando somente o numero da opção desejada: ")
    return escolha
  

def numeros():
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite outro numero: "))
    return numero1, numero2

def soma():
    print("\nVocê escolheu soma")
    numero1, numero2 = numeros()
    resposta = numero1 + numero2
    print(f"A soma de {numero1} por {numero2} é igual a {resposta}")
    print(f"{numero1} + {numero2} = {resposta}")
    voltar()

def subtracao():
    print("\nVocê escolheu subtração")
    numero1, numero2 = numeros()
    resposta = numero1 - numero2
    print(f"{numero1} - {numero2} = {resposta}")
    voltar()

def multiplicacao():
    print("\nVocê escolheu multiplicação")
    numero1, numero2 = numeros()
    resposta = numero1 * numero2
    print(f"{numero1} X {numero2} = {resposta}")
    voltar()

def divisão():
    print("\nVocê escolheu divisão")
    numero1, numero2 = numeros()
    while numero2 == 0:
        print(f"{Fore.RED}Resposta invalida: imposivel dividir por zero{Style.RESET_ALL}")
        numero1, numero2 = numeros()
    resposta = numero1 / numero2
    print(f"{numero1} / {numero2} = {resposta}")
    voltar()

def decidir(escolha):
    if escolha == "1":
        soma()

    elif escolha == "2":
        subtracao()

    elif escolha == "3":
        multiplicacao()

    elif escolha == "4":
        divisão()

    else:
        fim = 1
        return fim



#CALCULADORA


titulo = """
      /$$$$$$            /$$                     /$$                 /$$                             
     /$$__  $$          | $$                    | $$                | $$                             
    | $$  \__/  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$ 
    | $$       |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$|____  $$
    | $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$| $$  | $$| $$  \ $$| $$  \__/ /$$$$$$$
    | $$    $$ /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$| $$  | $$| $$  | $$| $$      /$$__  $$
    |  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$     |  $$$$$$$
    \______/  \_______/|__/ \_______/ \______/ |__/ \_______/ \_______/ \______/ |__/      \_______/
    """

while True:

    print("=" * 40)
    print(f"\n{titulo}\n")
    print("=" * 40)

    escolha = menu()

    fim = decidir(escolha)

    if fim == 1:
        break
