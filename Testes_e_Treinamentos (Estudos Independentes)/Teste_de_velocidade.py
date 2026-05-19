while True:
    velocidade = int(input("informe a velocidade do veículo mensurada em km/h: "))
    print(f"\nA velocidade do veículo aferida é {velocidade} km/h!")

    if velocidade == 0:
        print("Fim do expediente. Radar desligado.")
        break

    if velocidade > 80:
        print("Infração Gravíssima - Veículo Apreendido!")

    elif velocidade > 60:
        print("Infração Leve - Notificação Emitida.")

    elif velocidade > 0:
        print("Velocidade Permitida - Passe Livre.")

    else:
        print("Erro no sensor. Velocidade inválida.")