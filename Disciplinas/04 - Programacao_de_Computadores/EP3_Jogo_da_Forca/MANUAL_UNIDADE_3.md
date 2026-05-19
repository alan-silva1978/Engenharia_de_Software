# 🪖 MANUAL DE SOBREVIVÊNCIA: ENGENHARIA DE SOFTWARE (UNIDADE III)
**Objetivo:** Guia de consulta rápida para sintaxe, arquitetura e boas práticas em Python.

---

## 1. O QUARTEL GENERAL (Funções e Escopo)
Evite códigos monolíticos. Divida as missões em Sargentos Especialistas.

* **`def nome_da_funcao(parametros):`** -> O comando de recrutamento. Cria um especialista.
* **Parâmetros (A Bandeja):** O que a função precisa receber para trabalhar.
* **`return` (A Entrega):** Funções profissionais NÃO usam `print`. Elas devolvem o resultado com `return` para que o Comandante decida o que fazer com ele.
* **Regra do Escopo:** O que acontece em Vegas (dentro do `def`), fica em Vegas. Variáveis criadas dentro de uma função morrem quando ela termina. Variáveis fora das funções são Globais e perigosas de serem alteradas.

---

## 2. ARSENAL DE DADOS (Como guardar as munições)
A decisão mais importante da arquitetura de um software.

| Estrutura | Símbolo | Característica Principal | Quando Usar na Prática? |
| :--- | :---: | :--- | :--- |
| **Lista** | `[ ]` | Mutável, Ordenada (0, 1, 2...) | Fila de dados gerais (ex: notas de alunos, histórico). |
| **Tupla** | `( )` | **Imutável** (Cofre forte) | Dados blindados contra alteração (ex: coordenadas, configs). |
| **Dicionário** | `{ }` | Chave e Valor (Rótulos) | Dados com nomes/atributos (ex: ficha de cliente, carrinho de compras). |
| **Conjunto** | `set()` | Únicos e Desordenados | Filtragem rápida, cruzamento de dados, remoção de duplicatas. |

---

## 3. FORMAÇÕES DE COMBATE (Lógica de Fluxo)
Padrões universais para retirar dados de coleções.

* **PILHA (LIFO - Last In, First Out):**
  * *Lógica:* O último prato colocado no topo é o primeiro a ser lavado.
  * *Uso Prático:* O botão de **"Desfazer" (Undo)**. Analisador de histórico de navegação (botão voltar).
  * *Comandos Python:* `.append()` para colocar no topo, `.pop()` (vazio) para tirar do topo.

* **FILA (FIFO - First In, First Out):**
  * *Lógica:* Fila de banco. Quem chega primeiro é processado primeiro.
  * *Uso Prático:* Servidores web, fila de impressora, gerenciamento de tarefas.
  * *Comandos Python:* `.append()` para colocar no fim. Evite `.pop(0)` em listas grandes (muito lento), use o módulo `deque` do `collections` para alta performance.

---

## 4. O ESQUADRÃO ANTIBOMBAS (Blindagem de Código)
Softwares amadores travam e fecham. Softwares profissionais absorvem o impacto.

### **A. Verificação de Identidade (A Guarita)**
```python
if not isinstance(carga, list):
    raise ValueError("A carga interceptada não é uma lista válida!")
```
*Garante que o dado que entrou é do tipo correto antes de processá-lo.*

### **B. Leitura Segura de Dicionários (O Cauteloso)**
```python
# MODO PERIGOSO (Se o preço não existir, o sistema explode):
valor = ficha["preco"] 

# MODO BLINDADO (Se o preço não existir, ele assume R$ 0.0 e a vida segue):
valor = ficha.get("preco", 0.0)
```

### **C. A Câmara de Detonação (Try / Except)**
```python
try:
    # TENTE executar essa missão perigosa
    media = calcular_media(vendas)
except ValueError as erro:
    # SE EXPLODIR, não desligue o servidor. Apenas capture a bomba e avise.
    print(f"Ocorreu um erro, mas o sistema continua operante: {erro}")
```

---

## 5. DIÁRIO DE BORDO (Protocolo Git/GitHub)
A logística de salvamento tático do código fonte.

1. **Changes (O Pátio):** Arquivos alterados recentemente, mas ainda não agendados para o voo.
2. **Sinal de `+` (Staged / O Avião):** Seleciona arquivos específicos para o próximo pacote de salvamento.
3. **Commit (O Lacre):** Registra a foto do momento com uma mensagem técnica militar:
   * `feat:` (Nova ferramenta/função)
   * `refactor:` (Melhoria de código existente)
   * `docs:` (Anotações e documentação)
4. **Sync / Push (A Decolagem):** Envia os commits confirmados para a base externa (GitHub).