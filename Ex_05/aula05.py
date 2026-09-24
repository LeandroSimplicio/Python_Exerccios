#Ler uma medida em metros e exibir convertida em centímetros e milímetros.

medida = float(input("Digite a medida em metros: "))
cm = medida * 100
mm = medida * 1000
print(f"A medida de {medida} em cm é {cm} e em mm é {mm}")