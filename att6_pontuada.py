import os
os.system("cls")

nota1 = float
nota2 = float
media = float

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

soma = nota1 + nota2
media = soma / 2

if media >= 6:
    print("PARABENS VOCE ESTA APROVADO")
elif media == 6:
    print("NAO PASSOU")
else:
    print("REPROVADO")

print(f"Sua nota final é: {media}")