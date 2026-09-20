// Arquivo: js/modules/mascaras.js
// Responsabilidade Única: Sanitização e Máscaras Interativas (Real-Time)

import { validarCPFMatematicamente } from './storage.js';

export function aplicarMascaras() {
    const camposCpf = document.querySelectorAll('#cpf, #cpf-login, input[name="cpf"]');
    camposCpf.forEach(campo => {
        campo.addEventListener('input', function (e) {
            let valor = e.target.value.replace(/\D/g, '');
            if (valor.length > 11) valor = valor.slice(0, 11);
            valor = valor.replace(/(\d{3})(\d)/, '$1.$2');
            valor = valor.replace(/(\d{3})(\d)/, '$1.$2');
            valor = valor.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
            e.target.value = valor;

            if (valor.length === 14) {
                if (validarCPFMatematicamente(valor)) {
                    campo.classList.remove('input-erro');
                    campo.classList.add('input-sucesso');
                } else {
                    campo.classList.remove('input-sucesso');
                    campo.classList.add('input-erro');
                }
            } else {
                campo.classList.remove('input-erro', 'input-sucesso');
            }
        });
    });

    const telInput = document.getElementById('telefone');
    if (telInput) {
        telInput.addEventListener('input', function (e) {
            let valor = e.target.value.replace(/\D/g, '');
            if (valor.length > 11) valor = valor.slice(0, 11);
            valor = valor.replace(/^(\d{2})(\d)/g, '($1) $2');
            valor = valor.replace(/(\d)(\d{4})$/, '$1-$2');
            e.target.value = valor;
        });
    }

    // --- MÁSCARA DA QUANTIDADE DISTRIBUÍDA ---
    const itensInput = document.getElementById('itensDistribuidos');
    if (itensInput) {
        itensInput.addEventListener('input', function (e) {
            e.target.value = e.target.value.replace(/\D/g, '');
        });
    }
}