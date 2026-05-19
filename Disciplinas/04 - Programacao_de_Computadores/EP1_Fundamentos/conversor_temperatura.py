# Script: conversor_temperatura.py
# Objetivo: Converter temperatura de graus Celsius para Fahrenheit

# Captura a entrada do usuário (que nativamente é uma string) e realiza 
# o casting (conversão explícita) imediato para o tipo float, 
# garantindo que o dado seja numérico para as operações matemáticas subsequentes.
temperatura_celsius = float(input("Informe a temperatura em graus Celsius: ")) # casting: string para float

# Aplica a regra matemática de conversão respeitando a precedência dos operadores
# e armazena o resultado em uma nova variável padronizada em snake_case.
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Exibe o relatório final formatado (f-string) limitando a duas casas decimais (:.2f)
print(f"A temperatura convertida é {temperatura_fahrenheit:.2f} graus Fahrenheit.")