// Arquivo: js/main.js
// Responsabilidade Única: Roteamento da SPA (Single Page Application)

import { aplicarMascaras } from './modules/mascaras.js';
import { configurarFormularios, inicializarListeners } from './modules/storage.js';

const appContainer = document.getElementById('app-root');

// Os ouvintes globais de clique e submit são inicializados apenas UMA VEZ,
// fora do roteador, para não serem duplicados a cada troca de rota.
inicializarListeners();

function renderizarRota() {
    const rotaAtiva = window.location.hash || '#home';
    appContainer.innerHTML = '';

    if (rotaAtiva === '#home') {
        appContainer.innerHTML = `
            <section id="sobre" style="text-align: center; padding: 20px;">
                <h2 id="titulo-secao">Bem-vindo à ONG Ação e Vida</h2>
                <p style="font-size: 1.1em; margin-bottom: 20px;">Trabalhamos para levar esperança, suprimentos e apoio logístico para comunidades em situação de vulnerabilidade.</p>
                <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                    <a href="#acoes" style="padding: 12px 24px; text-decoration: none; background-color: #3498db; color: white; border-radius: 5px; font-weight: bold;">Conheça Nossas Ações</a>
                    <a href="#voluntarios" style="padding: 12px 24px; text-decoration: none; background-color: #1a7a42; color: white; border-radius: 5px; font-weight: bold;">Quero ser Voluntário</a>
                </div>
            </section>
        `;
    }
    else if (rotaAtiva === '#acoes') {
        appContainer.innerHTML = `
            <section id="painel-acoes">
                <h2 id="titulo-secao">O Nosso Impacto Social</h2>
                <article style="background-color: #f9f9f9; padding: 15px; margin-bottom: 15px; border-left: 5px solid #1a7a42;">
                    <h3>Distribuição de Alimentos (Em Andamento)</h3>
                    <p>Atuamos na linha de frente garantindo a segurança alimentar de 500 famílias cadastradas na região metropolitana.</p>
                </article>
                <div style="text-align: center; margin-top: 20px;">
                    <a href="#voluntarios" style="padding: 10px 20px; background-color: #2c3e50; color: white; text-decoration: none; border-radius: 5px;">Junte-se à Equipe</a>
                </div>
            </section>
        `;
    }
    else if (rotaAtiva === '#voluntarios') {
        appContainer.innerHTML = `
            <section id="cadastro-voluntario">
                <h2 id="titulo-secao">Cadastro de Novos Voluntários</h2>
                <form id="form-cadastro">
                    <fieldset>
                        <legend>Dados Pessoais</legend>
                        <label for="nome">Nome Completo:</label>
                        <input type="text" id="nome" placeholder="Digite seu nome completo" required>

                        <label for="cpf" id="label-cpf">CPF (Apenas números):</label>
                        <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" aria-describedby="cpf-erro" required>
                        <span id="cpf-erro" class="mensagem-erro" role="alert"></span>

                        <label for="telefone">Telefone de Contato:</label>
                        <input type="tel" id="telefone" name="telefone" placeholder="(00) 00000-0000" aria-describedby="telefone-erro" required>
                        <span id="telefone-erro" class="mensagem-erro" role="alert"></span>

                        <label for="area">Área de Atuação de Interesse:</label>
                        <select id="area" name="area">
                            <option value="Distribuição de Alimentos">Distribuição de Alimentos</option>
                            <option value="Administrativo">Administrativo</option>
                            <option value="Captação de Recursos">Captação de Recursos</option>
                        </select>
                    </fieldset>
                    <button type="submit" style="background-color: #27ae60;">Enviar Solicitação</button>
                </form>

                <div id="lista-voluntarios-cadastrados" style="margin-top: 25px;"></div>
            </section>
        `;
    }
    else if (rotaAtiva === '#login') {
        appContainer.innerHTML = `
            <section id="autenticacao" style="max-width: 400px; margin: 0 auto; text-align: center;">
                <h2 id="titulo-secao">Área Restrita</h2>
                <form id="form-login">
                    <label for="cpf-login" style="text-align: left;">CPF Operacional:</label>
                    <input type="text" id="cpf-login" required style="margin-bottom: 15px;" aria-describedby="cpf-login-erro">
                    <span id="cpf-login-erro" class="mensagem-erro" role="alert"></span>
                    <label for="senha" style="text-align: left;">Senha de Acesso:</label>
                    <input type="password" id="senha" required style="margin-bottom: 20px;">
                    <button type="submit" style="background-color: #B00020; color: white;">Autenticar e Assumir Turno</button>
                </form>
            </section>
        `;
    }
    else if (rotaAtiva === '#diario') {
        appContainer.innerHTML = `
            <section id="formulario-registro">
                <h2 id="titulo-secao">Diário de Distribuições</h2>

                <!-- PELOTÃO 1: REGISTRO DO TURNO -->
                <form id="form-diario" style="margin-bottom: 30px; padding-bottom: 20px; border-bottom: 2px solid #ccc;">
                    <fieldset>
                        <legend>1. Registro do Turno de Distribuição</legend>
                        <div id="ultimo-registro"></div>
                        <label for="itensDistribuidos">Quantidade de Kits Distribuídos:</label>
                        <input type="number" id="itensDistribuidos" name="itensDistribuidos">

                        <label for="assuncao">Data e Hora de Início do Turno:</label>
                        <input type="datetime-local" id="assuncao" name="assuncao">

                        <button type="submit" style="background-color: #2c3e50;">Registrar Turno</button>
                    </fieldset>
                </form>

                <!-- PELOTÃO 2: OCORRÊNCIAS NA DISTRIBUIÇÃO -->
                <div id="gestao-ocorrencias">
                    <fieldset>
                        <legend>2. Ocorrências e Itens Impróprios para Doação</legend>

                        <div id="lista-ocorrencias-ativas"></div>

                        <details style="margin-top: 15px; padding: 10px; background-color: #f9f9f9; border-radius: 5px;">
                            <summary style="font-weight: bold; color: #B00020; cursor: pointer;">+ Reportar Nova Ocorrência</summary>

                            <label for="descricao-ocorrencia">Descrição da Ocorrência:</label>
                            <input type="text" id="descricao-ocorrencia" placeholder="Ex: Alimento com validade vencida">

                            <button type="button" id="btn-gravar-ocorrencia" style="background-color: #e67e22; margin-top: 10px;">Registrar Ocorrência</button>
                        </details>
                    </fieldset>
                </div>
            </section>
        `;
    }

    // ACIONANDO OS PELOTÕES APÓS A RENDERIZAÇÃO
    aplicarMascaras();
    configurarFormularios();

        // --- GESTÃO DE FOCO: acessibilidade na troca de rota da SPA ---
    const tituloFoco = appContainer.querySelector('#titulo-secao');
    if (tituloFoco) {
        tituloFoco.setAttribute('tabindex', '-1');
        tituloFoco.focus();
    }
}

window.addEventListener('hashchange', renderizarRota);
window.addEventListener('load', renderizarRota);