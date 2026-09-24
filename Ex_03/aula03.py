#Leia um número inteiro e moster o seu antecessor e sucessor.

numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"""O antecessor de {numero} 
      é:{antecessor}
      e o sucessor é {sucessor}""")