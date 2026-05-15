soma = 0
while True:
    numero = int(input("digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero   # operador de atribuição composto

print("A soma dos números digitados é:", soma)