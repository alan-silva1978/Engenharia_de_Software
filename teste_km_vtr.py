while True:
    try:
        # TENTATIVA: O sistema tenta pegar a entrada e transformar em número inteiro
        km_inicial = int(input("Informe o Odômetro atual da viatura (apenas números): "))
        
        # Se passar daqui, a missão foi um sucesso e quebramos o laço
        print("KM", km_inicial, "registrada com sucesso. Assunção concluída.")
        break
        
    except ValueError:
        # DEFESA: Se o policial digitou "150ABC", o sistema cai aqui e não trava!
        print(">>> ATENÇÃO, COMANDO! Entrada inválida. Digite apenas números no Odômetro.")