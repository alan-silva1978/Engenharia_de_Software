# SIMULAÇÃO DE SISTEMA NOVO (Vazio)
# Banco de dados com 10 itens 
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

def categorias_vendidas(lista_vendas):
    if not lista_vendas:
        return set() 
    return {venda["categoria"] for venda in lista_vendas}

def vendas_por_categoria(lista_vendas):
    if not lista_vendas:
        return {} 
    resultado = {}
    for venda in lista_vendas:
        cat = venda["categoria"]
        resultado.setdefault(cat, []).append(venda)
    return resultado

def produto_mais_caro(lista_vendas):
    if not lista_vendas:
        return None
    return max(lista_vendas, key=lambda v: v.get("preco", 0))

def calcular_faturamento_total(lista_vendas):
    if not lista_vendas:
        return 0.0
    total = 0.0
    for venda in lista_vendas:
        total = total + venda.get("preco", 0) 
    return total

def obter_media_vendas(lista_vendas):
    """Calcula média de preços com validação estrita e uso do 'v' em lista comprimida."""
    # O Guarda da Guarita: É vazio? Ou não é uma lista?
    if not lista_vendas or not isinstance(lista_vendas, list):
        raise ValueError("O banco de dados de vendas está corrompido ou não é uma lista.")
    
    # Extrai só os preços usando a técnica espremida do 'v'
    precos = [v.get("preco", 0) for v in lista_vendas if isinstance(v, dict)]
    
    if not precos:
        return 0.0
    
    # Retorna a soma de todos divido pela quantidade
    return sum(precos) / len(precos)

# ==========================================
# RELATÓRIO DO COMANDANTE
# ==========================================

print("\n==============================================")
print(f"Categorias Identificadas: {categorias_vendidas(vendas)}")
print("==============================================")

por_cat = vendas_por_categoria(vendas)
print("\n==============================================")
print(f"Produtos em Componentes: {len(por_cat.get('Componentes', []))}")
print("==============================================")

caro = produto_mais_caro(vendas)
print("\n==============================================")
if caro:
    print(f"Produto mais caro: {caro['produto']} - R$ {caro['preco']:.2f}")
print("==============================================")

print("\n==============================================")
print(f"Faturamento Total: R$ {calcular_faturamento_total(vendas):.2f}")
print("==============================================")

# A CÂMARA DE DETONAÇÃO (TESTANDO A MÉDIA COM TRY/EXCEPT)
print("\n==============================================")
try:
    media = obter_media_vendas(vendas)
    print(f"Média de valor por venda: R$ {media:.2f}")
except ValueError as mensagem_de_erro:
    print(f"ALERTA VERMELHO: {mensagem_de_erro}")
print("==============================================")