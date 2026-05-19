# ==========================================
# BANCO DE DADOS DE VENDAS
# ==========================================
vendas = [
    {"id": 1, "produto": "Cadeira Gamer", "preco": 1200.00, "categoria": "Móveis"},
    {"id": 2, "produto": "Headset Bluetooth", "preco": 350.00, "categoria": "Acessórios"},
    {"id": 3, "produto": "Smartphone", "preco": 4500.00, "categoria": "Eletrônicos"},
    {"id": 4, "produto": "Mousepad Gigante", "preco": 80.00, "categoria": "Acessórios"},
    {"id": 5, "produto": "Placa de Vídeo", "preco": 2800.00, "categoria": "Componentes"},
    {"id": 6, "produto": "Mesa de Escritório", "preco": 650.00, "categoria": "Móveis"},
    {"id": 7, "produto": "Impressora", "preco": 900.00, "categoria": "Eletrônicos"},
    {"id": 8, "produto": "Pendrive 64GB", "preco": 45.00, "categoria": "Acessórios"},
    {"id": 9, "produto": "Processador", "preco": 1500.00, "categoria": "Componentes"},
    {"id": 10, "produto": "Cabo HDMI", "preco": 30.00, "categoria": "Acessórios"}
]

# ==========================================
# SARGENTOS ESPECIALISTAS (FUNÇÕES DESDOBRADAS)
# ==========================================

def categorias_vendidas(lista_vendas):
    """
    Missão: Descobrir quais são os setores (categorias) da nossa loja, sem repetições.
    
    Args:
        lista_vendas (list): O malote de fichas (dicionários) com todas as vendas.
        
    Returns:
        set: Uma coleção (conjunto) contendo os nomes das categorias, sem dados repetidos.
             Se o malote estiver vazio, retorna um conjunto vazio: set().
    """
    # 1. Checa se o malote tem documentos
    if not lista_vendas:
        return set() 
    
    # 2. Cria a gaveta vazia de categorias únicas (O Conjunto)
    categorias_unicas = set()
    
    # 3. Pega ficha por ficha na mão
    for ficha_de_venda in lista_vendas:
        # Lê a etiqueta 'categoria' da ficha atual
        categoria_atual = ficha_de_venda["categoria"]
        
        # Adiciona na gaveta. Se já existir lá dentro, o Conjunto ignora a repetição.
        categorias_unicas.add(categoria_atual)
        
    # 4. Entrega a gaveta pronta para o Comandante
    return categorias_unicas


def vendas_por_categoria(lista_vendas):
    """
    Missão: Organizar todas as fichas de vendas separando-as em pastas pelo nome da categoria.
    
    Args:
        lista_vendas (list): O malote de fichas com as vendas.
        
    Returns:
        dict: Um grande arquivo (dicionário) onde a chave é o nome do setor (ex: 'Móveis') 
              e o valor é uma lista com as fichas daquele setor.
    """
    if not lista_vendas:
        return {} 
    
    # 1. Cria o Arquivo Geral vazio (Dicionário)
    arquivo_organizado = {}
    
    # 2. Lê ficha por ficha
    for ficha_de_venda in lista_vendas:
        categoria_atual = ficha_de_venda["categoria"]
        
        # 3. A Lógica do "Se a pasta não existe":
        # Pergunta: O nome dessa categoria já virou uma pasta no meu Arquivo Geral?
        if categoria_atual not in arquivo_organizado:
            # Se não virou, eu crio uma pasta vazia (Lista vazia) com o nome dessa categoria
            arquivo_organizado[categoria_atual] = []
            
        # 4. Agora que tenho certeza que a pasta existe, guardo a ficha lá dentro
        arquivo_organizado[categoria_atual].append(ficha_de_venda)
        
    return arquivo_organizado


def produto_mais_caro(lista_vendas):
    """
    Missão: Procurar e identificar a ficha de venda com o maior preço registrado.
    
    Args:
        lista_vendas (list): O malote de fichas com as vendas.
        
    Returns:
        dict: Devolve apenas UMA ficha (a ficha inteira do produto campeão).
              Se o malote estiver vazio, retorna None (Nada).
    """
    if not lista_vendas:
        return None
    
    # 1. Preparativos antes da busca:
    # Eu ainda não sei quem é o mais caro, então deixo em branco (None)
    ficha_campea = None
    # Guardo um preço impossível de baixo para que o primeiro produto já ganhe dele
    maior_preco_ate_agora = -1.0 
    
    # 2. Começa a caçada ficha por ficha
    for ficha_de_venda in lista_vendas:
        # Lê o preço. Se o recruta esqueceu de anotar o preço na ficha, assumo que custa 0
        preco_atual = ficha_de_venda.get("preco", 0.0)
        
        # 3. A Batalha:
        # Se o preço da ficha que estou segurando é maior que o preço anotado no quadro...
        if preco_atual > maior_preco_ate_agora:
            # Atualizo o quadro com o novo recorde
            maior_preco_ate_agora = preco_atual
            # Coroo a ficha atual como a nova campeã
            ficha_campea = ficha_de_venda
            
    # 4. No fim da leitura de todas as fichas, devolve o campeão que sobreviveu
    return ficha_campea


