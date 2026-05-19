# 1. A Cautela do Equipamento (Sempre na primeira linha)
import datetime

print("--- SISGEF: Registro de Operações ---")

# 2. O aplicativo pede qual é a situação
evento = input("Informe a situação (Ex: Assunção de serviço, Abordagem, Fim de Turno): ")

# 3. O Relógio Atômico: O sistema puxa a hora exata da máquina invisivelmente
hora_exata = datetime.datetime.now()

# 4. O Relatório Final usando a Luneta de Precisão (F-String)
print(f"\n[REGISTRO OFICIAL] Comando, a situação '{evento}' foi cravada no sistema em: {hora_exata}")