import random
print("=" * 40)
print("GERADOR DE NÚMEROS DA SORTE")
print("=" * 40)
nome = input("\nQual é o seu nome? ")
mes = int(input("Em qual mês você nasceu? (1-12) "))
dia = int(input("Em qual dia você nasceu? (1-31) "))
# Gera 6 números aleatórios entre 1 e 60
numeros_sorte = sorted(random.sample(range(1, 61), 6))
# Calcula um número especial baseado na data
numero_especial = (mes + dia) % 10
print("\n" + "-" * 40)
print(f"Olá, {nome}!")
print(f"Seus números da sorte são: {numeros_sorte}")
print(f"Seu número especial é: {numero_especial}")
print("-" * 40)