# Script: calculo_fatorial.py
# Objetivo: Calcular o fatorial de um número inteiro fornecido pelo usuário.

import math

# Captura a entrada do usuário (nativamente texto) e realiza o casting (conversão 
# explícita) imediato para o tipo int. Isso garante que a função matemática 
# receba um número inteiro válido, rejeitando casas decimais ou caracteres soltos.
numero_fatorial = int(input("Digite um número inteiro entre 1 e 10: ")) # casting: string para int

# Processamento: invoca a função da biblioteca math para calcular o fatorial
# e armazena o resultado em uma variável autodescritiva em snake_case.
resultado_fatorial = math.factorial(numero_fatorial)

# Saída: exibe o número original e o seu fatorial formatados dinamicamente na mesma frase.
print(f"O fatorial do número {numero_fatorial} é {resultado_fatorial}.")