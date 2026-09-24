# Leia o salário fixo de um vendedor e o total vendido no mês. Calcule uma comissão de 4% sobre as vendas e mostre a comissão e o salário total.

salario_fixo = int(input("Digite o salário fixo do vendedor: "))
total_vendas = int(input("Digite o total vendido no mês: "))
comissao = total_vendas * 0.04
salario_total = salario_fixo + comissao
print(f"A comissão de 4% sobre as vendas de {total_vendas} é {comissao} e o salário total é {salario_total}")