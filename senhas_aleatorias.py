from time import sleep
import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numeros = ["1", "2", "3", "4", "5","6","7","8","9"]

caracteres = letras + numeros

senha = []

print(f"=" * 40)
print(f"\nGerador de senhas aleatorias\n")
print(f"=" * 40)

iniciar = input(f"\nAperte qualquer botão para gerar uma senha: ")

for i in range(8):
    escolher = random.choice(caracteres)
    senha.append(escolher)

senha_final = "".join(senha)

print(f"\nSua nova senha é: {senha_final.title()}")
