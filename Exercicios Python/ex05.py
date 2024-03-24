# 5 – Crie um programa que receba dois números inteiros e diferentes, maiores do que 0. Exiba as
# tabuadas de todos os números do intervalo (Ex. Números digitados: 3 e 7 → exibirá as tabuadas
# # do 3, 4, 5, 6 e 7). O resultado deve ser exibido no terminal.

num1 = int(input("Digite o primeiro número (maior que 0): "))
num2 = int(input("Digite o segundo número (maior que 0 e diferente do primeiro): "))

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1, num2 + 1):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")