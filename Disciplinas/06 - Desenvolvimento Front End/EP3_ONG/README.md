# 🤝 Plataforma Integrada - ONG Ação e Vida

> Sistema digital (Single Page Application) desenvolvido para otimizar o cadastro de voluntários e a gestão do diário de distribuições em comunidades vulneráveis.

## 🎯 Objetivo Tático do Projeto
A plataforma "Ação e Vida" foi construída sob rígidos padrões de **Governança**, **Responsabilidade Social** e **Cidadania Digital**. O objetivo é fornecer uma ferramenta de campo ágil, que opere com baixo consumo de dados (Sustentabilidade/TI Verde) e seja 100% acessível para voluntários com limitações motoras ou visuais, mitigando o viés de exclusão algorítmica.

## 🛠️ Arquitetura e Tecnologias
O projeto foi desenvolvido com uma *stack* nativa (sem dependências pesadas de back-end), garantindo a premissa de Entrada Mínima Viável (*Minimum Viable Input*):

*   **HTML5 Semântico:** Uso de *Landmarks* (`<main>`, `<nav>`, `<header>`) para estruturação lógica.
*   **CSS3 (Variáveis e Acessibilidade):** Implementação de perfis cromáticos de alto contraste (Nível AAA) e Otimização de Área Útil (*Viewport*).
*   **Vanilla JavaScript (ES6+):** Motor lógico modularizado para roteamento dinâmico e validação matemática de dados (Regex).
*   **Web Storage API (localStorage):** Persistência de dados local, garantindo a operação do voluntário em áreas de sombra de rede (sem internet).
*   **Vite:** Ferramenta de empacotamento (*Bundler*) utilizada para minificar o código e otimizar o tempo de carregamento em produção.

## ♿ Conformidade e Acessibilidade (WCAG 2.1 - Nível AA)
A interface foi projetada com foco em usabilidade sob estresse operacional:
*   **WAI-ARIA:** Suporte integral a leitores de tela nativos (NVDA, VoiceOver) através de alertas de estado (`aria-invalid`, `aria-live`).
*   **Navegação por Teclado:** Controle de foco (`:focus-visible`) para operação completa sem necessidade de mouse.
*   **Área de Toque Ampliada:** Botões de ação expandidos para prevenir erros de toque acidental em dispositivos móveis.

## 🚀 Como Executar o Projeto Localmente (Onboarding)

### Pré-requisitos
*   Git instalado na máquina.
*   Navegador web moderno (Chrome, Edge, Firefox).

### Passo a Passo da Instalação
1. Clone o repositório para a sua máquina local (Link Oficial):
   ```bash
   git clone https://github.com/alan-silva1978/Engenharia_de_Software.git
   cd "Engenharia_de_Software/Disciplinas/06 - Desenvolvimento Front End/EP3_ONG"