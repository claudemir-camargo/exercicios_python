# 6 – Crie um programa que receba um número n (inteiro e maior do que 1) como entrada e
# retorne se é um número é primo ou não.

n = int(input("Digite um número inteiro maior que 1: "))

primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
        break

if primo:
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")