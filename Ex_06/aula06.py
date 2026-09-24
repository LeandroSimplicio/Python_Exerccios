# Leia a largura ea altura de um retângulo. Mostre a área e o perímetro.

largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = largura * altura
perimetro = 2 * (largura + altura)

print(f"A area do retângulo de largura {largura} e altura {altura} é {area}")
print(f"O perímetro do retângulo de largura {largura} e altura {altura} é {perimetro}")