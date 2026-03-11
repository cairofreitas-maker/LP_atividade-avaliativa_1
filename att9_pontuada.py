import os
os.system("cls")

renda = float(input("Digite sua renda mensal: R$ "))
valor_emprestimo = float(input("Digite o valor do empréstimo: "))
num_prestacoes = int(input("Digite o número de prestações: "))

valor_parcela = valor_emprestimo / num_prestacoes
limite_total = renda * 10
limite_parcela = renda * 0.30

if valor_emprestimo <= limite_total and valor_parcela <= limite_parcela:
    print("EMPRÉSTIMO CONCEDIDO")
    print(f"Valor da parcela: R${valor_parcela:.2f}")
else:
    print("EMPRÉSTIMO NEGADO")
    if valor_emprestimo > limite_total:
        print("O VALOR SOLICITADO EXCEDE 10 VEZES A SUA RENDA")
    if valor_parcela > limite_total:
        print(f"A PARCELA (R$ {valor_parcela:.2f})")