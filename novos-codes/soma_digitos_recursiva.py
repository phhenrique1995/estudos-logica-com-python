# Implemente uma função recursiva que calcule a soma dos dígitos de um número inteiro positivo.

def soma_digitos(n):
    # Caso base: se n for menor que 10, retorna ele mesmo
    if n < 10:
        return n
    else:
        return n % 10 + soma_digitos(n // 10)

# Entrada de dados do usuário
entrada = input("Digite um número inteiro positivo: ")

# Validação
if entrada.isdigit():
    numero = int(entrada)
    resultado = soma_digitos(numero)
    print(f"A soma dos dígitos de {numero} é: {resultado}")
else:
    print("Entrada inválida. Por favor, digite apenas números inteiros positivos.")
