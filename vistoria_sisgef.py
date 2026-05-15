# A nossa "gaveta cofre"que vai guardar a quantidade de danos
total_avarias = 0

print("--- SISGEF: Vistoria Tática de Lataria ---")

# O Laço de Patrulha: vai rodar até o policial encerrar
while True:
    # Capturamos o texto do policial (sem usar int(), pois avaria é texto)
    avaria = input ("Descreva a nova avaria (ou digite 0 para encerrar): ")

    # Condição de Aborto da Missão
    if avaria == "0":
        break

    # O Acúmulo: Em vez de somar um valor, nós CONTAMOS +1 para cada registro
    total_avarias += 1
    print(">>> Avaria registrada com sucesso no sistema!")

# O relatório Final (Fora da Indentação do Laço)
print("Vistoria finalizada, Comando. Total de avarias novas registradas:", total_avarias)