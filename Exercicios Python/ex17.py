# 17 – Criar um programa que receba 10 valores inteiros e armazene-os em um vetor. Exibir o
# vetor ordenado de maneira crescente e também de maneira decrescente. (Realizar a ordenação
# usando um algoritmo de ordenação – Não utilizar funções prontas se existirem na linguagem
# escolhida)

def ordenacao_por_selecao(vetor):
    for i in range(len(vetor)):
        menor = i
        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[menor]:
                menor = j
        vetor[i], vetor[menor] = vetor[menor], vetor[i]
    return vetor

vetor = []
for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)

vetor_crescente = ordenacao_por_selecao(vetor[:])

vetor_decrescente = vetor_crescente[::-1]

print("Vetor ordenado de maneira crescente:", vetor_crescente)
print("Vetor ordenado de maneira decrescente:", vetor_decrescente)
