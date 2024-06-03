# Inicializa a variável soma_numeros como 0 para armazenar a soma dos números
soma_numeros = 0

# Solicita ao usuário que insira um número
numero = int(input("Por favor, insira um número: "))

# Itera de 1 até o número inserido pelo usuário, incluindo o próprio número
for i in range(1, numero + 1, 1):
    # Adiciona o valor de i à variável soma_numeros
    soma_numeros += i

# Imprime a soma dos números
print("A soma é = ", soma_numeros)
