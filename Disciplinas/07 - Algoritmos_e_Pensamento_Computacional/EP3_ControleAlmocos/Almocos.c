#include <stdio.h>

#define LIMITE_DIARIO 9999   // maior quantidade aceita por dia (cabe na coluna de 4 digitos)
#define TAMANHO_BARRA 40    // quantidade de asteriscos do dia de maior movimento

int main() {
    /* ======================================================================
       1. DECLARACAO DE ESTRUTURAS OBRIGATORIAS E VARIAVEIS
       ====================================================================== */
    int almocos[7];
    char dias[7][10] = {"Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"};
    
    int i, j;
    int total = 0;
    int maior, menor;
    int dias_acima_media = 0;
    float media;
    int validacao_entrada;
    int sobra;                 // caractere digitado logo apos o numero

    /* ======================================================================
       2. TELA DE BOAS-VINDAS
       ====================================================================== */
    printf("===================================================\n");
    printf("   CONTROLE DE ALMOCOS - Restaurante (7 dias)\n");
    printf("===================================================\n\n");

    /* ======================================================================
       3. LEITURA DOS DADOS COM VALIDACAO
       ====================================================================== */
    for(i = 0; i < 7; i++) {
        do {
            printf("Almocos servidos na %s: ", dias[i]);
            validacao_entrada = scanf("%d", &almocos[i]);
            
            // Confere o caractere logo apos o numero: deve ser o Enter.
            // Se for outra coisa (letra, ou "2x"), a entrada e invalida.
            sobra = getchar();
            if(sobra != '\n') {
                validacao_entrada = 0;
                // Descarta o restante da linha para evitar loop infinito
                while(sobra != '\n' && sobra != EOF) {
                    sobra = getchar();
                }
            }
            
            // Valida se a entrada nao e numero ou se esta fora da faixa de 0 a 9999
            if(validacao_entrada != 1 || almocos[i] < 0 || almocos[i] > LIMITE_DIARIO) {
                printf("[ERRO] Entrada invalida! Digite um numero inteiro de 0 a 9999.\n");
            }
            
        } while(validacao_entrada != 1 || almocos[i] < 0 || almocos[i] > LIMITE_DIARIO); // Trava no mesmo dia em caso de erro
        
        // Acumula o total de almocos servidos
        total += almocos[i];
    }

    /* ======================================================================
       4. PROCESSAMENTO DOS RESULTADOS
       ====================================================================== */
    // Conversao explicita (cast) para float: sem ela, a divisao entre
    // inteiros descartaria as casas decimais da media
    media = (float)total / 7;
    
    // Maior e menor comecam com o valor do primeiro dia (nunca com zero)
    maior = almocos[0];
    menor = almocos[0];
    
    // Inspeciona os dias restantes (indice 1 ao 6)
    for(i = 1; i < 7; i++) {
        if(almocos[i] > maior) {
            maior = almocos[i];
        }
        if(almocos[i] < menor) {
            menor = almocos[i];
        }
    }
    
    // Conta quantos dias superaram a media semanal
    for(i = 0; i < 7; i++) {
        if(almocos[i] > media) {
            dias_acima_media++;
        }
    }

    /* ======================================================================
       5. GERACAO DO RELATORIO FINAL E GRAFICO DE BARRAS
       ====================================================================== */
    printf("\n===================================================\n");
    printf("                RELATORIO SEMANAL\n");
    printf("===================================================\n");
    
    for(i = 0; i < 7; i++) {
        // Formata as colunas para alinhamento (10 espacos para o nome, 4 para o numero)
        printf("%-10s | %4d | ", dias[i], almocos[i]);
        
        // Barra proporcional ao dia de maior movimento: o pico recebe
        // TAMANHO_BARRA asteriscos e os demais dias, a fracao correspondente.
        // O teste maior > 0 evita divisao por zero numa semana toda zerada.
        int qtd_asteriscos = 0;
        if(maior > 0) {
            qtd_asteriscos = almocos[i] * TAMANHO_BARRA / maior;
            // Dia com movimento, mas pequeno demais para um asterisco inteiro
            if(almocos[i] > 0 && qtd_asteriscos == 0) {
                qtd_asteriscos = 1;
            }
        }
        for(j = 0; j < qtd_asteriscos; j++) {
            printf("*");
        }
        
        // Sinaliza o pico de movimento (marca todos os dias empatados).
        // Se a semana inteira foi zero, nao ha pico a destacar.
        if(almocos[i] == maior && maior > 0) {
            printf(" <- PICO");
        }
        printf("\n");
    }

    /* ======================================================================
       6. EXIBICAO DOS INDICADORES E TRATAMENTO DE EMPATES
       ====================================================================== */
    printf("\n--- ESTATISTICAS ---\n");
    printf("Total da semana......: %d\n", total);
    printf("Media semanal........: %.2f\n", media);
    printf("Dias acima da media..: %d\n", dias_acima_media);
    
    // Listagem de empates para o MAIOR valor
    printf("Maior movimento......: %d almocos em ", maior);
    for(i = 0; i < 7; i++) {
        if(almocos[i] == maior) {
            printf("%s ", dias[i]);
        }
    }
    printf("\n");
    
    // Listagem de empates para o MENOR valor
    printf("Menor movimento......: %d almocos em ", menor);
    for(i = 0; i < 7; i++) {
        if(almocos[i] == menor) {
            printf("%s ", dias[i]);
        }
    }
    printf("\n");
    printf("===================================================\n");

    return 0;
}