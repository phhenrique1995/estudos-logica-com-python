# Crie uma função que verifique se uma string é um palíndromo, desconsiderando espaços e diferenças entre maiúsculas e minúsculas.

#Vamos testar se uma palavra é um palíndromo?!

# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# Remove espaços e converte para minúsculas (opcional, para tornar a verificação mais robusta)
palavra_formatada = palavra.replace(" ", "").lower()

# Inverte a palavra
palavra_invertida = palavra_formatada[::-1]

# Verifica se é um palíndromo
if palavra_formatada == palavra_invertida:
    print(f"✅ A palavra '{palavra}' é um palíndromo!")
else:
    print(f"❌ A palavra '{palavra}' não é um palíndromo.")