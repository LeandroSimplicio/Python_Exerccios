# Leia um número inteiro e informe se ele é par ou ímpar.

# Regra : Um número é par se o resto da divisão por 2 for igual a 0, caso contrário, é ímpar.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")



113