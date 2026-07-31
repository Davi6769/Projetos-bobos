from colorama import Fore, Style
import time

#FUNCÕES

def cronometroS():
    minutos = 0
    horas = 0
    while True:
        segundos = 0
        while segundos < 60:
            print(f"{horas}:{minutos}:{segundos}")
            time.sleep(1)
            segundos +=1

        if segundos == 60:
            minutos += 1
            print(f"{horas}:{minutos}:{segundos}")

        if minutos == 60:
            minutos = 0
            horas += 1
            print(f"{horas}:{minutos}:{segundos}")


#MENU
print("\n" + "=" * 40)
print("CRONOMETRO")
print("=" * 40)
escolha = input(f"\nDigite{Fore.GREEN} ok {Style.RESET_ALL}para iniciar o cronometro: ").lower()

while escolha != "ok":
    print(f"{Fore.RED} Resposta Invalida {Style.RESET_ALL}")
    escolha = input(f"\nDigite{Fore.GREEN} ok {Style.RESET_ALL}para iniciar o cronometro: ").lower()

if escolha == "ok":
    cronometroS()

