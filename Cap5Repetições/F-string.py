# F-string
# ! F-string -> A partir dessa funcionalidade, é possível formatar saídas, de modo a incluir váriaiveis
# ? Sintaxe print(f"{variavel}")

a = "Mundo"
print(f"Olá, {a}")
# Programa equivalente a "Alô %s" % a ou até mesmo "Alô, {}" .format(a)

# É possível:
preco = 5.20
print(f"O preço é {preco:.1f}") # Definir quantidade de número após a vírgula
print(f"O preço é {preco:10.2f}") # Definir um espaçamento a esquerda

# * É possível formatar a partir do uso de <, > ou ^, para alinhar respectivamente à esquerda, direita ou centro

# Os espaços em branco podem ser preenchidos com caracteres:
print(f"O preço é {preco:.>25.2f}") # À direita
print(f"O preço é {preco:.<25.2f}") # À esquerda
print(f"O preço é {preco:.^10.2f}") # Em ambos os lados