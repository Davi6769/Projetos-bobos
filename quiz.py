#FUNÇÕES
import time
pontos = 0
def ganhar_pontos(pontos):
    pontos += 1
    print()
    print("VOCÊ ACERTOUUU!!!")
    print("você ganhou um ponto")
    return pontos

def perder_pontos(pontos):
    pontos -= 1
    print()
    print("EEEEERRRROOOOOUUUUUUU, o bixinho burro em")
    print("você perdeu um ponto")
    return pontos

def repeticao(resposta):
    while resposta not in ["1","2","3","4"]:
        print("PQP você não sabe ler ne ? De boa, eu repito pra você")
        resposta = input("DIGITE SOMENTE O NUMERO DA QUESTÃO QUE VOCÊ ACHA SER A CORRETA!!!!: ")
    return resposta

def suspense(tempo):
    print("Você....")
    time.sleep(tempo)




#QUIZ Menu
while True:
    print("Bem vindo ao quiz dos genios")
    print()
    print(f"Vamos fazer 6 perguntas, e a cada pergunta que você acertar, você vai receber um ponto")
    print("Caso você termine o quiz com 3 pontos, você é alguem normal, caso seus pontos sejam menor que 3, você é burro e se os pontos forem 6 certinho, você é UM GENIO (ou sla)")
    print("Mas cuidado, caso você erre uma questão, você ira perder pontos....")

    print()
    perg = input("Você esta pronto ????? [y/n]: ")

    while perg not in ["y", "n"]:
        print("pqp você se você consegiu errar isso você não é capaz de fazer essa porra...")
        perg = input("Você esta pronto SIM (y) OU NÃO(y) ????? [y/n]")
        

    else:
        print("OTIMOOOOO !!!! vamos começar o quiz então:")
        break


    
#PRIMEIRA QUESTÃO   
print()
print("Primeira questãooo")
print("Quanto é 2 + 2 ?:")
alternativas = ["1: 3", "2: 4", "3: 1+1+1+1", "4: 8"]

for i in alternativas:
        print(i)

resposta = input("Digite somente o numero da questão que você acha ser a correta!: ")

resposta = repeticao(resposta)

if resposta in ["1", "2", "3"]:
    suspense(1)
    pontos = perder_pontos(pontos)
    print(f"pontos atuais = {pontos}")
else:
    suspense(1)
    pontos = ganhar_pontos(pontos)
    print(f"pontos atuais = {pontos}")

time.sleep(1)



#SEGUNDA QUESTÃO
print()
print("Segunda pergunta: ")
print("Antigamente farmacia começava com Ph, e hoje em dia ?")
alternativas = ["1-H","2-F","3-J","4-P"]
for i in alternativas:
    print(i)

resposta = input("Digite somente o numero da questão que você acha ser a correta!: ")

resposta = repeticao(resposta)

if resposta in ["2", "3", "4"]:
    suspense(1)
    pontos = perder_pontos(pontos)
    print(f"pontos atuais = {pontos}")
else:
    suspense(1)
    pontos = ganhar_pontos(pontos)
    print(f"pontos atuais = {pontos}")

time.sleep(1)



#TERCEIRA QUESTÃO
print()
print("6:Terceira pergunta: ")
print("89 + 820 x (5199 - 1293 + 6592 / 2) + o numero dessa questão = ?")
alternativas = ["1-5905729","2-123²","3-5905731","4-4,5555"]
for i in alternativas:
    print(i)

resposta = input("Digite somente o numero da questão que você acha ser a correta!: ")

resposta = repeticao(resposta)

if resposta in ["1", "2", "4"]:
    suspense(1)
    pontos = perder_pontos(pontos)
    print(f"pontos atuais = {pontos}")

else:
    suspense(1)
    pontos = ganhar_pontos(pontos)
    print(f"pontos atuais = {pontos}")

time.sleep(1)



#QUARTA QUESTÃO
print()
print("Quarta pergunta: ")
print("Qual desses animes é o melhor ?")
alternativas = ["1-Boruto","2-Classroom of the Elite","3-School days","4-No game no life"]
for i in alternativas:
    print(i)