def calcular_faturamento_total(lista_vendas):
    """
    Missão: Somar o valor financeiro de todas as vendas (O Sargento Contador).
    """
    if not lista_vendas:
        return 0.0
    
    # A caixa registradora começa zerada
    total_acumulado = 0.0
    
    for ficha_de_venda in lista_vendas:
        preco_da_ficha = ficha_de_venda.get("preco", 0.0)
        total_acumulado = total_acumulado + preco_da_ficha
        
    return total_acumulado


def obter_media_vendas(lista_vendas):
    """
    Missão: Calcular o valor médio de uma venda na loja, utilizando a blindagem máxima.
    
    Args:
        lista_vendas (list): O malote de dados (deve ser obrigatoriamente do tipo Lista).
        
    Returns:
        float: O número que representa a média de preço.
        
    Raises:
        ValueError: Dispara o Alarme Vermelho se o dado enviado não for uma lista.
    """
    # 1. O Guarda da Guarita (Blindagem)
    if not lista_vendas or not isinstance(lista_vendas, list):
        raise ValueError("O banco de dados de vendas está corrompido ou não é uma lista.")
    
    # 2. Cria uma gaveta só para guardar os números dos preços (separando da ficha)
    gaveta_de_precos = []
    
    # 3. Lê ficha por ficha para extrair só o número (O Jeito Longo de fazer o "v")
    for ficha in lista_vendas:
        # Confirma se a ficha é mesmo um dicionário (evita erro se tiver lixo no meio)
        if isinstance(ficha, dict):
            preco_da_ficha = ficha.get("preco", 0.0)
            gaveta_de_precos.append(preco_da_ficha)
            
    # 4. Se só tinha lixo na lista e não extraiu nenhum preço, retorna 0
    if not gaveta_de_precos:
        return 0.0
    
    # 5. A Matemática
    soma_dos_precos = sum(gaveta_de_precos)          # Soma todo mundo
    quantidade_de_vendas = len(gaveta_de_precos)     # Conta quantos itens tem
    
    media_final = soma_dos_precos / quantidade_de_vendas
    return media_final


# ==========================================
# ÁREA DE EXECUÇÃO E RELATÓRIOS DO COMANDANTE
# ==========================================

print("\n==============================================")
print("1. RELATÓRIO DE SETORES (Conjuntos):")
# Chama o sargento enviando o malote global 'vendas'
setores = categorias_vendidas(vendas)
print(f"Categorias Identificadas: {setores}")

print("\n==============================================")
print("2. RELATÓRIO DE ESTOQUE (Dicionários e Listas):")
arquivo_por_categoria = vendas_por_categoria(vendas)
# Usando o .get para acessar a pasta 'Componentes'. Se não existir, devolve lista vazia []
quantidade_componentes = len(arquivo_por_categoria.get('Componentes', []))
print(f"Quantidade de produtos no setor 'Componentes': {quantidade_componentes}")

print("\n==============================================")
print("3. RELATÓRIO DO PRODUTO MAIS CARO:")
produto_campeao = produto_mais_caro(vendas)
if produto_campeao:
    print(f"O item mais caro é: {produto_campeao['produto']} custando R$ {produto_campeao['preco']:.2f}")

print("\n==============================================")
print("4. RELATÓRIO FINANCEIRO TOTAL:")
faturamento = calcular_faturamento_total(vendas)
print(f"Faturamento Total da Loja: R$ {faturamento:.2f}")

print("\n==============================================")
print("5. RELATÓRIO ESTATÍSTICO BLINDADO (Try/Except):")
try:
    media = obter_media_vendas(vendas)
    print(f"O Ticket Médio (Média) por venda é: R$ {media:.2f}")
except ValueError as mensagem_de_erro:
    print(f"ALERTA VERMELHO DESARMADO: {mensagem_de_erro}")
print("==============================================")