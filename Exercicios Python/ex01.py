# 1 – Elaborar um programa que receba o nome de um cliente, seu endereço, valor de uma
# compras e data de entrega. O programa deve exibir o seguinte texto (apresentar na tela a
# mesma formatação):
# AVISO
# Caro cliente Sr(a) ______________________, os produtos da sua compra no
# valor de R$ _____ serão entregues no endereço abaixo:
# Rua _____________________________.
# Data da Entrega: ________________.
# ******************** Obrigado pela Preferência! **********************

nome = input("Digite o nome do cliente: ")
endereco = input("Digite o endereço de entrega: ")
valor_compra = float(input("Digite o valor da compra: "))
data_entrega = input("Digite a data de entrega: ")

mensagem = f"""
AVISO
Caro cliente Sr(a) {nome}, os produtos da sua compra no
valor de R$ {valor_compra:.2f} serão entregues no endereço abaixo:
{endereco}.
Data da Entrega: {data_entrega}.
******************** Obrigado pela Preferência! **********************
"""
print(mensagem)