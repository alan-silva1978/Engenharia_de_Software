-- ============================================================================
-- SCRIPT DE POVOAMENTO (DML - INSERT)
-- Projeto: Sistema de Gestão de Frotas - Tinta Certa (tinta_certa_frota)
-- Ordem respeitada: Entidades independentes primeiro, dependentes depois.
-- ============================================================================

-- 1. Inserção na tabela USUARIO (Tabela independente: gestores e acessos de motoristas)
INSERT INTO usuario (nome, email, perfil, ativo) VALUES
('Ana Paula Souza', 'ana.gestao@tintacerta.com.br', 'GESTOR', TRUE),
('Carlos Eduardo Lima', 'carlos.lima@tintacerta.com.br', 'MOTORISTA', TRUE),
('Marcos Vinícius Rocha', 'marcos.rocha@tintacerta.com.br', 'MOTORISTA', TRUE);

-- 2. Inserção na tabela MOTORISTA (Depende de USUARIO via id_usuario opcional)
-- Nota: O terceiro motorista não possui login (id_usuario = NULL) para demonstrar relacionamento opcional.
INSERT INTO motorista (id_usuario, nome, cpf, data_nascimento, telefone, numero_cnh, categoria_cnh, validade_cnh, ativo) VALUES
(2, 'Carlos Eduardo Lima', '12345678901', '1988-04-15', '41999887766', '01234567890', 'B', '2028-04-15', TRUE),
(3, 'Marcos Vinícius Rocha', '98765432100', '1982-11-22', '41988776655', '09876543210', 'D', '2027-08-10', TRUE),
(NULL, 'Roberto Ferreira', '45678912309', '1995-02-08', '41977665544', '04567891230', 'AB', '2029-01-30', TRUE);

-- 3. Inserção na tabela VEICULO (Tabela independente; placas padronizadas sem hífen)
INSERT INTO veiculo (placa, marca, modelo, ano_fabricacao, ano_modelo, cor, tipo_combustivel, renavam, chassi, numero_motor, km_atual, ativo, categoria_cnh_exigida) VALUES
('ABC1D23', 'Fiat', 'Fiorino Endurance', 2023, 2024, 'Branco', 'FLEX', '12345678901', '9BD2651J2R9234567', 'MOTFIRE14001', 28385, TRUE, 'B'),
('DEF4567', 'Volkswagen', 'Delivery Express', 2022, 2022, 'Prata', 'DIESEL', '23456789012', '9536E5238NR123456', 'MOTCUMM28002', 64200, TRUE, 'B'),
('GHI8J90', 'Honda', 'CG 160 Cargo', 2024, 2024, 'Branco', 'FLEX', '34567890123', '9C2KC2200RR012345', 'MOTCG160003', 9800, TRUE, 'A');

-- 4. Inserção na tabela OFICINA (Tabela independente com endereço fracionado na 1FN)
-- Nota: A terceira oficina foi cadastrada apenas para cotação e não possui serviços vinculados.
INSERT INTO oficina (nome, cnpj, cep, logradouro, numero, complemento, bairro, cidade, uf, telefone) VALUES
('Auto Mecânica Paraná Ltda', '12345678000190', '80250000', 'Av. Sete de Setembro', '1450', 'Barracão 2', 'Rebouças', 'Curitiba', 'PR', '4133221100'),
('Diesel Center Curitiba', '98765432000110', '81110000', 'Rua Anne Frank', '3200', NULL, 'Boqueirão', 'Curitiba', 'PR', '4132889900'),
('Auto Elétrica Sul Ltda', '45612378000155', '81900000', 'Rua Nicola Pellanda', '980', NULL, 'Umbará', 'Curitiba', 'PR', '4133557788');

-- 5. Inserção na tabela REGISTRO_USO (Depende de VEICULO e MOTORISTA)
-- Nota: O terceiro registro está em aberto (data_hora_retorno e km_final NULL), simulando veículo em rota.
INSERT INTO registro_uso (id_veiculo, id_motorista, data_hora_saida, km_inicial, finalidade, data_hora_retorno, km_final, observacoes) VALUES
(1, 1, '2026-11-18 08:15:00', 28310, 'Entrega de tintas - Região Central', '2026-11-18 11:40:00', 28385, 'Entrega concluída sem ocorrências.'),
(2, 2, '2026-11-19 07:30:00', 64050, 'Entrega de carga volumosa - Obra Batel', '2026-11-19 16:20:00', 64200, 'Leve arranhão identificado no para-choque ao retornar.'),
(3, 3, '2026-11-22 09:00:00', 9800, 'Entrega expressa de pigmentos - Água Verde', NULL, NULL, 'Motoboy em rota de entrega.');

-- 6. Inserção na tabela ABASTECIMENTO (Depende de VEICULO e MOTORISTA)
-- Nota: O quarto registro repete o terceiro, digitado manualmente sem código de transação,
-- simulando um lançamento em duplicidade que será tratado no script de exclusão.
INSERT INTO abastecimento (id_veiculo, id_motorista, data_abastecimento, km_hodometro, litros, valor_total, foto_cupom, nome_posto, tipo_combustivel, codigo_transacao) VALUES
(1, 1, '2026-11-18', 28350, 38.50, 223.30, '/uploads/cupons/cupom_20261118_01.jpg', 'Posto Pelanda Rebouças', 'GASOLINA', 'PRIME-998811'),
(2, 2, '2026-11-19', 64120, 85.00, 509.15, '/uploads/cupons/cupom_20261119_02.jpg', 'Posto Shell Linha Verde', 'DIESEL', 'PRIME-998845'),
(3, 3, '2026-11-20', 9780, 12.20, 48.68, '/uploads/cupons/cupom_20261120_03.jpg', 'Auto Posto Batel', 'ETANOL', 'PRIME-998902'),
(3, 3, '2026-11-20', 9780, 12.20, 48.68, NULL, 'Auto Posto Batel', 'ETANOL', NULL);

-- 7. Inserção na tabela MANUTENCAO (Depende de VEICULO e OFICINA)
-- Nota: O segundo registro possui valor_total NULL, simulando veículo recém-deixado na oficina aguardando orçamento.
INSERT INTO manutencao (id_veiculo, id_oficina, data, km_hodometro, tipo_servico, descricao, valor_total, numero_os) VALUES
(1, 1, '2026-11-10', 28000, 'PREVENTIVA', 'Troca de óleo, filtro de óleo, filtro de ar e alinhamento.', 485.00, 'OS-2026-0412'),
(2, 2, '2026-11-21', 64200, 'CORRETIVA', 'Verificação de ruído na suspensão dianteira e revisão de freios.', NULL, 'OS-2026-0458');

-- 8. Inserção na tabela AVARIA (Depende de REGISTRO_USO)
INSERT INTO avaria (id_uso, data_registro, descricao, gravidade, resolvida, foto) VALUES
(2, '2026-11-19 16:25:00', 'Arranhão superficial no canto direito do para-choque traseiro durante manobra de descarga.', 'LEVE', FALSE, '/uploads/avarias/avaria_20261119_01.jpg');