# Implemente um gerador que produza os primeiros n números da sequência de Fibonacci.

# Fibonacci Fácil

# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série
# de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual
# à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46)
# e mostre os N primeiros números dessa série.

# •	Entrada

# O arquivo de entrada contém um valor inteiro N (0 < N < 46).

# •	Saída

# Os valores devem ser mostrados na mesma linha, separados por um espaço em
# branco. Não deve haver espaço após o último valor.

# Solicita o valor de N com mensagem clara
n = int(input("Digite um número inteiro entre 1 e 45: "))

# Validação de entrada
if n <= 0 or n >= 46:
    print("Entrada inválida. O número deve estar entre 1 e 45.")
else:
    fib1 = 0
    fib2 = 1
    fib_list = [fib1]

    for i in range(1, n):
        fib_list.append(fib2)
        fib1, fib2 = fib2, fib1 + fib2

    # Geração da saída formatada
    fib_string = ' '.join(str(x) for x in fib_list)
    print(fib_string)