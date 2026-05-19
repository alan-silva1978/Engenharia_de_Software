# 1. O senhor está ENSINANDO o Python a calcular a munição.
# A função recebe duas "moedas" de entrada: soldados e pentes.
def calcular_municao_total(soldados, pentes_por_soldado):
    
    # 2. Faça a matemática aqui dentro (Escopo Local):
    # Primeiro, descubra o total de pentes (soldados multiplicados pelos pentes_por_soldado)
    total_pentes = soldados * pentes_por_soldado 
    
    # Depois, descubra o total de balas (total_pentes multiplicado por 30)
    total_balas = total_pentes * 30
    
    # 3. Agora, use o comando correto para DEVOLVER (cuspir para fora) o total_balas
    return total_balas


# ==========================================
# O CÓDIGO GLOBAL (O QG usando a sua função)
# ==========================================

# O General envia um esquadrão de 5 soldados, cada um com 4 pentes.
balas_liberadas = calcular_municao_total(5, 4)

print(f"Autorizada a liberação de {balas_liberadas} balas do arsenal.")