resposta = input("Digite somente o que você acha ser a questão correta!: ")

if resposta in ["1", "2", "3", "4"]:
    suspense(1)
    pontos = perder_pontos(pontos)
    time.sleep(1)
    print()
    print("MDS, ja ouviu falar em banho ? Que nojo....")
    time.sleep(1)
    print()
    print(f"pontos atuais = {pontos}")

else:
    suspense(1)
    pontos = ganhar_pontos(pontos)
    print()
    time.sleep(1)
    print("Isso mesmo, todos esses animes são HORRIVEIS, fiquei orgulhoso de você em")
    time.sleep(1)
    print(f"pontos atuais = {pontos}")

time.sleep(1)


#QUINTA QUESTÃO
print()
print("Quinta pergunta: ")
print("Qual desses jogos tem o genero de sobrevivencia com blocos ?")
alternativas = ["1-Terraria","2-Minecraft","3-hypixel","4-Mario cart 8 remaster definitive edition"]
for i in alternativas:
    print(i)

resposta = input("Digite somente o numero da questão que você acha ser a correta!: ")

resposta = repeticao(resposta)

if resposta == "4":
    suspense(1)
    print()
    print("serio por que ??? Qual o sentido dessa resposta ?")
    time.sleep(1)
    print("adivinhaaa...")
    time.sleep(2)
    print("Você....")
    time.sleep(1)
    pontos = perder_pontos(pontos)
    print(f"pontos atuais = {pontos}")

else:
    suspense(1)
    pontos = ganhar_pontos(pontos)
    print(f"pontos atuais = {pontos}")

time.sleep(1)


#SEXTA QUESTÃO
print()
print("Sexta e ultima pergunta: ")
print("Agora para finalizar esse quiz....")
time.sleep(1)
print("me responda....")
time.sleep(1)
print("Você gostou do quiz ????? :3")
time.sleep(1)
alternativas = ["1-Com certeza","2-CLARO","3-SIIIIIM","4-eu amei você e o seu quiz"]
for i in alternativas:
    print(i)

resposta = input("Digite SOMENTE o numero da questão que você acha ser a correta!: ")

while resposta not in ["1","2","3","4", "não", "n", "no", "NÃO", "Não"]:
    print("PQP você não sabe ler ne ? De boa, eu repito pra você")
    resposta = input("DIGITE SOMENTE O NUMERO DA QUESTÃO QUE VOCÊ ACHA SER A CORRETA!!!!: ")


if resposta in ["1", "2", "4", "3"]:
    suspense(1)
    pontos = ganhar_pontos(pontos)
    time.sleep(0.6)
    print("Parabens por completar o quiz, vamos analizar as suas respsotas agora")
    print(f"Você teve um total de {pontos} pontos")
    time.sleep(0.5)
    print("Então....")
    time.sleep(1)
    if pontos == 6:
        print("VOCÊ É UM GENIO")
        time.sleep(0.5)
        print("meus parabens, você merece")
    elif pontos > 3:
        print("Você foi aceitavel, parabens")
    elif pontos == 3:
        print("Você ficou na media, n é um genio, mas tbm não é um imbecil")
    else:
        print("Você é um idiota.....")

elif resposta in ["não", "n", "no", "NÃO", "Não"]:
    time.sleep(2)
    print("...")
    time.sleep(1)
    print("como você ousa falar assim do meu quiz, VOCÊ TEM IDEIA DE COMO FOI DIFICIL FAZER ISSO ??? (na verdade n foi tanto)")
    time.sleep(1.4)
    print("MAS MESMO ASSIM, É MUITA OUSADIA DA SUA PARTE, EU QUERO QUE VOCÊ SAIBA QUE EU DECIDO SE VOCÊ GANHA PONTOS OU PERDE")
    time.sleep(1.4)
    print("OU SEJA EU DECIDO SE VOCÊ É INTELIGENTE OU NÃO")
    time.sleep(2)
    print("EU")
    time.sleep(0.5)
    print("SOU")
    time.sleep(0.5)
    print("DEEEEUSSSSS")
    time.sleep(0.3)
    print("XX Fatal Error, erro na linha 235, variavel não definida")



time.sleep(1)