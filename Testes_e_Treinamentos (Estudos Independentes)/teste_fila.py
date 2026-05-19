# ==========================================
# 1. A FÁBRICA DE FILAS (A Estrutura Básica)
# ==========================================
class Fila:
    def __init__(self):
        self.elementos = []
        
    def enqueue(self, item):
        self.elementos.append(item) # Entra no final
        
    def dequeue(self):
        if not self.esta_vazia():
            return self.elementos.pop(0) # Sai do começo
        return None
        
    def esta_vazia(self):
        return len(self.elementos) == 0


# ==========================================
# 2. O SISTEMA DO BANCO (Com Revezamento)
# ==========================================
class GerenciadorComRevezamento:
    def __init__(self):
        self.fila_prioritaria = Fila()
        self.fila_normal = Fila()
        self.contador_prioridade = 0  # O "caderninho" do Sargento

    def adicionar_cliente(self, nome, tipo):
        if tipo == "prioridade":
            self.fila_prioritaria.enqueue(nome)
        else:
            self.fila_normal.enqueue(nome)

    def proximo_da_vez(self):
        # REGRA MESTRA: Já chamou 2 prioritários? Tem gente na fila normal?
        if self.contador_prioridade >= 2 and not self.fila_normal.esta_vazia():
            self.contador_prioridade = 0 # Zera o caderninho
            return self.fila_normal.dequeue() + " (Chamado por REVEZAMENTO)"

        # Tenta atender a fila prioritária primeiro
        if not self.fila_prioritaria.esta_vazia():
            self.contador_prioridade += 1 # Anota +1 no caderninho
            return self.fila_prioritaria.dequeue() + " (Chamado por PRIORIDADE)"
        
        # Se não tem prioritário, atende a fila normal normalmente
        if not self.fila_normal.esta_vazia():
            self.contador_prioridade = 0
            return self.fila_normal.dequeue() + " (Chamado da fila Normal)"

        return None


# ==========================================
# 3. CAMPO DE TESTES (A Simulação)
# ==========================================

banco = GerenciadorComRevezamento()

# O Sargento Triador recebe os clientes e coloca nas filas:
banco.adicionar_cliente("Senhor Alberto (Idoso)", "prioridade")
banco.adicionar_cliente("Senhora Maria (Idosa)", "prioridade")
banco.adicionar_cliente("Senhor Carlos (Idoso)", "prioridade")
banco.adicionar_cliente("Senhora Joana (Idosa)", "prioridade")

banco.adicionar_cliente("Jovem Pedro", "normal")
banco.adicionar_cliente("Jovem Lucas", "normal")
banco.adicionar_cliente("Jovem Ana", "normal")

print("--- INICIANDO ATENDIMENTO NO GUICHÊ ---\n")

# O loop vai rodar até não sobrar ninguém em nenhuma das filas
while True:
    cliente_atendido = banco.proximo_da_vez()
    
    # Se o método retornou None, é porque as filas acabaram
    if cliente_atendido is None:
        break
        
    print(f"ATENDENDO AGORA: {cliente_atendido}")

print("\n--- TODOS OS CLIENTES FORAM ATENDIDOS ---")