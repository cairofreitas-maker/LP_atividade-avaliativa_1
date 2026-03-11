import os 
os.system("cls")

A = int(input("Digite um número para somar: "))
B = int(input("Digite um segundo número para somar: "))

soma = A + B
multiplicacao = A * B

if A==B:
    print(f"A soma é: {soma}")
else:
    print(f"A multiplicação é: {multiplicacao}")