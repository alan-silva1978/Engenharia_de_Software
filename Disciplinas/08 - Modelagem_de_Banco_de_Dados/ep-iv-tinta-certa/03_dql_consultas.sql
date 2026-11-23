-- ============================================================================
-- SCRIPT DE CONSULTAS RELACIONAIS (DQL - SELECT)
-- Projeto: Sistema de Gestão de Frotas - Tinta Certa (tinta_certa_frota)
-- ============================================================================

-- 1. Relatório dos maiores abastecimentos (junção de três tabelas com INNER JOIN + WHERE + ORDER BY + LIMIT)
-- Objetivo: Cruzar abastecimento, veículo e motorista para identificar gastos acima de R$ 100,00.
SELECT 
    a.data_abastecimento,
    v.placa,
    v.modelo,
    m.nome AS motorista,
    a.nome_posto,
    a.tipo_combustivel,
    a.litros,
    a.valor_total
FROM abastecimento a
INNER JOIN veiculo v ON a.id_veiculo = v.id_veiculo
INNER JOIN motorista m ON a.id_motorista = m.id_motorista
WHERE a.valor_total > 100.00
ORDER BY a.valor_total DESC
LIMIT 5;

-- 2. Histórico de manutenções por oficina (INNER JOIN + WHERE + ORDER BY)
-- Objetivo: Listar serviços realizados ou em orçamento para veículos ativos da frota.
SELECT 
    man.numero_os,
    man.data,
    v.placa,
    v.modelo,
    o.nome AS oficina,
    o.cidade,
    man.tipo_servico,
    man.valor_total
FROM manutencao man
INNER JOIN veiculo v ON man.id_veiculo = v.id_veiculo
INNER JOIN oficina o ON man.id_oficina = o.id_oficina
WHERE v.ativo = TRUE
ORDER BY man.data DESC;

-- 3. Rastreamento de avarias pendentes (INNER JOIN encadeado + WHERE + ORDER BY)
-- Objetivo: Identificar avarias ainda não resolvidas, qual veículo foi afetado e quem o conduzia.
SELECT 
    av.data_registro,
    av.gravidade,
    v.placa,
    v.modelo,
    m.nome AS motorista_responsavel,
    ru.finalidade,
    av.descricao
FROM avaria av
INNER JOIN registro_uso ru ON av.id_uso = ru.id_uso
INNER JOIN veiculo v ON ru.id_veiculo = v.id_veiculo
INNER JOIN motorista m ON ru.id_motorista = m.id_motorista
WHERE av.resolvida = FALSE
ORDER BY av.data_registro DESC;

-- 4. Listagem de motoristas e seus acessos ao sistema (LEFT JOIN + ORDER BY + LIMIT)
-- Objetivo: Exibir todos os motoristas cadastrados, incluindo os que não possuem usuário de login (NULL).
SELECT 
    m.nome AS motorista,
    m.categoria_cnh,
    m.validade_cnh,
    u.email AS email_login,
    u.perfil
FROM motorista m
LEFT JOIN usuario u ON m.id_usuario = u.id_usuario
WHERE m.ativo = TRUE
ORDER BY m.nome ASC
LIMIT 10;

-- 5. Identificação do condutor em data e hora específicas (consulta para multas)
-- Objetivo: Responder "quem estava com o veículo DEF4567 em 19/11/2026 às 14h?",
-- considerando também um uso ainda em aberto (sem data de retorno).
SELECT 
    v.placa,
    v.modelo,
    m.nome AS condutor,
    m.numero_cnh,
    ru.data_hora_saida,
    ru.data_hora_retorno,
    ru.finalidade
FROM registro_uso ru
INNER JOIN veiculo v ON ru.id_veiculo = v.id_veiculo
INNER JOIN motorista m ON ru.id_motorista = m.id_motorista
WHERE v.placa = 'DEF4567'
  AND ru.data_hora_saida <= '2026-11-19 14:00:00'
  AND (ru.data_hora_retorno >= '2026-11-19 14:00:00' OR ru.data_hora_retorno IS NULL)
ORDER BY ru.data_hora_saida DESC
LIMIT 1;