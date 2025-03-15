-- Apaga registros com joins
-- INNER JOIN = JOIN
SELECT u.first_name, p.bio FROM users u
JOIN profiles p 
ON p.user_id = u.id 
WHERE u.first_name = 'Katelyn';

-- Assim apaga tudo
DELETE FROM users u
JOIN profiles p 
ON p.user_id = u.id 
WHERE u.first_name = 'Katelyn';

-- Assim apaga só da profiles
DELETE p FROM users u
JOIN profiles p 
ON p.user_id = u.id 
WHERE u.first_name = 'Katelyn';

SELECT u.first_name, p.bio FROM users u
LEFT JOIN profiles p 
ON p.user_id = u.id 
WHERE u.first_name = 'Katelyn';

-- Assim apaga só da profiles e users
DELETE p, u FROM users u
LEFT JOIN profiles p 
ON p.user_id = u.id 
WHERE u.first_name = 'Katelyn';
