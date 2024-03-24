# 11 – Criar um programa que leia um vetor de números inteiros com 10 posições.
# Exibir quantos números pares e quantos números ímpares foram informados. Exibir também a
# soma dos números pares e a média dos números ímpares

numeros_pares = 0
soma_pares = 0
numeros_impares = 0
soma_impares = 0

for i in range(10):
    numero = int(input(f"Digite o número da posição {i+1}: "))
    
    if numero % 2 == 0:
        numeros_pares += 1
        soma_pares += numero
    else:
        numeros_impares += 1
        soma_impares += numero

media_impares = soma_impares / numeros_impares if numeros_impares > 0 else 0

print(f"Números pares: {numeros_pares}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Números ímpares: {numeros_impares}")
print(f"Média dos números ímpares: {media_impares:.2f}")