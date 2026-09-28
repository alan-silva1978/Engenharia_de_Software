# 🤝 Plataforma Integrada - ONG Ação e Vida

> Aplicação web de página única (SPA) para cadastro de voluntários e registro de distribuições de uma ONG.

🔗 **Versão publicada:** https://ongacaoevida.vercel.app/

## 🎯 Objetivo
Oferecer uma ferramenta leve, pensada para telas pequenas e conexões limitadas, que permita cadastrar voluntários e registrar turnos de distribuição e ocorrências, mantendo os dados no próprio navegador.

## 🛠️ Tecnologias
- **HTML5 semântico** (`header`, `nav`, `main`, `footer`)
- **CSS3** com variáveis (`:root`)
- **JavaScript (ES6+)** modularizado: `main.js` (rotas), `mascaras.js` (máscaras e validação em tempo real), `storage.js` (persistência e alertas)
- **localStorage** para guardar os dados no navegador
- **SweetAlert2** (via CDN) para caixas de diálogo
- **Vite** para gerar a versão de produção (minificação)
- **Vercel** para publicação

## 📁 Estrutura de pastas
```
EP3_ONG/
├── index.html
├── css/style.css
├── js/main.js
├── js/modules/mascaras.js
├── js/modules/storage.js
├── img/ (brasao-ong.png e brasao-ong.webp)
├── package.json
├── vite.config.js
└── .gitignore
```

## ♿ Acessibilidade (WCAG 2.1)
- Marcos semânticos e `aria-live="polite"` na área de conteúdo
- Campos de CPF e telefone com `aria-invalid` e `aria-describedby` apontando para a mensagem de erro
- Foco levado ao título (`h2`) a cada troca de tela
- Foco visível para navegação por teclado (`:focus-visible`)
- Brasão com texto alternativo, em WebP com alternativa PNG (`<picture>`)

**Limitações conhecidas:** ainda não houve teste com leitores de tela (NVDA/VoiceOver); a revisão de contraste de todas as cores está em andamento; os dados (inclusive CPF) ficam no `localStorage` sem criptografia. Para uso real seriam necessários servidor, consentimento explícito e política de privacidade (LGPD).

## 🚀 Como executar localmente
**Pré-requisitos:** Git, Node.js (versão LTS) e um navegador atual.

```bash
git clone https://github.com/alan-silva1978/Engenharia_de_Software.git
cd "Engenharia_de_Software/Disciplinas/06 - Desenvolvimento Front End/EP3_ONG"
npm install
npm run dev
```
Abra o endereço mostrado no terminal (normalmente http://localhost:5173).
⚠️ Não abra o `index.html` com duplo clique: módulos ES exigem um servidor.

**Versão de produção:** `npm run build` (gera a pasta `dist/`) e `npm run preview` (testa em http://localhost:4173).

## 🔀 Versionamento (GitFlow simplificado)
- `main`: versão em produção (a Vercel publica automaticamente a cada atualização)
- `develop`: integração
- `feature/nome-da-mudanca`: uma branch por mudança, com Pull Request para `develop` (confira que a **base** é `develop`); depois, Pull Request de `develop` para `main`
- `hotfix/`: correções urgentes a partir da `main` (ainda não utilizada neste projeto)
- Mensagens de commit no padrão Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`)
- `node_modules/` e `dist/` ficam no `.gitignore` e nunca são versionados

## ☁️ Deploy
Vercel conectada a este repositório, com *Root Directory* na pasta do projeto, comando `npm run build` e saída em `dist/`.