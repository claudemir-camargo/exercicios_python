# 3 – Crie um programa que leia dois números reais e apresente um menu com as opções:
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# Caso a linguagem escolhida tenha suporte, exibir o resultado em uma tela gráfica.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha uma opção:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    resultado = num1 + num2
elif opcao == 2:
    resultado = num1 - num2
elif opcao == 3:
    resultado = num1 * num2
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Opção inválida"

print("Resultado: ", resultado)
