# 16 – Ler uma matriz 3x3 e exibir o valor do seu Determinante. Criar o algoritmo de acordo com a
# regra de Sarrus.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

determinante = (matriz[0][0]*matriz[1][1]*matriz[2][2] + matriz[0][1]*matriz[1][2]*matriz[2][0] + matriz[0][2]*matriz[1][0]*matriz[2][1]) - (matriz[0][2]*matriz[1][1]*matriz[2][0] + matriz[0][1]*matriz[1][0]*matriz[2][2] + matriz[0][0]*matriz[1][2]*matriz[2][1])

print(f"O determinante da matriz é {determinante}.")