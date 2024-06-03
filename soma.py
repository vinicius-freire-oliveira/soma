# Definição da função somalista que recebe uma lista de números como entrada
def somalista(numeros):
    soma = 0  # Inicializa a variável de soma
    for i in numeros:  # Itera sobre os elementos da lista
        soma = soma + i  # Adiciona cada elemento à variável de soma
    return soma  # Retorna o valor da soma

# Chama a função somalista com uma lista de números e imprime o resultado
print(somalista([1, 3, 5, 7, 9]))
