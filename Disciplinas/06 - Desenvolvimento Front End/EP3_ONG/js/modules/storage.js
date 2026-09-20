// Arquivo: js/modules/storage.js
// Responsabilidade: Validação, UX, Operação Offline, Gestão de Registros Locais e Prevenção de Duplo Clique (Debounce)

export function validarCPFMatematicamente(cpfBase) {
    const cpfLimpo = cpfBase.replace(/\D/g, '');
    if (cpfLimpo.length !== 11 || /^(\d)\1{10}$/.test(cpfLimpo)) return false;
    let soma = 0, resto;
    for (let i = 1; i <= 9; i++) soma += parseInt(cpfLimpo.substring(i-1, i)) * (11 - i);
    resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) resto = 0;
    if (resto !== parseInt(cpfLimpo.substring(9, 10))) return false;
    soma = 0;
    for (let i = 1; i <= 10; i++) soma += parseInt(cpfLimpo.substring(i-1, i)) * (12 - i);
    resto = (soma * 10) % 11;
    if (resto === 10 || resto === 11) resto = 0;
    if (resto !== parseInt(cpfLimpo.substring(10, 11))) return false;
    return true;
}

function renderizarListaOcorrencias() {
    const listaDiv = document.getElementById('lista-ocorrencias-ativas');
    if (!listaDiv) return;

    const dadosSalvos = JSON.parse(localStorage.getItem('dadosTurno') || '{"ocorrencias":[]}');
    const ocorrencias = dadosSalvos.ocorrencias || [];

    if (ocorrencias.length === 0) {
        listaDiv.innerHTML = '<div style="padding: 10px; background-color: #eafaf1; border-left: 5px solid #27ae60; color: #27ae60;"><strong>Turno em conformidade.</strong> Nenhuma ocorrência ativa registrada.</div>';
        return;
    }

    let html = '<ul style="list-style: none; padding: 0; margin: 0;">';
    ocorrencias.forEach((ocorrencia, index) => {
        html += `
            <li style="background: #fdedec; padding: 10px; margin-bottom: 8px; border-radius: 4px; border-left: 5px solid #e74c3c; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <span style="flex: 1;"><strong>Ocorrência Ativa:</strong> ${ocorrencia}</span>
                <button type="button" class="btn-excluir-ocorrencia" data-index="${index}" style="background: #c0392b; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-weight: bold; font-size: 0.85em;">Dar Baixa (Justificar)</button>
            </li>
        `;
    });
    html += '</ul>';
    listaDiv.innerHTML = html;
}

function renderizarListaVoluntarios() {
    const listaDiv = document.getElementById('lista-voluntarios-cadastrados');
    if (!listaDiv) return;

    const voluntarios = JSON.parse(localStorage.getItem('listaVoluntarios') || '[]');

    if (voluntarios.length === 0) {
        listaDiv.innerHTML = '';
        return;
    }

    const cardsHtml = voluntarios.map(voluntario => `
        <div class="card-voluntario">
            <strong>${voluntario.nomeCompleto}</strong>
            <span>${voluntario.areaAtuacao}</span>
            <span class="badge badge-ativo">${voluntario.status}</span>
        </div>
    `).join('');

    listaDiv.innerHTML = `
        <h3>Voluntários Cadastrados Recentemente</h3>
        <div class="lista-cards-voluntarios">${cardsHtml}</div>
    `;
}

