#Leia a temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura de {celsius} em Fahrenheit é {fahrenheit}")