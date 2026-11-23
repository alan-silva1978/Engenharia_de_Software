-- ==========================================================
-- 1. CRIAÇÃO DOS TIPOS ENUM (Padronização de domínios)
-- ==========================================================
CREATE TYPE perfil_usuario AS ENUM ('GESTOR', 'MOTORISTA');
CREATE TYPE tipo_combustivel_enum AS ENUM ('GASOLINA', 'ETANOL', 'FLEX', 'DIESEL', 'GNV', 'ELETRICO', 'HIBRIDO');
CREATE TYPE tipo_servico_enum AS ENUM ('PREVENTIVA', 'CORRETIVA');
CREATE TYPE gravidade_avaria_enum AS ENUM ('LEVE', 'MEDIA', 'GRAVE');
CREATE TYPE categoria_cnh_motorista_enum AS ENUM ('ACC', 'A', 'B', 'C', 'D', 'E', 'AB', 'AC', 'AD', 'AE');
CREATE TYPE categoria_cnh_veiculo_enum AS ENUM ('ACC', 'A', 'B', 'C', 'D', 'E');

-- ==========================================================
-- 2. CRIAÇÃO DAS TABELAS (Ordem de dependência)
-- ==========================================================
CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    perfil perfil_usuario NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE motorista (
    id_motorista SERIAL PRIMARY KEY,
    id_usuario INT UNIQUE REFERENCES usuario(id_usuario),
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    data_nascimento DATE NOT NULL,
    telefone VARCHAR(15),
    numero_cnh CHAR(11) UNIQUE NOT NULL,
    categoria_cnh categoria_cnh_motorista_enum NOT NULL,
    validade_cnh DATE NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE veiculo (
    id_veiculo SERIAL PRIMARY KEY,
    placa CHAR(7) UNIQUE NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    ano_fabricacao INT NOT NULL,
    ano_modelo INT NOT NULL,
    cor VARCHAR(30) NOT NULL,
    tipo_combustivel tipo_combustivel_enum NOT NULL,
    renavam CHAR(11) UNIQUE NOT NULL,
    chassi CHAR(17) UNIQUE,
    numero_motor VARCHAR(30),
    km_atual INT NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    categoria_cnh_exigida categoria_cnh_veiculo_enum NOT NULL
);

CREATE TABLE oficina (
    id_oficina SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cnpj CHAR(14) UNIQUE NOT NULL,
    cep CHAR(8) NOT NULL,
    logradouro VARCHAR(150) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    complemento VARCHAR(100),
    bairro VARCHAR(80) NOT NULL,
    cidade VARCHAR(80) NOT NULL,
    uf CHAR(2) NOT NULL,
    telefone VARCHAR(15)
);

CREATE TABLE registro_uso (
    id_uso SERIAL PRIMARY KEY,
    id_veiculo INT NOT NULL REFERENCES veiculo(id_veiculo),
    id_motorista INT NOT NULL REFERENCES motorista(id_motorista),
    data_hora_saida TIMESTAMP NOT NULL,
    km_inicial INT NOT NULL,
    finalidade VARCHAR(150) NOT NULL,
    data_hora_retorno TIMESTAMP,
    km_final INT,
    observacoes TEXT
);

CREATE TABLE abastecimento (
    id_abastecimento SERIAL PRIMARY KEY,
    id_veiculo INT NOT NULL REFERENCES veiculo(id_veiculo),
    id_motorista INT NOT NULL REFERENCES motorista(id_motorista),
    data_abastecimento DATE NOT NULL,
    km_hodometro INT NOT NULL,
    litros DECIMAL(8,2) NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    foto_cupom VARCHAR(255),
    nome_posto VARCHAR(100) NOT NULL,
    tipo_combustivel tipo_combustivel_enum NOT NULL,
    codigo_transacao VARCHAR(50) UNIQUE
);

CREATE TABLE manutencao (
    id_manutencao SERIAL PRIMARY KEY,
    id_veiculo INT NOT NULL REFERENCES veiculo(id_veiculo),
    id_oficina INT NOT NULL REFERENCES oficina(id_oficina),
    data DATE NOT NULL,
    km_hodometro INT NOT NULL,
    tipo_servico tipo_servico_enum NOT NULL,
    descricao TEXT,
    valor_total DECIMAL(10,2),
    numero_os VARCHAR(50) UNIQUE
);

CREATE TABLE avaria (
    id_avaria SERIAL PRIMARY KEY,
    id_uso INT NOT NULL REFERENCES registro_uso(id_uso),
    data_registro TIMESTAMP NOT NULL,
    descricao TEXT NOT NULL,
    gravidade gravidade_avaria_enum NOT NULL,
    resolvida BOOLEAN NOT NULL DEFAULT FALSE,
    foto VARCHAR(255)
);