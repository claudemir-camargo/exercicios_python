# 2 – Crie um programa para o cálculo do IMC de uma pessoa. Exibir mensagens de acordo com
# a faixa de valores encontrada:
# Menor que 16,5 = Desnutrição
# de 16,6 a 18,5 = Abaixo do peso
# de 18,6 a 24,9 = Peso normal
# de 25 a 29,9 = Sobrepeso
# maior ou igual a 30 = Obesidade.

peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 16.5:
    categoria = "Desnutrição"
elif imc < 18.5:
    categoria = "Abaixo do peso"
elif imc < 24.9:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

print(f"Seu IMC é {imc:.2f} e sua categoria é '{categoria}'.")
