# 10 – Criar um programa que solicite um "login" e uma "senha".
# Se o login for igual a "IFSP" e a senha for igual a "PosWEB", exibir a mensagem "Login efetuado
# com sucesso". Se o usuário errar a senha 3 vezes seguidas, informar "Acesso negado".

login_correto = "IFSP"
senha_correta = "PosWEB"

tentativas = 0

while tentativas < 3:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    
    if login == login_correto and senha == senha_correta:
        print("Login efetuado com sucesso.")
        break
    else:
        tentativas += 1
        print("Login ou senha incorretos. Tente novamente.")

if tentativas == 3:
    print("Acesso negado.")
