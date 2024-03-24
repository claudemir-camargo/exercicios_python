# 7 – Desenvolver um algoritmo que simule um jogo de adivinhação: O jogador insere números na
# tentativa de acertar o número sorteado entre 0 e 9 pelo algoritmo. Quando acertar, o programa
# deve informar que ele acertou o número x (sorteado) em x tentativas (quantidade de tentativas
# do jogador). Verificar como é realizada a geração de números aleatórios na linguagem
# escolhida.

import random
numero_sorteado = random.randint(0, 9)

tentativas = 0

while True:
    numero = int(input("Digite um número entre 0 e 9: "))
    
    tentativas += 1
    
    if numero == numero_sorteado:
        print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativas} tentativas.")
        break
    else:
        print("Número incorreto. Tente novamente.")
