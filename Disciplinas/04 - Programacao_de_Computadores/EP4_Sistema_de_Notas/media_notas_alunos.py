# Inicialização do banco de dados principal (Lista de Dicionários)
# Cada dicionário representa um estudante com 'nome' (str) e 'notas' (list of float)
banco_de_estudantes = [
    {"nome": "Alan Carlos", "notas": [8.5, 9.0, 7.5]},
    {"nome": "Maria Silva", "notas": [6.0, 5.5, 7.0]},
    {"nome": "João Mendes", "notas": [9.5, 10.0, 9.8]}
]

def calcular_media(notas):
    """
    Calcula a média aritmética simples a partir de um histórico de notas.
    
    Esta rotina processa os valores numéricos fornecidos e possui uma 
    validação de segurança (Edge Case) que intercepta listas vazias, 
    retornando um valor padrão para evitar falhas críticas no sistema 
    (ZeroDivisionError).
    
    Args:
        notas (list): Uma lista contendo valores numéricos do tipo float 
                      ou int, referentes ao histórico do estudante.
                      
    Returns:
        float: O valor resultante da média aritmética. Caso a lista de 
               entrada esteja vazia, a função retorna 0.0 com segurança.
    """
    if not notas:
        return 0.0
    
    soma_total = sum(notas)
    quantidade = len(notas)
    
    return soma_total / quantidade


def verificar_aprovacao(media, media_minima=7.0):
    """
    Avalia o status de aprovação institucional do estudante.
    
    A função atua como o módulo de decisão final. Ela compara a média 
    consolidada do aluno com a nota de corte vigente. O uso de um parâmetro 
    padrão (Default Parameter) garante flexibilidade para que a mesma rotina 
    seja reaproveitada em turmas com réguas de avaliação diferentes, sem a 
    necessidade de reescrever o código ou gerar redundância.
    
    Args:
        media (float): A média final consolidada obtida pelo estudante.
        media_minima (float, opcional): O limite mínimo exigido para 
                                        aprovação. O padrão assumido é 7.0.
                                        
    Returns:
        str: Retorna exatamente a string 'Aprovado' caso o estudante 
             atinja ou supere a nota de corte; caso contrário, 
             retorna a string 'Reprovado'.
    """
    if media >= media_minima:
        return "Aprovado"
    else:
        return "Reprovado"
    
def gerar_relatorio(alunos):
    """
    Itera sobre o banco de estudantes, processa os cálculos e exibe um relatório formatado.
    
    Args:
        alunos (list): Lista de dicionários contendo 'nome' (str) e 'notas' (list).
        
    Returns:
        None: Esta função não retorna valor. Exibe o relatório diretamente no terminal.
    """
    # Cabeçalho do Relatório formatado para clareza visual
    print("-" * 55)
    print("RELATÓRIO CONSOLIDADO DE DESEMPENHO".center(55))
    print("-" * 55)
    
    # Laço de repetição: Iterando sobre a estrutura de dados
    for aluno in alunos:
        # 1. Extração de Dados com defesa suave (.get)
        nome_aluno = aluno.get("nome", "Desconhecido")
        notas_aluno = aluno.get("notas", [])
        
        # 2. Invocação das funções lógicas (Delegação de tarefas)
        media_final = calcular_media(notas_aluno)
        status = verificar_aprovacao(media_final)
        
        # 3. Impressão formatada utilizando f-strings
        # O marcador :<15 alinha o nome à esquerda em 15 espaços
        # O marcador :.2f fixa a média em duas casas decimais
        print(f"Aluno(a): {nome_aluno:<15} | Média: {media_final:>5.2f} | Situação: {status}")
    
    # Rodapé de encerramento
    print("-" * 55)

# Ponto de entrada para execução direta do script
if __name__ == "__main__":
    gerar_relatorio(banco_de_estudantes)