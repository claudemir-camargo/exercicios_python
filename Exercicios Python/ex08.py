# 8 – Pesquisar o algoritmo de validação de CPF e implemente-o.

def valida_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    soma = sum(int(a) * b for a, b in zip(cpf[:-2], range(10, 1, -1)))
    d1 = (soma * 10 % 11) % 10
    if d1 != int(cpf[-2]):
        return False
    
    soma = sum(int(a) * b for a, b in zip(cpf[:-1], range(11, 1, -1)))
    d2 = (soma * 10 % 11) % 10
    if d2 != int(cpf[-1]):
        return False

    return True

cpf = input("Digite o CPF: ")
if valida_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
