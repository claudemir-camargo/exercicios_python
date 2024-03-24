# 14 – Criar um programa que leia uma matriz 3x4 (3 linhas e 4 colunas). Exibir a matriz informada
# e sua Transposta.

matriz = [[i * 4 + j for j in range(4)] for i in range(3)]

print("Matriz:")
for linha in matriz:
    print(linha)

transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print("\nMatriz Transposta:")
for linha in transposta:
    print(linha)