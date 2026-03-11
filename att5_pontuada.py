import os
os.system("cls")

A = int(input("Digite um número: "))
B = int(input("Digite um segundo número: "))
operacao = (input("Digite a operação desejada: "))

match operacao:
    case "+":
        print(f"{A+B}")
    case "-":
        print(f"{A-B}")
    case "/":
        print(f"{A/B}")
    case "*":
        print(f"{A*B}")
    case _:
        print(f"O VALOR DOS NÚMEROS DEU: {operacao}")