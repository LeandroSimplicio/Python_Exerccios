#Leia dois valores inteiors, armazene-os em A e B e troque seus conteúdos. Ao fina, mostre os valores depois da troca.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

a, b = b, a

print(f"A = {a} e B = {b}")