from time import sleep
import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

senha = []

print(f"=" * 40)
print(f"\nGerador de senhas aleatorias\n")
print(f"=" * 40)

iniciar = input(f"\nAperte qualquer botão para gerar uma senha: ")

for i in range(8):
    escolha = random.choice(letras)
    senha.append(escolha)

print(f"\nSua nova senha é: {"".join(senha).title()}")
