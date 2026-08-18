titulo = """
     ██  ██████   ██████   ██████      ██████   █████      ███████  ██████  ██████   ██████  █████  
     ██ ██    ██ ██       ██    ██     ██   ██ ██   ██     ██      ██    ██ ██   ██ ██      ██   ██ 
     ██ ██    ██ ██   ███ ██    ██     ██   ██ ███████     █████   ██    ██ ██████  ██      ███████ 
██   ██ ██    ██ ██    ██ ██    ██     ██   ██ ██   ██     ██      ██    ██ ██   ██ ██      ██   ██ 
 █████   ██████   ██████   ██████      ██████  ██   ██     ██       ██████  ██   ██  ██████ ██   ██ 
                                                                                                    
                                                                                                    """

from time import sleep
from colorama import Fore, Style
from random import choice

#VARIAVEIS IMPORTANTES
palavras = ["abajur", "pneu", "parafuso", "prego", "alicate", "chaveiro", "toalha", "escova", "sabonete", "shampoo", "perfume", "espelho", "pente", "secador", "travesseiro", "cobertor", "lençol", "colchão", "cama", "armário", "cabide", "gaveta", "estante", "livro", "caderno", "borracha", "apontador", "regua", "mochila", "estojo", "tesoura", "cola", "papel", "pasta", "clipe", "grampeador", "caneta", "lápis", "marcador", "tintas", "pincel", "tela", "quadro", "moldura", "vaso", "planta", "flor", "folha", "semente", "terra", "adubo", "jardim", "grama", "árvore", "galho", "fruto", "raiz", "pedra", "areia", "cascalho", "rocha", "montanha", "colina", "vale", "rio", "lago", "lagoa", "mar", "oceano", "onda", "praia", "ilha", "vulcão", "caverna", "deserto", "floresta", "selva", "campo", "caminho", "trilha", "estrada", "rua", "avenida", "ponte", "túnel", "viaduto", "praça", "parque", "banco", "poste", "farol", "sinal", "faixa", "calçada", "muro", "portão", "cerca", "casa", "prédio", "apartamento", "telhado", "chaminé", "janela", "porta", "maçaneta", "campainha", "degrau", "escada", "elevador", "garagem", "carro", "moto", "caminhão", "ônibus", "trem", "metrô", "avião", "helicóptero", "foguete", "nave", "satélite", "barco", "navio", "submarino", "canoa", "caiaque", "balsa", "âncora", "remo", "vela", "motor", "roda", "volante", "buzina", "espelho", "pedal", "freio", "bateria", "fio", "tomada", "interruptor", "lâmpada", "lanterna", "vela", "fogo", "fumaça", "cinza", "carvão", "caldeira", "forno", "fogão", "panela", "frigideira", "chaleira", "bule", "copo", "xícara", "caneca", "prato", "tigela", "talher", "garfo", "faca", "colher", "concha", "espatula", "peneira", "ralo", "pia", "torneira", "esponja", "balde", "vassoura", "rodo", "pá", "lixo", "saco", "pano", "detergente", "geladeira", "freezer", "micro-ondas", "liquidificador", "batedeira", "cafeteira", "torradeira", "ventilador", "televisão", "rádio", "computador", "teclado", "mouse", "fone", "caixa", "câmera", "celular", "relógio", "bússola", "mosaico", "escultura", "engrenagem", "ampulheta", "diamante", "troféu", "tambor", "violão", "violino", "teia", "corrente", "capacete", "sorvete", "capacete", "martelo", "bateria", "passaporte", "girassol", "cachoeira""computador", "universo", "gaveta", "pirâmide", "coruja", "paraquedas", "estátua", "microfone", "tambor", "satélite", "mochila", "armário", "mosaico", "cacto", "labirinto", "sorvete", "capacete", "engrenagem", "sombra", "neblina", "fogueira", "fantasma", "corrente", "almofada", "troféu", "espada", "diamante", "teia", "ampulheta", "espelho", "martelo", "bússola", "floresta", "telescópio", "castelo", "vulcão", "foguete", "oceano", "planeta", "violino", "escultura", "portal", "âncora", "lanterna", "máscara", "buzina", "bicicleta", "passaporte", "girassol", "cachoeira""oceano", "foguete", "chave", "espada", "lanterna", "travesseiro", "bússola", "moeda", "espelho", "martelo", "caderno", "ampulheta", "diamante", "disco", "floresta", "planeta", "vulcão", "castelo", "sino", "pincel", "escultura", "máscara", "telescópio", "bateria", "violino", "vela", "imã", "engarrafamento", "labirinto", "portal","cadeira", "espelho", "nuvem", "livro", "lanterna", "girassol", "violão", "relógio", "janela", "bicicleta", "mochila", "caneta", "sapato", "garrafa", "telefone"]

