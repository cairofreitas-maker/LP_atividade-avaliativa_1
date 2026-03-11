import os 
os.system("CLS")

A = int(input("Digite um número de 0 á 10: "))
B = int(input("Digite um número de 0 á 10: "))
C = int(input("Digite um número de 0 á 10: "))

soma = A + B

if soma< C:
    print("este número é maior que A e B")
else:
    print("este número é menor que C")