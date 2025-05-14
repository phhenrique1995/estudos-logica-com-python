# Crie uma função que determine se um número inteiro é primo.

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Entrada do usuário
entrada = input("Digite um número inteiro: ")

# Validação
if entrada.lstrip("-").isdigit():  # permite número negativo, mas não considera como primo
    numero = int(entrada)
    if eh_primo(numero):
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
else:
    print("Entrada inválida. Por favor, digite um número inteiro válido.")