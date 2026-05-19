Jogo da Forca em Python 🐍
📌 Sobre o Projeto

Este projeto consiste em um Jogo da Forca interativo executado via terminal de linha de comando. Ele foi desenvolvido como Experiência Prática (EP3) durante o 1º semestre do curso de Engenharia de Software, com foco em consolidar fundamentos de algoritmos, interatividade e boas práticas de codificação.
⚙️ Conceitos e Arquitetura Aplicada

O código foi estruturado simulando um ambiente real de desenvolvimento, priorizando a organização e a eficiência:

    Modularização: O código foge do modelo de "script único". As responsabilidades foram divididas em funções específicas (Sargentos/Especialistas), como inicializar_jogo() e processar_tentativa(), isolando as lógicas de sorteio e verificação do motor principal do jogo.

    Estrutura de Dados Estratégica: Utilização de Listas (list) para criar o "tabuleiro mascarado" (mantendo a ordem posicional das letras) e Conjuntos (set) para registrar as tentativas do jogador, garantindo uma busca de complexidade O(1) e impedindo entradas duplicadas de forma nativa.

    Controle de Fluxo: Implementação de laço while com dupla condição de parada, gerenciando perfeitamente o ciclo de vida do jogo (vitória ao preencher lacunas ou derrota ao zerar vidas).

    Tratamento de Entrada e UX: Blindagem de inputs (utilizando .upper(), .strip() e .isalpha()) para evitar que erros de digitação do usuário quebrem o sistema, além de fornecer feedbacks visuais limpos e organizados no terminal.

🚀 Como Executar

    Certifique-se de ter o Python instalado em sua máquina.

    Clone este repositório ou baixe o arquivo jogo_forca.py.

    Abra o terminal (ou prompt de comando), navegue até a pasta do arquivo e execute o comando:

Bash

python jogo_forca.py

🛠️ Tecnologias Utilizadas

    Linguagem: Python 3.x

    Bibliotecas: random (Nativa)