#FUNÇÂOS

def repetidor(escolha):
    while escolha not in ["x", "j"]:
        print(f"{Fore.RED}Resposta invalida{Style.RESET_ALL}")
        escolha = input("Digite SOMENTE a letra da opção desejada: ").lower()
    return escolha


def desenhos(erros):
    desenho1 = """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """

    desenho2 = """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """

    desenho3 = """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """

    desenho4 = """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """

    desenho5 = """
    +---+
    |   |
    O   |
   /|\\ |
        |
        |
    =========
    """

    desenho6 = """
    +---+
    |   |
    O   |
   /|\\ |
   /    |
        |
    =========
    """

    desenho7 = """
     +---+
     |   |
     O   |
    /|\\ |
    / \\ |
         |
    =========
    """

    desenho8 = """
     +---+
     |   |
     x   |
    /|\\ |
    / \\ |
         |
    =========
    """

    if erros == 0:
        print(desenho1)

    elif erros == 1:
        print(desenho2)

    elif erros == 2:
        print(desenho3)

    elif erros == 3:
        print(desenho4)

    elif erros == 4:
        print(desenho5)

    elif erros == 5:
        print(desenho6)

    elif erros == 6:
        print(desenho7)
    elif erros == 7:
        print(desenho8)


#MENU
while True:
    print("=" * 40)
    print(titulo)
    print("=" * 40)
    opcoes = ["(J)----Jogar", "(X)----Sair"]

    for i in opcoes:
        print(f"\n{i}")

    escolha = input("\nDigite somente a letra da opção desejada: ").lower()
    escolha = repetidor(escolha)
    palavra_escolhida = choice(palavras)
    local = []
    if escolha == "j":
        print("Vamos iniciar o jogo")
        sleep(1)
        print("Escolhendo a palavra....")
        sleep(2)

        for i in palavra_escolhida:
            local.append("_")

        erros = 0
        print("palavra escolhida")
        letras_incorretas = []
        
        while True:
            desenhos(erros)
            print(local)
            print(f"\nErros: {Fore.RED}{letras_incorretas}{Style.RESET_ALL}")
            escolha = input("Voce deseja chutar uma letra ou uma palavra ?: ").lower()

            while escolha not in ["palavra", "letra"]:
                print("Resposta incorreta, digite somente letra ou palavra")
                escolha = input("Voce deseja chutar uma letra ou uma palavra ?: ").lower()

            if escolha == "letra":
                chute = input("Chute uma letra: ")
                for numero, letra in enumerate(palavra_escolhida):
                    if letra == chute:
                        sleep(1)
                        local[numero] = chute
                if "_" not in local:
                    print("Voce ganhouj")
                    break


                if chute not in palavra_escolhida:
                    sleep(1)
                    erros += 1
                    letras_incorretas.append(chute)

            else:
                chute = input("Chute uma palvra: ")
                if chute == palavra_escolhida:
                    print(f"{Fore.GREEN}Você acertou na mosca{Style.RESET_ALL}")
                    sleep(1)
                    break
                else:
                    erros += 1
                    print("Resposta incorreta")
                    sleep(1)

            if erros == 7:
                desenhos(erros)
                print(f"{Fore.RED}Game ouver{Style.RESET_ALL}")
                print(f"palavra escolhida: {palavra_escolhida}")
                input("aperte qualquer tecla para voltar: ")
                break
    else:
        break        
            



