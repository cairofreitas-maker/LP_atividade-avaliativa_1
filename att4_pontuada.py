import os 
os.system("cls")

kg_morango = float(input("Digite a quantidade de morangos (kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (kg): "))

if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

total = preco_morango + preco_maca
total_kg = kg_morango + kg_maca

if total_kg > 10 or total > 15:
    total = total * 0.90

print(f"Valor total a pagar: R$ {total:.2f}")
