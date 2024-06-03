# Solicita ao usuário que informe quantos números deseja inserir
numeros = int(input("Quantos números: "))

# Solicita ao usuário o primeiro número e inicializa variáveis para soma, contagem e maior número
primeiro = int(input("Número 1: "))
count = 1
maior = primeiro
soma = primeiro

# Loop para receber os números restantes e calcular a soma, o maior número e a contagem
while count < numeros:
    count += 1
    # Solicita ao usuário o próximo número
    temp = int(input("Número %d: " % count))
    # Adiciona o número à soma
    soma += temp
    # Verifica se o número atual é maior que o maior número encontrado até agora
    if temp > maior:
        maior = temp
    
# Calcula a média dos números
media = soma / numeros

# Imprime a soma, o maior número, a média e a contagem
print("Soma:", soma)
print("Maior:", maior)
print("Média: %.2f" % media)
print("Contagem:", count)
