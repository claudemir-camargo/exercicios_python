# 13 – Criar um programa que preenche uma Matriz de 10 linhas com 10 colunas. Exibir a matriz
# na tela. O programa deve então gerar uma segunda matriz que tem como base a primeira:
# Se o número da linha for igual ao número da coluna, colocar o valor "1" na posição.
# Se o número da linha for menor que o número da coluna, colocar o valor "0".
# Se o número da linha for maior que o número da coluna, colocar o valor "2".
# Exibir a segunda matriz na tela.

matriz1 = [[i * 10 + j for j in range(10)] for i in range(10)]

print("Primeira matriz:")
for linha in matriz1:
    print(linha)

matriz2 = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        if i == j:
            matriz2[i][j] = 1
        elif i < j:
            matriz2[i][j] = 0
        else:
            matriz2[i][j] = 2

print("\nSegunda matriz:")
for linha in matriz2:
    print(linha)
