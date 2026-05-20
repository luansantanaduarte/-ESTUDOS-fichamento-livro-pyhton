# Pág. 90
# Exercício 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

deposito_inicial = float(input("Digite seu capital: "))
juros = float(input("Digite a taxa de juros: "))
juros_mensal = 0
juros_finais = 0
x = 1
while x <= 24:
  juros_mensal = deposito_inicial * juros
  deposito_inicial += juros_mensal
  print("No mês %d, o montante é igual a R$ %.2f" % (x, deposito_inicial))

  juros_finais += juros_mensal
  x += 1
print("Montante final: R$ %.2f" % juros_finais)