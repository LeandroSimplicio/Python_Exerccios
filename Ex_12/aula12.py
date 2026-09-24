#Leia o preço unitário de um produto, a quantidade comprada e o valor do frete. Mostre o subtoral dos produtos e valor total da compra.

preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
frete = float(input("Digite o valor do frete: "))

sub_total = preco_unitario * quantidade
total = sub_total + frete

print(f"O subtotal dos produtos e R${sub_total:.2f} e o valor total da compra e R${total:.2f}")