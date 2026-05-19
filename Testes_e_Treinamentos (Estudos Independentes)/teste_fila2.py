# 1. MONTANDO A FILA (O primeiro a entrar é o primeiro a sair - FIFO)
fila_do_rancho = ["Soldado Alfa", "Soldado Bravo", "Soldado Charlie", "Recruta Delta", "Recruta Echo"]

print("=======================================")
print("  SISTEMA DE ATENDIMENTO MANUAL DO QG  ")
print("=======================================")
print(f"Iniciando os trabalhos. Temos {len(fila_do_rancho)} homens na fila.")

# 2. O LOOP INFINITO (O turno de trabalho do Sargento)
while True:

    # 3. A PAUSA TÁTICA (O sistema congela e espera a sua ordem)
    comando = input("\n[Aperte ENTER para chamar o próximo] ou digite 'S' para fechar o refeitório: ")

    # Se o senhor digitar S, o break encerra o loop.
    if comando.upper() == 'S':
        print("Finalizando o expediente. Bom descanso, Comandante!")
        break

    # 4. O SENSOR (Verifica se o tamanho da fila chegou a zero)
    esta_vazia = (len(fila_do_rancho)  == 0)

    # 5. A REGRA DO 'NOT' (A Cancela)
    if not esta_vazia:
        # O pop(0) arranca o primeiro da lista e empurra os outros para a frente
        atendido_agora = fila_do_rancho.pop(0)
        print(f">>> PRÓXIMO! Atendendo agora: {atendido_agora}")
        print(f">>> Pessoas restantes aguardando: {len(fila_do_rancho)}")

    else:
        # Se o sensor disser que está vazia, o 'not' bloqueia o pop(0) e cai aqui:
        print(">>> AVISO DO SISTEMA: A fila acabou! Não aperte o botão, não tem ninguém lá!")