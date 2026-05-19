# 1. ENTRADA: Perguntar a pontuação do recruta (lembrar de converter para int)
nota = int(input("Digite a nota obtida após realizar o teste de tiro no estande: "))

# 2. PROCESSAMENTO E SAÍDA: Iniciar o posto de controle
# (Dica: O print vai ficar "dentro" / indentado em cada opção)
print(f"A nota informada foi {nota}.")

# Se nota maior ou igual a 90...
if nota >= 90:
    print("Atirador de elite.")

# Senão, se nota maior ou igual a 70...
elif nota >= 70:
    print("Atirador Padrão.")

# Senão, se nota maior ou igual a 50...
elif nota >= 50:
    print("Em treinamento.")

# Caso contrário (o que sobrou)...
else:
    print("Reprovado -  Voltar à Academia.")