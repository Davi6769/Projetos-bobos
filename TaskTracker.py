#TAASK TRACKER

#VARIAVEIS
opcao = ["1-Adicionar Tarefas", "2-Remover Tarefas", "3-Ver tarefas atuais"]
tarefas = []

#MENU
print("Bem vindo ao seu gerenciador de tarefas")
print()
print("Aqui você pode adicionar tarefas, remover tarefas")

while True:
    print()
    print("qual das opções você vai escolher: ")
    print()
    for i in opcao:
        print(i)
    print()
    escolha = input("Escreva somente o numero da opção desejada: ")

    while escolha not in ["1", "2", "3"]:
        print("Resposta incorreta")
        escolha = input("Escreva somente o numero da opção desejada: ")
    print()

#TAREFAS

#ADICIONAR TAREFAS
    if escolha == "1":
        print("Você escolheu: Adicionar tarefas (Digite somente: N ou n para encerrar a ação)")
        print()
        while True:
            add_tarefas = input("Adicione sua tarefa: ")

            if add_tarefas in ["n", "N"]:
                break
            else:
                print(f"{add_tarefas} adicionado")
                tarefas.append(add_tarefas)

#REMOVER TAREFAS

    elif escolha == "2":
        if len(tarefas) == 0:
            print("Nenhuma terefa para remover")

        else:
            while True:
                print("Você escolheu: remover tarefas (Digite somente: N ou n para encerrar a ação)")
                
                print(f"Tarefas Atuais = {len(tarefas)}")
                for i in tarefas:
                    print(i)

                add_tarefas = input("Remova a tarefa desejada: ")

                if add_tarefas == "n":
                    break

                while add_tarefas not in tarefas:
                    print("Essa tarefa não existe, lembre de escrever a tarefa que vc deseja excluir corretamente")
                    add_tarefas = input("Remova a tarefa desejada: ")

                print(f"{add_tarefas} foi removido")
                tarefas.remove(add_tarefas)


#VER TAREFAS

    elif escolha == "3" and len(tarefas) == 0:
        print("Nenhuma tarefa pendente")

    elif escolha == "3":
        print(f"Tarefas Atuais: {len(tarefas)}")
        for i in tarefas:
            print(i)
