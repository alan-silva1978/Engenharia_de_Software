"""
Sistema de Gerenciamento de Estoque - DataCode Solutions.
Estrutura do dicionário 'estoque':
{ 'nome_do_produto': {'quantidade': int, 'preco': float} }
"""

# JUSTIFICATIVA TÉCNICA:
# Optei por utilizar um Dicionário de Dicionários para modelar o estoque.
# Essa estrutura permite busca direta e eficiente pelo produto através da chave.
# NOTA SOBRE OS ATRIBUTOS: O 'nome' do produto (string) é representado 
# de forma otimizada pela própria chave do dicionário externo ("Monitor", 
# "Teclado", "Mouse"), eliminando redundância de dados. Os atributos de 
# 'quantidade' (int) e 'preço' (float) compõem o dicionário interno.

estoque = {
    "Monitor": {
        "quantidade": 15,
        "preco": 850.50
    },
    "Teclado": {
        "quantidade": 42,
        "preco": 120.00
    },
    "Mouse": {
        "quantidade": 30,
        "preco": 75.90
    }
}

# Início do laço de repetição para manter o sistema ativo
while True:
    # Exibição do Menu de Interface ao Usuário
    print("\n========= MENU PRINCIPAL - GESTÃO DE ESTOQUE =========")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    print("======================================================")

    # Coleta da opção escolhida pelo usuário
    opcao = input("Selecione a operação desejada (1-4): ")

    # === INÍCIO DO DIRECIONAMENTO DE TRÁFEGO ===

    if opcao == '1':
        print("\n--- RELATÓRIO DE ESTOQUE ATUAL ---")
        for produto, dados in estoque.items():
            print(f"Produto: {produto} | Quantidade: {dados['quantidade']} | Preço: R$ {dados['preco']:.2f}")
        print("----------------------------------")

    elif opcao == '2':
        print("\n--- REGISTRAR ENTRADA DE PRODUTO ---")
        nome_produto = input("Digite o nome do produto: ")

        # INÍCIO DA BLINDAGEM (try / except)
        try:
            # O sistema TENTA converter a digitação em número inteiro
            qtde_entrada = int(input("Digite a quantidade de entrada: "))

            # Intervenção Cirúrgica 2: Validação > 0 na Opção 2
            if qtde_entrada > 0:
                # Se a conversão der certo, o código continua normalmente:
                if nome_produto in estoque:
                    estoque[nome_produto]['quantidade'] += qtde_entrada
                    print(f"Sucesso! {qtde_entrada} unidades adicionadas ao produto '{nome_produto}'.")
                else:
                    print("Produto não encontrado.")
            else:
                print("ERRO: A quantidade deve ser um valor positivo. Operação abortada.")

        # Se o usuário digitar texto em vez de número, o ValueError explode e cai aqui:
        except ValueError:
            print("ERRO DE DIGITAÇÃO: A quantidade deve ser um número inteiro válido. Operação abortada.")

    elif opcao == '3':
        print("\n--- REGISTRAR SAÍDA DE PRODUTO ---")
        nome_produto = input("Digite o nome do produto para saída: ")

        # Primeira barreira: Prevenção de quebra do sistema por erro de digitação
        try:
            qtde_saida = int(input("Digite a quantidade para saída: "))

            # Intervenção Cirúrgica 3: Validação > 0 na Opção 3
            if qtde_saida > 0:
                # Segunda barreira: O produto existe no banco de dados?
                if nome_produto in estoque:

                    # Terceira barreira: O saldo atual atende à demanda?
                    if qtde_saida <= estoque[nome_produto]['quantidade']:
                        # Operação de dedução no dicionário
                        estoque[nome_produto]['quantidade'] -= qtde_saida
                        print(f"Sucesso! {qtde_saida} unidades removidas do produto '{nome_produto}'.")
                    else:
                        # Trava de segurança contra estoque negativo exigida pelo enunciado
                        print("Estoque insuficiente.")

                else:
                    # Mensagem exata exigida pelo enunciado
                    print("Produto não encontrado.")
            else:
                print("ERRO: A quantidade deve ser um valor positivo. Operação abortada.")

        # Tratamento de exceção caso o input da quantidade não seja um número inteiro
        except ValueError:
            print("ERRO DE DIGITAÇÃO: A quantidade deve ser um número inteiro válido. Operação abortada.")

    elif opcao == '4':
        print("\n--- ENCERRANDO O SISTEMA ---")
        print("Sessão finalizada com segurança. Até logo!")
        # O comando break encerra o loop while True de forma cirúrgica
        break

    else:
        # Fallback global: captura qualquer input fora do escopo (1 a 4)
        print("\nALERTA: Opção inválida. Por favor, selecione um comando válido de 1 a 4.")