#include <stdio.h>

int main() {
    // 1. Declaracao de variaveis de controle de fluxo e leitura
    int opcao = -1;
    int opcao_item = 0;
    int quantidade = 0;
    int retorno_leitura = 0;
    
    // 2. Declaracao de variaveis financeiras (Acumuladores)
    float subtotal = 0.0;
    float desconto = 0.0;
    float total = 0.0;
    
    // 3. Contadores da quantidade pedida de cada item do cardapio
    int qtd_prato1 = 0, qtd_prato2 = 0, qtd_prato3 = 0;
    int qtd_bebida1 = 0, qtd_bebida2 = 0, qtd_bebida3 = 0;
    int qtd_sobremesa1 = 0, qtd_sobremesa2 = 0, qtd_sobremesa3 = 0;

    // --- MENSAGEM INICIAL DE BOAS-VINDAS E CONTEXTUALIZACAO ---
    printf("=====================================================\n");
    printf("            BEM-VINDO AO CARDAPIO DIGITAL            \n");
    printf("=====================================================\n");
    printf("Navegue pelo nosso menu interativo digitando o numero da opcao desejada.\n");
    printf("O sistema registrara seus itens e calculara o total automaticamente.\n");
    printf("E um prazer receber voce. Vamos comecar o seu pedido?\n");

    // --- LACO DE REPETICAO PRINCIPAL (MENU) ---
    do {
        printf("\n--- MENU PRINCIPAL ---\n");
        printf("1 - Pratos\n");
        printf("2 - Bebidas\n");
        printf("3 - Sobremesas\n");
        printf("4 - Ver resumo do pedido\n");
        printf("0 - Finalizar pedido\n");
        printf("Escolha uma opcao: ");
        
        // Le a opcao e confere se foi digitado um numero inteiro
        retorno_leitura = scanf("%d", &opcao);
        
        if (retorno_leitura != 1) {
            printf("\n[AVISO] Entrada invalida. Por favor, digite apenas o numero da opcao.\n");
            while (getchar() != '\n'); // Descarta o que sobrou na entrada (ex: letras) ate o Enter
            opcao = -1; // Valor neutro para o laco continuar
            continue; 
        }

        // --- ESTRUTURAS DE DECISAO (PROCESSAMENTO DO FLUXO) ---
        switch (opcao) {
            case 1: // Categoria: Pratos
                printf("\n--- PRATOS ---\n");
                printf("1 - Feijoada Completa (R$ 45.00)\n");
                printf("2 - Bife a Cavalo (R$ 30.00)\n");
                printf("3 - Salada Executiva (R$ 22.00)\n");
                printf("Escolha o prato: ");
                
                if (scanf("%d", &opcao_item) != 1) {
                    printf("\n[AVISO] Entrada invalida. Retornando ao menu principal...\n");
                    while (getchar() != '\n');
                    break;
                }
                
                if (opcao_item >= 1 && opcao_item <= 3) {
                    printf("Digite a quantidade desejada: ");
                    if (scanf("%d", &quantidade) == 1 && quantidade > 0) {
                        if (opcao_item == 1) { qtd_prato1 += quantidade; subtotal += (quantidade * 45.00); }
                        else if (opcao_item == 2) { qtd_prato2 += quantidade; subtotal += (quantidade * 30.00); }
                        else if (opcao_item == 3) { qtd_prato3 += quantidade; subtotal += (quantidade * 22.00); }
                        printf("-> Item adicionado com sucesso!\n");
                    } else {
                        printf("\n[AVISO] Quantidade invalida. Operacao cancelada.\n");
                        while (getchar() != '\n');
                    }
                } else {
                    printf("\n[AVISO] A opcao de prato selecionada nao existe.\n");
                }
                break;

            case 2: // Categoria: Bebidas
                printf("\n--- BEBIDAS ---\n");
                printf("1 - Suco Natural de Laranja (R$ 9.00)\n");
                printf("2 - Refrigerante Lata (R$ 6.00)\n");
                printf("3 - Agua Mineral sem gas (R$ 4.00)\n");
                printf("Escolha a bebida: ");
                
                if (scanf("%d", &opcao_item) != 1) {
                    printf("\n[AVISO] Entrada invalida. Retornando ao menu principal...\n");
                    while (getchar() != '\n');
                    break;
                }
                
                if (opcao_item >= 1 && opcao_item <= 3) {
                    printf("Digite a quantidade desejada: ");
                    if (scanf("%d", &quantidade) == 1 && quantidade > 0) {
                        if (opcao_item == 1) { qtd_bebida1 += quantidade; subtotal += (quantidade * 9.00); }
                        else if (opcao_item == 2) { qtd_bebida2 += quantidade; subtotal += (quantidade * 6.00); }
                        else if (opcao_item == 3) { qtd_bebida3 += quantidade; subtotal += (quantidade * 4.00); }
                        printf("-> Item adicionado com sucesso!\n");
                    } else {
                        printf("\n[AVISO] Quantidade invalida. Operacao cancelada.\n");
                        while (getchar() != '\n');
                    }
                } else {
                    printf("\n[AVISO] A opcao de bebida selecionada nao existe.\n");
                }
                break;

            case 3: // Categoria: Sobremesas
                printf("\n--- SOBREMESAS ---\n");
                printf("1 - Pudim de Leite (R$ 12.00)\n");
                printf("2 - Taca de Sorvete (R$ 15.00)\n");
                printf("3 - Salada de Frutas (R$ 10.00)\n");
                printf("Escolha a sobremesa: ");
                
                if (scanf("%d", &opcao_item) != 1) {
                    printf("\n[AVISO] Entrada invalida. Retornando ao menu principal...\n");
                    while (getchar() != '\n');
                    break;
                }
                
                if (opcao_item >= 1 && opcao_item <= 3) {
                    printf("Digite a quantidade desejada: ");
                    if (scanf("%d", &quantidade) == 1 && quantidade > 0) {
                        if (opcao_item == 1) { qtd_sobremesa1 += quantidade; subtotal += (quantidade * 12.00); }
                        else if (opcao_item == 2) { qtd_sobremesa2 += quantidade; subtotal += (quantidade * 15.00); }
                        else if (opcao_item == 3) { qtd_sobremesa3 += quantidade; subtotal += (quantidade * 10.00); }
                        printf("-> Item adicionado com sucesso!\n");
                    } else {
                        printf("\n[AVISO] Quantidade invalida. Operacao cancelada.\n");
                        while (getchar() != '\n');
                    }
                } else {
                    printf("\n[AVISO] A opcao de sobremesa selecionada nao existe.\n");
                }
                break;

            case 4: // Ver resumo: exibe apenas os itens ja pedidos
                printf("\n--- RESUMO DO PEDIDO PARCIAL ---\n");
                if (subtotal == 0) {
                    printf("Seu carrinho esta vazio no momento.\n");
                } else {
                    if (qtd_prato1 > 0) printf("%d x Feijoada Completa\n", qtd_prato1);
                    if (qtd_prato2 > 0) printf("%d x Bife a Cavalo\n", qtd_prato2);
                    if (qtd_prato3 > 0) printf("%d x Salada Executiva\n", qtd_prato3);
                    
                    if (qtd_bebida1 > 0) printf("%d x Suco Natural de Laranja\n", qtd_bebida1);
                    if (qtd_bebida2 > 0) printf("%d x Refrigerante Lata\n", qtd_bebida2);
                    if (qtd_bebida3 > 0) printf("%d x Agua Mineral sem gas\n", qtd_bebida3);
                    
                    if (qtd_sobremesa1 > 0) printf("%d x Pudim de Leite\n", qtd_sobremesa1);
                    if (qtd_sobremesa2 > 0) printf("%d x Taca de Sorvete\n", qtd_sobremesa2);
                    if (qtd_sobremesa3 > 0) printf("%d x Salada de Frutas\n", qtd_sobremesa3);
                    
                    printf("--------------------------------\n");
                    printf("Subtotal provisorio: R$ %.2f\n", subtotal);
                }
                break;

            case 0: // Finalizar pedido
                printf("\nProcessando fechamento do pedido...\n");
                break;

            default: // Numero fora das opcoes do menu
                printf("\n[AVISO] Opcao invalida. Por favor, escolha um numero entre 0 e 4.\n");
                break;
        }
    } while (opcao != 0);

    // --- ENCERRAMENTO E EXIBICAO DOS TOTAIS ACUMULADOS ---
    printf("\n=====================================================\n");
    printf("                   NOTA DO PEDIDO                    \n");
    printf("=====================================================\n");
    
    if (subtotal == 0) {
        printf("Nenhum item foi selecionado. Sessao encerrada.\n");
        printf("Obrigado pela sua visita. Esperamos ve-lo em breve!\n");
    } else {
        // Bonus: desconto de 10% para consumo igual ou superior a R$ 100,00
        if (subtotal >= 100.00) {
            desconto = subtotal * 0.10;
        }
        
        total = subtotal - desconto;
        
        printf("Valor Subtotal : R$ %.2f\n", subtotal);
        if (desconto > 0) {
            printf("Desconto (10%%) : R$ %.2f\n", desconto);
        }
        printf("VALOR TOTAL    : R$ %.2f\n", total);
        
        // Mensagem de encerramento
        printf("\n-----------------------------------------------------\n");
        printf("Pedido finalizado com sucesso! \n");
        printf("Obrigado pela preferencia. Bom apetite e volte sempre!\n");
    }
    printf("=====================================================\n");

    return 0;
}