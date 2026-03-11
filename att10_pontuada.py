import os
os.system("cls")

litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Tipo de combustível (A-Alcool, G-Gasolina): ")

preco_gasolina = 6.59
preco_alcool = 3.79
valor_final = 0

if tipo == 'A':
    if litros <= 20:
     valor_final = litros * (preco_alcool * 0.97)
    else:
     valor_final = litros * (preco_alcool * 0.95)
elif tipo == 'G':
  if litros <=20:
    valor_final = litros * (preco_gasolina * 0.96)
  else:
    print("Tipo de combustível inválido")
if valor_final > 0:
 print(f"Total a pagar: R${valor_final:.2f}")