import os 
os.system("cls")

preco = float
produto = float 

nome = (input("Digite o nome do produto: "))
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

soma = preco * produto

if quantidade <= 5:
    desconto = soma * 0.02
elif quantidade <= 10:
    desconto = soma * 0.03
else:
    desconto = soma * 0.05

total_pagar = soma - desconto

print("\nproduto: ", nome)
print("Total: ", soma)
print("Desconto: ", desconto)
print("Total a pagar: ", total_pagar)