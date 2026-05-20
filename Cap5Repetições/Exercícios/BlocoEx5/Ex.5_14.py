# Pág. 91
# Exercício 5.14 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

soma = 0
acumulador = 0
numeros = []

while True:
  n = int(input("Digite valores: "))
  soma += n
  if n == 0:
    media = soma / acumulador
    print("Quantidade de números digitados: %d" % acumulador)
    print("A soma dos números é: %d" % soma)
    print("A média é: %.2f" % media)
    break
  else:
    acumulador += 1
