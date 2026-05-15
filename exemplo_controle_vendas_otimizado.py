# SIMULAÇÃO DE SISTEMA NOVO (Vazio)
# Para testar o erro, o senhor pode deixar assim: vendas = []
vendas = [{"id": 1, "produto": "Cadeira Gamer", "preco": 1200.00, "categoria": "Móveis"},
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
        return {} # Retorna dicionário vazio se não houver carga
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
    """Soma o preço de todas as vendas registradas."""
    # 1. Blindagem de segurança: Verifica se a lista está vazia
    if not lista_vendas:
        return 0.0  # Retorna faturamento zero se não houver vendas
    
    # 2. A Caixa Registradora (Começa Zerada)
    total_acumulado = 0.0

    # 3. O processo de soma
    for vendas in lista_vendas:
        #pega o preçoda venda atual (se não tiver preço, assume 0)
        valor_da_ficha = vendas.get("preco", 0)

        # Pega o que já tinha no caixa e soma com o valor novo
        total_acumulado = total_acumulado + valor_da_ficha

    # 4. Entrega o malote de dinheiro para o Comandante
    return total_acumulado

# ==========================================
# RELATÓRIO DINÂMICO (Trata o "Nada" com elegância)
# ==========================================

print("\n==============================================")
cats = categorias_vendidas(vendas)
if cats:
    print(f"Categorias Identificadas: {cats}")
else:
    print("Categorias: [NENHUM DADO DISPONÍVEL]")
print("==============================================")

print("\n==============================================")
por_cat = vendas_por_categoria(vendas)
# Proteção: .get('Eletrônicos', []) evita erro se a categoria não existir
eletronicos = por_cat.get('Eletrônicos', [])
print(f"Produtos em Eletrônicos: {len(eletronicos)}")
print("==============================================")

print("\n==============================================")
caro = produto_mais_caro(vendas)
if caro:
    print(f"Produto mais caro: {caro['produto']} - R${caro['preco']:.2f}")
else:
    print("Produto mais caro: [ESTOQUE VAZIO]")
print("==============================================")

print("\n==============================================")
faturamento = calcular_faturamento_total(vendas)
print(f"Faturamento Total: R$ {faturamento:.2f}")
print("==============================================")