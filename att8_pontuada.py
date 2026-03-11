import os 
os.system("cls")

cor = input("Digite a cor do CD desejada: ").lower()

if cor == "verde":
    preco = 10
elif cor == "azul":
    preco = 20
elif cor == "amarelo":
    preco = 30
elif cor == "vermelho":
    preco = 40 
else:
    preco = None

if preco != None:
    print("O preço do CD é ", {preco})
else:
    print("cor inválida")