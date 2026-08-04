#FUNÇÕES
def repeticao(denovo):
    while denovo not in ["y", "n"]:
        print("resposta invalida")
        denovo = input("gostaria de repetir a conta [n/y]: ")
    return denovo



def temperaturas(escolha):
    #C-F
    if escolha == "1":
        print()
        print("Você escolheu converter: Celcios(C) para Fahrenheit(F)")
        print()

        while True:   
            temperatura = int(input("Digite a temperatura em celcios(C): "))
            conta = (temperatura * 1.8) + 32
            print(f"F = ({temperatura} X 1,8) + 32 = {conta}")

            denovo = input("gostaria de repetir a conta [n/y]: ")

            denovo = repeticao(denovo)

            if denovo == "y":
                print("Ok")
                continue
            else:
                break

    #F-C
    elif escolha == "2":
        print()
        print("Você escolheu converter: Fahrenheit(F) para Celcios(C)")
        print()

        while True:   
            temperatura = int(input("Digite a temperatura em Fahrenheit(F): "))
            conta = (temperatura - 32) * (5/9)
            print(f"C = ({temperatura} - 32) X (5/9) = {conta}")

            denovo = input("gostaria de repetir a conta [n/y]: ")

            denovo = repeticao(denovo)

            if denovo == "y":
                print("Ok")
                continue
            else:
                break


    #C-K
    elif escolha == "3":
        print()
        print("Você escolheu converter: Celcios(C) para Kelvin(K)")
        print()

        while True:   
            temperatura = int(input("Digite a temperatura em Celcios(C): "))
            conta = temperatura + 273
            print(f"K = {temperatura} + 273 = {conta}")

            denovo = input("gostaria de repetir a conta [n/y]: ")

            denovo = repeticao(denovo)

            if denovo == "y":
                print("Ok")
                continue
            else:
                break       


    #K-C
    elif escolha == "4":
        print()
        print("Você escolheu converter: Kelvin(K) para Celcios(C)")
        print()

        while True:   
            temperatura = int(input("Digite a temperatura em Kelvin(K): "))
            conta = temperatura - 273
            print(f"C = {temperatura} - 273 = {conta}")

            denovo = input("gostaria de repetir a conta [n/y]: ")

            denovo = repeticao(denovo)

            if denovo == "y":
                print("Ok")
                continue
            else:
                break       
    


#MENU
print("Conversor de temperaturas.")


while True:
    print()
    print("Escolha para qual temperatura você queira converter: ")
    print()

    temperaturas_Menu = ["1-Celcios para Fahrenheit", "2-Fahrenheit para Celcios", "3-Celcios para Kelvin", "4-Kelvin para Celcios", "", "5-Sair"]

    for i in temperaturas_Menu:
        print(i)

    print()

    while True:
        escolha = input("Escolha a opção desejada digitando somente o numero da opção: ")

        if escolha not in ["1", "2", "3", "4","5"]:
            print("Resposta invalida")
            continue
        else:
            break
    if escolha == "5":
        break
    
#CONVENÇÃO
    temperaturas(escolha)

