import os
os.system("cls")

nome = str(input("Digite seu nome: "))
sexo = str(input("Digite seu Sexo: "))
sexo2 = 'F'
estado_civil = str(input("Digite seu estado civil atual: "))
casada = str
anos_de_casamento = 0

match estado_civil.lower():
   case "casada":
    if sexo.upper() =='F':
      anos_de_casamento = int(input("Quantos anos de casamento: "))
   case _:
      print("dados corretos")

print(f"Seus resultados foram: {nome},{sexo},{estado_civil},{anos_de_casamento}")