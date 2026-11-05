#include <stdio.h>

int main() {
    // Vetor de 10 posicoes com os precos simulados (em R$)
    float precos_supermercado[10] = {23.90, 5.49, 31.75, 8.99, 4.29, 18.60, 12.35, 2.79, 27.40, 9.15};

    // Exibicao dos dados originais (nao ordenados)
    printf("--- Precos Originais (Nao Ordenados) ---\n");
    for(int i = 0; i < 10; i++) {
        printf("Produto %d: R$ %.2f\n", i + 1, precos_supermercado[i]);
    }
    printf("\n");

    // Logica do Bubble Sort para ordenacao em ordem crescente
    for (int i = 0; i < 10 - 1; i++) {
        for (int j = 0; j < 10 - i - 1; j++) {
            // Compara elementos adjacentes
            if (precos_supermercado[j] > precos_supermercado[j + 1]) {
                // Utilizacao da variavel temporaria para realizar a troca (swap)
                float temp = precos_supermercado[j];
                precos_supermercado[j] = precos_supermercado[j + 1];
                precos_supermercado[j + 1] = temp;
            }
        }
    }

    // Exibicao dos dados ordenados de forma crescente
    printf("--- Precos Ordenados (Ordem Crescente) ---\n");
    for (int i = 0; i < 10; i++) {
        printf("Posicao %d: R$ %.2f\n", i + 1, precos_supermercado[i]);
    }
    printf("\n");

    // Logica do Bubble Sort para ordenacao em ordem decrescente
    for (int i = 0; i < 10 - 1; i++) {
        for (int j = 0; j < 10 - i - 1; j++) {
            // Compara elementos adjacentes: se o atual for MENOR que o proximo, ocorre a troca
            if (precos_supermercado[j] < precos_supermercado[j + 1]) {
                // Utilizacao da variavel temporaria para realizar a troca (swap)
                float temp = precos_supermercado[j];
                precos_supermercado[j] = precos_supermercado[j + 1];
                precos_supermercado[j + 1] = temp;
            }
        }
    }

    // Exibicao dos dados ordenados de forma decrescente
    printf("--- Precos Ordenados (Ordem Decrescente) ---\n");
    for (int i = 0; i < 10; i++) {
        printf("Posicao %d: R$ %.2f\n", i + 1, precos_supermercado[i]);
    }
    printf("\n");

    return 0;
}