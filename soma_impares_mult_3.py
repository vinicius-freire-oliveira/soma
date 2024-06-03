# Inicializa a variável de soma
s = 0

# Itera sobre os números ímpares de 1 a 499 (inclusive)
for a in range(1, 500, 2):
    # Verifica se o número é divisível por 3
    if a % 3 == 0:
        # Se for divisível por 3, adiciona-o à soma
        s += a

# Imprime o resultado da soma
print('Soma:', s)
