-- Update - Atualiza registros
UPDATE users SET 
first_name = 'Luiz',
last_name = 'Miranda'
WHERE id = 119;

SELECT * FROM users WHERE id = 119;

UPDATE users SET 
first_name = 'Luiz',
last_name = 'Miranda'
WHERE id BETWEEN 119 AND 121;

SELECT * FROM users WHERE id BETWEEN 119 AND 121;