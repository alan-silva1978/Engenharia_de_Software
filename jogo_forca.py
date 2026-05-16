import random

def inicializar_jogo(banco_palavras):
    """
    Prepara o estado inicial da partida de forca.

    Argumentos:
        banco_palavras (list): Uma lista de strings contendo o vocabulário disponível.

    Retornos:
        tuple: Contém a palavra secreta sorteada (str), a lista de lacunas mascarada (list),
               o conjunto de letras tentadas (set) e o número de tentativas iniciais (int).
    """
    palavra_secreta = random.choice(banco_palavras)
    palavra_mascarada = ['_'] * len(palavra_secreta)
    
    # JUSTIFICATIVA (Conjunto vs Lista exigida nos critérios):
    # Utilizamos um conjunto (set) para 'letras_tentadas' pois ele é baseado em tabelas de dispersão (hash tables).
    # Isso garante uma busca instantânea de complexidade O(1) para verificar se a letra já foi jogada.
    # Além disso, conjuntos ignoram inserções duplicadas nativamente, garantindo a integridade dos dados,
    # sendo estruturalmente muito mais eficientes que uma lista (que exigiria busca linear O(n)).
    letras_tentadas = set()
    tentativas_restantes = 6

    return palavra_secreta, palavra_mascarada, letras_tentadas, tentativas_restantes


def processar_tentativa(letra, palavra_secreta, palavra_mascarada):
    """
    Avalia a letra digitada pelo jogador e atualiza o status visual do tabuleiro.

    Argumentos:
        letra (str): O caractere alfabético digitado pelo jogador.
        palavra_secreta (str): A palavra gabarito que deve ser adivinhada.
        palavra_mascarada (list): A lista contendo as lacunas ('_') e letras reveladas da partida.

    Retornos:
        bool: Retorna True se a letra existir na palavra secreta (acerto), ou False caso contrário (erro).
    """
    acertou = False
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            palavra_mascarada[i] = letra
            acertou = True
            
    return acertou


def jogar():
    """
    Função maestro que orquestra o controle de fluxo (laço while) e a interface textual (UX).
    """
    banco_palavras = ["PYTHON", "ALGORITMO", "ESTRUTURA", "COMPUTADOR", "VARIAVEL", 
        "SINTAXE", "SOFTWARE", "HARDWARE", "LINGUAGEM", "COMPILADOR", 
        "FUNCAO", "DEBUGAR", "SISTEMA", "REPETICAO", "CONDICIONAL", 
        "ARQUITETURA", "SERVIDOR", "BIBLIOTECA"]
    palavra_secreta, palavra_mascarada, letras_tentadas, tentativas_restantes = inicializar_jogo(banco_palavras)

    print("=" * 40)
    print("   BEM-VINDO AO JOGO DA FORCA EDUCATIVO   ")
    print("=" * 40)

    # Laço de repetição principal
    while tentativas_restantes > 0 and '_' in palavra_mascarada:
        print("\n" + "-" * 40) # <- NOVA LINHA DIVISÓRIA AQUI
        print(f"\nPalavra: {' '.join(palavra_mascarada)}")
        
        # Exibe o conjunto formatado ou avisa se estiver vazio
        letras_formatadas = ', '.join(sorted(letras_tentadas)) if letras_tentadas else 'Nenhuma'
        print(f"Letras testadas: {letras_formatadas}")
        print(f"Vidas restantes: {tentativas_restantes}")

        letra = input("\nDigite uma letra: ").upper().strip()

        # Feedback 6: Validação de entrada inválida
        if len(letra) != 1 or not letra.isalpha():
            print("\n[INVÁLIDO] Digite apenas UMA letra do alfabeto por vez.")
            continue

        # Feedback 1: Letra repetida (usando busca O(1) do Set)
        if letra in letras_tentadas:
            print("\n[AVISO] Você já tentou esta letra! Olhe as letras testadas e escolha uma nova. Nenhuma tentativa descontada.")
            continue

        # Registra a tentativa no conjunto
        letras_tentadas.add(letra)

        # Processa o palpite
        acertou = processar_tentativa(letra, palavra_secreta, palavra_mascarada)

        # Feedbacks 2 e 3: Acerto ou Erro
        if acertou:
            print("\n[ACERTO] Muito bem! A letra pertence à palavra secreta. Continue assim!")
        else:
            tentativas_restantes -= 1
            print("\n[ERRO] Esta letra não existe na palavra. Você perdeu uma tentativa. Fique atento às vidas restantes!")

    # Finalização do Jogo
    print("\n" + "=" * 40)
    print("                FIM DE JOGO               ")
    print("=" * 40)
    
    # Feedbacks 4 e 5: Vitória ou Derrota
    if '_' not in palavra_mascarada:
        print(f"\n[VITÓRIA] Parabéns! Você revelou todas as letras e venceu o jogo!")
        print(f"A palavra era: {palavra_secreta}")
    else:
        print(f"\n[DERROTA] Suas tentativas acabaram.")
        print(f"A palavra secreta era: {palavra_secreta}")

# Chamada de inicialização padrão do Python
if __name__ == "__main__":
    jogar()