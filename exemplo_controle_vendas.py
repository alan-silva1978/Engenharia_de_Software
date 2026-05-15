# Estrutura de dados para representar vendas
vendas = [
 {"id": 1, "produto": "Notebook", "preco": 3500.00, "categoria": 
"Eletrônicos"},
 {"id": 2, "produto": "Mouse", "preco": 50.00, "categoria": "Acessórios"},
 {"id": 3, "produto": "Teclado", "preco": 150.00, "categoria": "Acessórios"},
 {"id": 4, "produto": "Monitor", "preco": 800.00, "categoria": 
"Eletrônicos"},
 {"id": 5, "produto": "Webcam", "preco": 200.00, "categoria": "Acessórios"}
]

def categorias_vendidas(lista_vendas):
 """Retorna conjunto de categorias únicas."""
 return {venda["categoria"] for venda in lista_vendas}

def vendas_por_categoria(lista_vendas):
 """Agrupa vendas por categoria."""
 resultado = {}
 for venda in lista_vendas:
     cat = venda["categoria"]
     if cat not in resultado:
         resultado[cat] = []
     resultado[cat].append(venda)
 return resultado

def produto_mais_caro(lista_vendas):
 """Encontra o produto com maior preço."""
 if not lista_vendas:
       return None
 return max(lista_vendas, key=lambda v: v["preco"])

# Usando as funções
categorias = categorias_vendidas(vendas)
print(f"\nCategorias: {categorias}")  # {'Eletrônicos', 'Acessórios'}

por_categoria = vendas_por_categoria(vendas)
print(f"\nProdutos em Eletrônicos: {len(por_categoria['Eletrônicos'])}")

caro = produto_mais_caro(vendas)
print(f"\nProduto mais caro: {caro['produto']} - R${caro['preco']:.2f}")