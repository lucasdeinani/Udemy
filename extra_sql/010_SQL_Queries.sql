-- Delete apaga registros da tabela
DELETE FROM users WHERE id = 114;

-- Aviso: use SELECT para garantir que está
-- apagando os valores corretos
SELECT * FROM users WHERE id BETWEEN 110 AND 115;