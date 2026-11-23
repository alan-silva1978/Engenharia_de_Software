# Sistema de Gestão de Frotas — Tinta Certa (`tinta_certa_frota`)

## Descrição do Minimundo
O projeto **Tinta Certa Frota** é um banco de dados relacional desenvolvido em **PostgreSQL** para o controle operacional e financeiro da frota de veículos de uma loja de tintas. O sistema centraliza o cadastro de veículos, motoristas, usuários gestores e oficinas parceiras, permitindo o rastreamento completo de saídas e retornos (rotas), abastecimentos, manutenções preventivas/corretivas e registro de avarias. Uma das perguntas centrais que o banco responde é: quem estava com cada veículo em determinada data e hora (por exemplo, para identificar o condutor no caso de uma multa).

## Estrutura do Modelo Implementado
O banco de dados foi modelado respeitando a integridade referencial (`PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE` e `NOT NULL`), a 1ª Forma Normal (endereços fracionados) e a padronização de domínios por meio de tipos `ENUM`. Valores em dinheiro e litros usam `DECIMAL`, para evitar erros de arredondamento.

### Tipos ENUM Personalizados
* `perfil_usuario`: `'GESTOR'`, `'MOTORISTA'`
* `tipo_combustivel_enum`: `'GASOLINA'`, `'ETANOL'`, `'FLEX'`, `'DIESEL'`, `'GNV'`, `'ELETRICO'`, `'HIBRIDO'`
* `tipo_servico_enum`: `'PREVENTIVA'`, `'CORRETIVA'`
* `gravidade_avaria_enum`: `'LEVE'`, `'MEDIA'`, `'GRAVE'`
* `categoria_cnh_motorista_enum`: `'ACC'`, `'A'`, `'B'`, `'C'`, `'D'`, `'E'`, `'AB'`, `'AC'`, `'AD'`, `'AE'`
* `categoria_cnh_veiculo_enum`: `'ACC'`, `'A'`, `'B'`, `'C'`, `'D'`, `'E'`

### Tabelas (8 Entidades)
1. **`usuario`**: Credenciais e perfis de acesso ao sistema.
2. **`motorista`**: Cadastro de condutores, CNH e vínculo opcional (`1:1`) com `usuario`.
3. **`veiculo`**: Cadastro técnico da frota, hodômetro atual e categoria de CNH exigida.
4. **`oficina`**: Prestadores de serviço com CNPJ único e endereço fracionado.
5. **`registro_uso`**: Histórico de saídas, finalidade da rota e quilometragem percorrida.
6. **`abastecimento`**: Controle de litros, valores, postos e `codigo_transacao` único.
7. **`manutencao`**: Ordens de serviço (`numero_os`), custos e histórico por oficina.
8. **`avaria`**: Ocorrências vinculadas a um `registro_uso`, com nível de gravidade e status de resolução.

## Pré-requisitos e Configuração do Ambiente
* **SGBD:** PostgreSQL (versão 15 ou superior; testado na versão 19).
* **Ferramenta de Gestão:** pgAdmin 4 (ou cliente SQL compatível).

### Configuração Inicial
1. Abra o **pgAdmin 4** e conecte-se ao seu servidor PostgreSQL local.
2. Clique com o botão direito em **Databases** > **Create** > **Database...**.
3. Nomeie o banco como **`tinta_certa_frota`** e clique em **Save**.
4. Clique com o botão direito sobre o banco criado e selecione **Query Tool** para executar os scripts abaixo.

## Ordem de Execução dos Scripts
Para respeitar as dependências entre chaves primárias e estrangeiras, execute os arquivos na seguinte sequência exata:

1. **`01_ddl_estrutura.sql`** *(DDL — Criação)*: Cria os 6 tipos `ENUM` e as 8 tabelas na ordem correta de dependência.
2. **`02_dml_povoamento.sql`** *(DML — Carga Inicial)*: Insere os dados de teste nas entidades independentes primeiro (`usuario`, `veiculo`, `oficina`) e nas dependentes em seguida. Inclui de propósito um abastecimento duplicado e uma oficina sem serviços, usados no teste de exclusão.
3. **`03_dql_consultas.sql`** *(DQL — Consultas Relacionais)*: Executa 5 consultas utilizando `INNER JOIN`, `LEFT JOIN`, `WHERE`, `ORDER BY` e `LIMIT` para validar os relacionamentos, incluindo a identificação do condutor por data e hora. *(Recomendado executar uma consulta por vez selecionando o bloco e pressionando `F5`)*.
4. **`04_dml_update_delete.sql`** *(DML — Manutenção)*: Aplica atualizações condicionais (`UPDATE ... WHERE`) para encerrar a rota em aberto, atualizar o hodômetro e registrar a resolução de uma avaria, e realiza exclusões seguras (`DELETE ... WHERE`) de um lançamento duplicado, de um orçamento recusado e de uma oficina sem vínculos, sem violar a integridade referencial.

> **Importante:** veículos e motoristas com histórico não devem ser excluídos. Para retirá-los de operação, use `UPDATE ... SET ativo = FALSE`.

## Evoluções Previstas
* Plano de manutenção preventiva por veículo (troca de óleo, pneus, correia dentada), com intervalos por quilometragem ou tempo.
* Regras de verificação (`CHECK`), como `km_final >= km_inicial` e valores maiores que zero.

## Tecnologias Utilizadas
* brModelo (modelos conceitual e lógico)
* PostgreSQL 19 & pgAdmin 4
* Visual Studio Code (edição dos scripts)
* Git & GitHub (armazenamento e histórico dos arquivos)
