#Leia o preço de um produto. Calcule um desconto de 10% e mosrte o valor do desconto e o preço a pagar.


preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.10
preco_a_pagar = preco - desconto
print(f"O valor do desconto é {desconto} e o preço a pagar é {preco_a_pagar}")