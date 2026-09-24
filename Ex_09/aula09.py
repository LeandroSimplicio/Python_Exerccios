# Leia o salário de um funcionário e mostre o valor do aumento de 15% e o novo salário.

salario = float(input("Digite o salário do funcionário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f"O aumento de 15% de {salario} é {aumento} e o novo salário é {novo_salario}")