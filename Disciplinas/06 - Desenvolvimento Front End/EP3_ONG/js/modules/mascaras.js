// Arquivo: js/modules/mascaras.js
// Responsabilidade Única: Sanitização e Máscaras Interativas (Real-Time)

import { validarCPFMatematicamente } from './storage.js';

export function aplicarMascaras() {
    const camposCpf = document.querySelectorAll('#cpf, #cpf-login, input[name="cpf"]');
    camposCpf.forEach(campo => {
        const erroSpan = document.getElementById(campo.id + '-erro');
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
                    campo.setAttribute('aria-invalid', 'false');
                    if (erroSpan) { erroSpan.textContent = ''; erroSpan.style.display = 'none'; }
                } else {
                    campo.classList.remove('input-sucesso');
                    campo.classList.add('input-erro');
                    campo.setAttribute('aria-invalid', 'true');
                    if (erroSpan) { erroSpan.textContent = 'CPF inválido. Verifique os números digitados.'; erroSpan.style.display = 'block'; }
                }
            } else {
                campo.classList.remove('input-erro', 'input-sucesso');
                campo.removeAttribute('aria-invalid');
                if (erroSpan) { erroSpan.textContent = ''; erroSpan.style.display = 'none'; }
            }
        });
    });

    const telInput = document.getElementById('telefone');
    if (telInput) {
        const erroSpan = document.getElementById('telefone-erro');
        telInput.addEventListener('input', function (e) {
            let valor = e.target.value.replace(/\D/g, '');
            if (valor.length > 11) valor = valor.slice(0, 11);
            valor = valor.replace(/^(\d{2})(\d)/g, '($1) $2');
            valor = valor.replace(/(\d)(\d{4})$/, '$1-$2');
            e.target.value = valor;

            const digitos = valor.replace(/\D/g, '');
            if (digitos.length === 11) {
                telInput.classList.remove('input-erro');
                telInput.classList.add('input-sucesso');
                telInput.setAttribute('aria-invalid', 'false');
                if (erroSpan) { erroSpan.textContent = ''; erroSpan.style.display = 'none'; }
            } else if (digitos.length > 0) {
                telInput.classList.remove('input-sucesso');
                telInput.classList.add('input-erro');
                telInput.setAttribute('aria-invalid', 'true');
                if (erroSpan) { erroSpan.textContent = 'Telefone incompleto. Use o formato (00) 00000-0000.'; erroSpan.style.display = 'block'; }
            } else {
                telInput.classList.remove('input-erro', 'input-sucesso');
                telInput.removeAttribute('aria-invalid');
                if (erroSpan) { erroSpan.textContent = ''; erroSpan.style.display = 'none'; }
            }
        });
    }

    const itensInput = document.getElementById('itensDistribuidos');
    if (itensInput) {
        itensInput.addEventListener('input', function (e) {
            e.target.value = e.target.value.replace(/\D/g, '');
        });
    }
}