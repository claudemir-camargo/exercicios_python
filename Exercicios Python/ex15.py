# 15 – Exibir uma matriz com os números de 1 a 100, adicionando uma marca (ex: asterisco) em 
# todos os números primos. (Crivo de Eratóstenes).

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

matriz = [[i * 10 + j + 1 for j in range(10)] for i in range(10)]

for i in range(10):
    for j in range(10):
        if eh_primo(matriz[i][j]):
            print(f"{matriz[i][j]}*", end=" ")
        else:
            print(matriz[i][j], end=" ")
    print()
