-- FUNCIONÁRIOS
INSERT INTO funcionario_funcionario (
    nome, funcao, salario, banco, contato, cpf, data_admissao,
    frequencia_pagamento, status, tipo_chave_pix, chave_pix
)
VALUES
('João Silva', 'Operador de Máquina', 2500.00, 'Banco do Brasil', '11999998888', '123.456.789-00', '2022-01-10', 'Mensal', 'Ativo', 'CPF', '123.456.789-00'),
('Maria Souza', 'Auxiliar', 1800.00, 'Caixa', '11988887777', '987.654.321-00', '2021-03-05', 'Semanal', 'Férias', 'EMAIL', 'maria@example.com'),
('Carlos Pereira', 'Supervisor', 3500.00, 'Itaú', '11977776666', '111.222.333-44', '2020-07-10', 'Mensal', 'Ativo', 'TELEFONE', '11977776666'),
('Ana Lima', 'Técnica', 2900.00, 'Nubank', '11955554444', '333.222.111-55', '2023-02-15', 'Quinzenal', 'Inativo', 'CHAVE_ALEATORIA', 'abcd-1234-xyz'),
('Lucas Andrade', 'Auxiliar', 2200.00, 'Bradesco', '11944443333', '555.666.777-88', '2022-08-22', 'Mensal', 'Ativo', 'EMAIL', 'lucas@empresa.com');

-- PRODUTOS
INSERT INTO produto_produto (nome, preco_unitario, largura, altura, comprimento)
VALUES
('Tijolo Baiano', 0.80, 39.0, 14.0, 19.0),
('Tijolo Maciço', 0.60, 19.0, 9.0, 5.0),
('Tijolo 6 Furos', 0.75, 23.0, 11.5, 5.5),
('Tijolo 8 Furos', 0.85, 29.0, 14.0, 9.0),
('Tijolo de Vedação', 0.70, 30.0, 14.0, 9.0);

-- PRODUÇÃO
INSERT INTO producao_producao (data, quantidade_produzida, produto_id)
VALUES
('2025-08-01', 10, 1),
('2025-08-02', 5, 2),
('2025-08-03', 3, 3),
('2025-08-04', 4, 4),
('2025-08-05', 7, 5);

-- PAGAMENTOS
INSERT INTO pagamento_pagamento (funcionario_id, data_pagamento, vale_desconto, bonus_comissao, pago)
VALUES
(1, '2025-08-01', 200.00, 150.00, 1),
(2, '2025-08-01', 100.00, 75.00, 1),
(3, '2025-08-01', 300.00, 250.00, 0),
(4, '2025-08-01', 150.00, 100.00, 1),
(5, '2025-08-01', 180.00, 120.00, 1);

-- MATERIAIS
INSERT INTO material_material (nome, certificado_aprovacao, dias_de_emprestimo, fabricante, quantidade)
VALUES
('Capacete de Segurança', 123456, 30, '3M', 10),
('Luvas de Proteção', 654321, 15, 'Delta Plus', 25),
('Botina de Couro', 789123, 20, 'Bracol', 15),
('Óculos de Proteção', 321654, 10, '3M', 30),
('Colete Refletivo', 456987, 25, 'NobreSeg', 20);

-- EMPRÉSTIMOS
INSERT INTO emprestimo_emprestimo (material_id, funcionario_id, data_emprestimo, data_devolucao, status)
VALUES
(1, 1, '2025-07-01', '2025-07-30', 'devolvido'),
(2, 2, '2025-08-01', NULL, 'ativo'),
(3, 3, '2025-08-02', NULL, 'pendente'),
(4, 4, '2025-07-15', '2025-07-25', 'devolvido'),
(5, 5, '2025-08-03', NULL, 'ativo');