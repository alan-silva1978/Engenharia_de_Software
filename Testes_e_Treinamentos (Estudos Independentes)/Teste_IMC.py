nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(nome + ",seu IMC é:", imc)
if imc <18.5:
    print("Você está abaixo do peso.")
elif imc <25:
    print("Você está com peso normal.")
else:
    print("Você está acima do peso.")