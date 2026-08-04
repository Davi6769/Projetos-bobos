#IMPORTS
from colorama import Fore, Style
from random import choice
from time import sleep


#FUNÇÕES
def repetir(escolha):
    while escolha not in ["1", "2"]:
        print(f"\n{Fore.RED}Resposta invalida{Style.RESET_ALL}")
        escolha = input("\nDigite somente o numero da opção desejada: ")
    return escolha


def senha_aleatoria():
    while True:
        print(f"\nGerando nova senha....")
        sleep(1)
        senha = []
        caracteres = ["a","b","c","d","e","f","g","h","j","i","k","l","n","m","o","p","q","r","s","t","u","v","x","y","z", "1", "2", "3", "4", "5", "6","7","8","9","0"]

        for i in range(8):
            escolher = choice(caracteres)
            senha.append(escolher)

        senha_final = "".join(senha)
        print(f"Sua senha nova é {senha_final.capitalize()}")

        nota = input("Gostou da senha gerada ? [y/n]: ").lower()

        while nota not in ["n", "y"]:
            print("Resposta invalida")
            nota = input("Gostou da senha gerada ? [y/n]: ").lower()

        if nota == "n":
            print()

        else:
            return senha_final


#GLOBAIS
opcoes = ["1-Registrar conta", "2-Acessar conta"]

opcoes2 = ["1-Criar senha", "2-Gerar senha"]

contas = []


#MENU
while True:
    print("=" * 40)
    print(f"\n Bem vindo ao nosso sistema de login\n")
    print("=" * 40)

    print("\nVocê gostaria de:")

    for i in opcoes:
        print(f"\n{i}")

    escolher = input("\nDigite somente o numero da opção desejada: ")

    escolher = repetir(escolher)

    print()

    #CRIANDO CONTA
    while True:
        if escolher == "1":
            print("=" *40)
            print("\nVocê escolheu Registrar conta\n")
            print("=" * 40)
            nome = input("\nPrimeiro digite seu nome de usuario: ")
            if nome in contas:
                print("Esse nome ja esta sendo usado")
                sleep(1)
                break

            gmail = input(f"agora digite seu email: ")

            if gmail in contas:
                print("Esse Email ja esta cadastrado")
                sleep(1)
                break

            while not gmail.endswith("@gmail.com"):
                print("Endereso de Gmail iinvalido")
                gmail = input(f"agora digite seu email: ")

            sleep(1)

            print(f"\nCerto {nome}, ja registramos o seu email: {gmail}\n")

            sleep(1)

            print("Agora digite sua senha (ou use nosso criador de senhas aleatorio, basta escolher uma das opções: )")
            for i in opcoes2:
                print(f"\n{i}")

            escolha = input("\nDigite somente o numero da opção desejada: ")
            escolha = repetir(escolha)

            if escolha == "1":
                senha = input("Escreva sua senha (de preferencia uma facil): ")
                print(f"Certo, seu nome é {nome}, seu gmail é {gmail} e sua senha é {senha}\n")
                contas.append(f"{nome}")
                contas.append(f"{gmail}")
                contas.append(f"{senha}")
                sleep(1)
                break

            else:
                senha = senha_aleatoria()
                print(f"Certo, seu nome é {nome}, seu gmail é {gmail} e sua senha é {senha}\n")
                sleep(1)
                contas.append(f"{nome}")
                contas.append(f"{gmail}")
                contas.append(f"{senha}")
                break
    #LOGIN
    if escolher == "2":
        print("=" * 40)
        print(f"\nVocê escolheu fazer login\n")
        print("=" * 40)
        nome = input("Digite seu nome de usuario: ")
        gmail = input("Digite seu gmail: ")
        senha = input("por fim digite sua senha: ")
        if nome in contas and gmail in contas and senha in contas:
            print(f"Bem vindo {nome}")
        else:
            print("Usuario não encontrado")




