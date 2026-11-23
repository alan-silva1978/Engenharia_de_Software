-- ============================================================================
-- SCRIPT DE ATUALIZAÇÃO CONDICIONAL (DML - UPDATE)
-- Projeto: Sistema de Gestão de Frotas - Tinta Certa (tinta_certa_frota)
-- ============================================================================

-- 1. Encerrar o registro de uso em aberto (retorno da moto CG 160 da entrega)
UPDATE registro_uso
SET data_hora_retorno = '2026-11-22 10:35:00',
    km_final = 9825,
    observacoes = 'Entrega expressa concluída com sucesso.'
WHERE id_uso = 3;

-- 2. Atualizar a quilometragem atual da moto após o encerramento da rota
-- Nota: km_atual é uma redundância controlada (repete o último km_final do veículo)
-- e por isso precisa ser atualizado junto com o encerramento do uso.
UPDATE veiculo
SET km_atual = 9825
WHERE placa = 'GHI8J90';

-- 3. Marcar como resolvida a avaria do para-choque após o reparo
-- (a condição resolvida = FALSE evita alterar um registro já encerrado)
UPDATE avaria
SET resolvida = TRUE
WHERE id_avaria = 1 AND resolvida = FALSE;


-- ============================================================================
-- SCRIPT DE EXCLUSÃO SEGURA (DML - DELETE)
-- Projeto: Sistema de Gestão de Frotas - Tinta Certa (tinta_certa_frota)
-- ============================================================================

-- 1. Excluir o abastecimento lançado em duplicidade (cópia manual sem código de transação)
-- A condição codigo_transacao IS NULL preserva o lançamento original 'PRIME-998902'.
DELETE FROM abastecimento
WHERE id_abastecimento = 4 AND codigo_transacao IS NULL;

-- 2. Excluir a ordem de serviço cujo orçamento foi recusado antes da execução
-- A condição valor_total IS NULL impede apagar uma OS que já teve valor aprovado.
DELETE FROM manutencao
WHERE numero_os = 'OS-2026-0458' AND valor_total IS NULL;

-- 3. Excluir a oficina cadastrada apenas para cotação (tabela principal sem registros dependentes)
DELETE FROM oficina
WHERE cnpj = '45612378000155';

-- Observação sobre integridade referencial (teste executado no pgAdmin):
-- DELETE FROM veiculo WHERE placa = 'ABC1D23';
-- Resultado: ERRO: atualização ou exclusão em tabela "veiculo" viola restrição de
-- chave estrangeira "registro_uso_id_veiculo_fkey" em "registro_uso" (SQL state 23503).
-- O veículo possui usos, abastecimentos e manutenção vinculados. Para retirá-lo
-- da frota sem perder o histórico, o caminho correto é:
-- UPDATE veiculo SET ativo = FALSE WHERE placa = 'ABC1D23';