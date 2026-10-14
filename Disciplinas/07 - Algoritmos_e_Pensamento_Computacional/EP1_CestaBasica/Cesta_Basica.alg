algoritmo "CestaBasica"
// Disciplina: Algoritmos e Pensamento Computacional
// Experiencia Pratica I - Monitoramento do preco da cesta basica
// Autor: Alan Carlos da Silva

var
   nome1, nome2, nome3: caractere
   preco_anterior1, preco_anterior2, preco_anterior3: real
   preco_atual1, preco_atual2, preco_atual3: real
   variacao1, variacao2, variacao3: real
   situacao1, situacao2, situacao3: caractere

inicio
   escreval("--- MONITORAMENTO DA CESTA BÁSICA ---")

   // ---------- ENTRADA: PRODUTO 1 ----------
   escreval("Digite o nome do produto 1:")
   leia(nome1)
   escreval("Digite o preço no mês anterior (R$):")
   leia(preco_anterior1)
   escreval("Digite o preço no mês atual (R$):")
   leia(preco_atual1)

   // ---------- ENTRADA: PRODUTO 2 ----------
   escreval("Digite o nome do produto 2:")
   leia(nome2)
   escreval("Digite o preço no mês anterior (R$):")
   leia(preco_anterior2)
   escreval("Digite o preço no mês atual (R$):")
   leia(preco_atual2)

   // ---------- ENTRADA: PRODUTO 3 ----------
   escreval("Digite o nome do produto 3:")
   leia(nome3)
   escreval("Digite o preço no mês anterior (R$):")
   leia(preco_anterior3)
   escreval("Digite o preço no mês atual (R$):")
   leia(preco_atual3)

   // ---------- PROCESSAMENTO: VARIAÇÃO PERCENTUAL ----------
   variacao1 <- ((preco_atual1 - preco_anterior1) / preco_anterior1) * 100
   variacao2 <- ((preco_atual2 - preco_anterior2) / preco_anterior2) * 100
   variacao3 <- ((preco_atual3 - preco_anterior3) / preco_anterior3) * 100

   // Tolerância de 0.0001: números reais são aproximados no computador.
   // Sem ela, 4.00 -> 4.40 (exatamente 10%) seria calculado como
   // 10.000000000000009 e classificado, por engano, como abusivo.

   // ---------- DECISÃO: CLASSIFICAÇÃO DO PRODUTO 1 ----------
   se variacao1 > 10.0001 entao
      situacao1 <- "AUMENTO ABUSIVO"
   senao
      se variacao1 > 0 entao
         situacao1 <- "AUMENTO"
      senao
         se variacao1 < 0 entao
            situacao1 <- "QUEDA"
         senao
            situacao1 <- "ESTÁVEL"
         fimse
      fimse
   fimse

   // ---------- DECISÃO: CLASSIFICAÇÃO DO PRODUTO 2 ----------
   se variacao2 > 10.0001 entao
      situacao2 <- "AUMENTO ABUSIVO"
   senao
      se variacao2 > 0 entao
         situacao2 <- "AUMENTO"
      senao
         se variacao2 < 0 entao
            situacao2 <- "QUEDA"
         senao
            situacao2 <- "ESTÁVEL"
         fimse
      fimse
   fimse

   // ---------- DECISÃO: CLASSIFICAÇÃO DO PRODUTO 3 ----------
   se variacao3 > 10.0001 entao
      situacao3 <- "AUMENTO ABUSIVO"
   senao
      se variacao3 > 0 entao
         situacao3 <- "AUMENTO"
      senao
         se variacao3 < 0 entao
            situacao3 <- "QUEDA"
         senao
            situacao3 <- "ESTÁVEL"
         fimse
      fimse
   fimse

   // ---------- SAÍDA: RESUMO FINAL ----------
   escreval("")
   escreval("--- Resumo de variação de preços ---")
   escreval("")
   escreval("Produto: ", nome1)
   escreval("  Preço anterior: R$ ", preco_anterior1:6:2)
   escreval("  Preço atual: R$ ", preco_atual1:6:2)
   escreval("  Variação: ", variacao1:6:2, "%")
   escreval("  Situação: ", situacao1)
   escreval("")
   escreval("Produto: ", nome2)
   escreval("  Preço anterior: R$ ", preco_anterior2:6:2)
   escreval("  Preço atual: R$ ", preco_atual2:6:2)
   escreval("  Variação: ", variacao2:6:2, "%")
   escreval("  Situação: ", situacao2)
   escreval("")
   escreval("Produto: ", nome3)
   escreval("  Preço anterior: R$ ", preco_anterior3:6:2)
   escreval("  Preço atual: R$ ", preco_atual3:6:2)
   escreval("  Variação: ", variacao3:6:2, "%")
   escreval("  Situação: ", situacao3)
fimalgoritmo
