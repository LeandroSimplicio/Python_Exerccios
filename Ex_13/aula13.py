# Leia um número real e informe se ele é positivo, negativo ou zero.

numero = float(input("Digite um número real: "))

if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número é zero.")  