// Ouvintes globais de clique e submit. Chamado apenas UMA VEZ pelo main.js
// (fora do roteador), para não duplicar o mapeamento de eventos a cada troca de rota.
export function inicializarListeners() {

    document.addEventListener('click', function(e) {

        // 1. AÇÃO: Gravar NOVA Ocorrência (Com Prevenção de Duplo Clique)
        if (e.target.id === 'btn-gravar-ocorrencia') {
            const btn = e.target;
            if (btn.disabled) return;
            btn.disabled = true;
            btn.style.opacity = '0.7';

            const campo = document.getElementById('descricao-ocorrencia');
            if (campo.value.trim() === '') {
                Swal.fire('Negado', 'Descreva a ocorrência antes de registrar.', 'warning').then(() => {
                    btn.disabled = false;
                    btn.style.opacity = '1';
                });
                return;
            }

            const dados = JSON.parse(localStorage.getItem('dadosTurno') || '{"ocorrencias":[]}');
            if (!dados.ocorrencias) dados.ocorrencias = [];

            dados.ocorrencias.push(campo.value.trim());
            localStorage.setItem('dadosTurno', JSON.stringify(dados));

            campo.value = '';
            renderizarListaOcorrencias();
            Swal.fire('Registrado', 'Nova ocorrência incorporada ao diário de distribuição.', 'success').then(() => {
                btn.disabled = false;
                btn.style.opacity = '1';
            });
        }

        // 2. AÇÃO: Excluir Ocorrência
        if (e.target.classList.contains('btn-excluir-ocorrencia')) {
            const index = e.target.getAttribute('data-index');

            Swal.fire({
                title: 'Baixa de Ocorrência',
                text: 'Para manter a Trilha de Auditoria, justifique a exclusão deste registro.',
                input: 'text',
                inputPlaceholder: 'Ex: Item retirado do estoque, ou Erro de registro...',
                showCancelButton: true,
                confirmButtonColor: '#27ae60',
                cancelButtonColor: '#7f8c8d',
                confirmButtonText: 'Confirmar Baixa',
                cancelButtonText: 'Cancelar',
                inputValidator: (value) => {
                    if (!value) return 'A justificativa é obrigatória!';
                }
            }).then((result) => {
                if (result.isConfirmed) {
                    const dados = JSON.parse(localStorage.getItem('dadosTurno') || '{"ocorrencias":[]}');
                    console.log(`[AUDITORIA] Ocorrência removida: "${dados.ocorrencias[index]}". Justificativa: "${result.value}"`);
                    dados.ocorrencias.splice(index, 1);
                    localStorage.setItem('dadosTurno', JSON.stringify(dados));
                    renderizarListaOcorrencias();
                    Swal.fire('Baixa Confirmada', 'O registro foi arquivado com a justificativa fornecida.', 'success');
                }
            });
        }
    });

    document.addEventListener('submit', function(e) {
        const campoCpf = e.target.querySelector('#cpf, #cpf-login, input[name="cpf"]');
        if (campoCpf) {
            if (!validarCPFMatematicamente(campoCpf.value)) {
                e.preventDefault();
                campoCpf.classList.add('input-erro');
                Swal.fire('Atenção', 'O CPF não é matematicamente válido.', 'error');
                return;
            } else {
                campoCpf.classList.remove('input-erro');
            }
        }

        if (e.target.id === 'form-cadastro') {
            e.preventDefault();

            const voluntario = {
                id: Date.now(),
                nomeCompleto: document.getElementById('nome').value,
                cpf: campoCpf.value,
                telefone: document.getElementById('telefone').value,
                areaAtuacao: document.getElementById('area').value,
                status: 'Pendente'
            };

            const voluntarios = JSON.parse(localStorage.getItem('listaVoluntarios') || '[]');
            voluntarios.push(voluntario);
            localStorage.setItem('listaVoluntarios', JSON.stringify(voluntarios));

            e.target.reset();
            renderizarListaVoluntarios();
            Swal.fire('Recebido!', 'Cadastro realizado.', 'success');
        }

        if (e.target.id === 'form-login') {
            e.preventDefault();
            const senha = document.getElementById('senha').value;
            if (senha.length < 6) {
                Swal.fire('Acesso Negado', 'A senha requer mínimo de 6 caracteres.', 'error');
                return;
            }
            window.location.hash = '#diario';
        }

        // 3. AÇÃO: Registrar Turno de Distribuição (Com Prevenção de Duplo Clique)
        if (e.target.id === 'form-diario') {
            e.preventDefault();

            const btnSubmit = e.target.querySelector('button[type="submit"]');
            if (btnSubmit && btnSubmit.disabled) return;
            if (btnSubmit) {
                btnSubmit.disabled = true;
                btnSubmit.style.opacity = '0.7';
            }

            const itensDistribuidos = document.getElementById('itensDistribuidos');
            const assuncao = document.getElementById('assuncao');
            let formValido = true;

            if (itensDistribuidos.value.trim() === '' || itensDistribuidos.value <= 0) {
                itensDistribuidos.classList.add('input-erro'); formValido = false;
            } else { itensDistribuidos.classList.remove('input-erro'); }

            if (assuncao.value.trim() === '') {
                assuncao.classList.add('input-erro'); formValido = false;
            } else { assuncao.classList.remove('input-erro'); }

            if (!formValido) {
                Swal.fire('Atenção', 'Preencha a quantidade distribuída e a data.', 'warning').then(() => {
                    if (btnSubmit) {
                        btnSubmit.disabled = false;
                        btnSubmit.style.opacity = '1';
                    }
                });
                return;
            }

            const dados = JSON.parse(localStorage.getItem('dadosTurno') || '{"ocorrencias":[]}');
            dados.itensDistribuidos = itensDistribuidos.value;
            dados.assuncao = assuncao.value;

            localStorage.setItem('dadosTurno', JSON.stringify(dados));
            e.target.reset();

            Swal.fire('Sucesso!', 'Turno registrado com sucesso.', 'success').then(() => {
                if (btnSubmit) {
                    btnSubmit.disabled = false;
                    btnSubmit.style.opacity = '1';
                }
                window.dispatchEvent(new Event('hashchange'));
            });
        }
    });
}

// Inicializações específicas de cada rota — chamadas a CADA renderização da SPA.
export function configurarFormularios() {

    const formDiario = document.getElementById('form-diario');
    if (formDiario) {
        const dados = JSON.parse(localStorage.getItem('dadosTurno') || '{}');
        const refDiv = document.getElementById('ultimo-registro');
        if (refDiv && dados.itensDistribuidos) {
            refDiv.innerHTML = `<span style="display: block; color: #e67e22; font-weight: bold; margin-bottom: 10px;">Último registro de distribuição: ${dados.itensDistribuidos} kits</span>`;
        }
        renderizarListaOcorrencias();
    }

    if (document.getElementById('lista-voluntarios-cadastrados')) {
        renderizarListaVoluntarios();
    }
}