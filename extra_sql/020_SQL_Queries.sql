SELECT u.first_name FROM users u
WHERE u.first_name = 'Katelyn';

-- INNER JOIN = JOIN
SELECT u.first_name, p.bio FROM users u
JOIN profiles p 
ON p.user_id = u.id 
WHERE u.first_name = 'Katelyn';

-- INNER JOIN = JOIN
-- Atualiza registros com joins
-- SELECT u.first_name, p.bio FROM users u
UPDATE users AS u
JOIN profiles AS p 
ON p.user_id = u.id 
SET p.bio = CONCAT(p.bio, ' atualizado')
WHERE u.first_name = 'Katelyn';

-- INNER JOIN = JOIN
SELECT u.first_name, p.bio FROM users u
-- UPDATE users AS u
JOIN profiles AS p 
ON p.user_id = u.id 
-- SET p.bio = CONCAT(p.bio, ' atualizado')
WHERE u.first_name = 'Katelyn';