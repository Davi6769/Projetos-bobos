from colorama import Fore, Style
from time import sleep

saldo = 0

def add_dinheiro(dinheiro):
    print(f" R$ {dinheiro} Adicionado")
    print(f"Saldo atualizado: R$ {dinheiro + saldo}")
    return dinheiro + saldo

def remover_dinheiro(dinheiro):
    if saldo < dinheiro:
        print(f"\n{Fore.RED}Imposivel retirar essa quantidade{Style.RESET_ALL}\n")
        sleep(1)

    else:
        print(f"R$ {dinheiro} Retirado com sucesso")
        return saldo - dinheiro

def repetir(continuar):
    while continuar not in ["n", "y"]:
        print(f"\n{Fore.RED}Resposta invalida{Style.RESET_ALL}\n")
        continuar = input("Deseja adicionar mais ? [n/y]: ")
    return continuar
    


opcao = ["(A)---Adicionar $ Dinheiro $", "(S)---Sacar -$ Dinheiro -$", "(V)---Ver Saldo atual", "(X)---Sair"]

#MENU
while True:
    print(f"{Fore.YELLOW}${Style.RESET_ALL}" * 40)
    print(f"\n{Fore.GREEN}Caixa Eletronico{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}${Style.RESET_ALL}" * 40)

    print("\nEscolha uma opção: \n")
    for i in opcao:
        print(i)

    escolha = input("Escolha a opção desejada: ").lower()

    while escolha not in ["a", "s", "v", "x"]:
        print(f"\n{Fore.RED}Resposta invalida{Style.RESET_ALL}")
        escolha = input("Escolha a opção desejada: ").lower()

    if escolha == "a":
        while True:
            dinheiro = int(input("\nDigite a quantidade que você deseja adicionar: R$ "))
            saldo = add_dinheiro(dinheiro)
            continuar = input("Deseja adicionar mais ? [n/y]: ")

            continuar = repetir(continuar)

            if continuar == "y":
                print()

            else:
                break
                

    elif escolha == "s":
        dinheiro = int(input("\nDigite a quantidade que você deseja retirar: R$ "))
        saldo = remover_dinheiro(dinheiro)


    elif escolha == "v":
        while True:
            print("Quantidade atual:")
            print(f"\nR$ {saldo}\n")
            sair = input("Aperte qualuqer tecla para sair: ")
            break

    else:
        break
