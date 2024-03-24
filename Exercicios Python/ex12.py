# 12 – Criar um programa que preencha um Vetor de 1000 posições com números aleatórios.
# Exibir a porcentagem de números maiores ou iguais a 700 existentes no vetor.

import random

vetor = []
contador = 0

for i in range(1000):
    numero = random.randint(0, 1000)
    vetor.append(numero)
    print(vetor[i])
   
    if numero >= 700:
        contador += 1

porcentagem = (contador / 1000) * 100

print(f"A porcentagem de números maiores ou iguais a 700 é {porcentagem:.2f}%.")