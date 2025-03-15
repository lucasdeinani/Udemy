SELECT u.id as uid, p.id as pid,
p.bio, u.first_name
FROM users as u, profiles as p
WHERE u.id = p.user_id;

-- Seleciona users.id, profiles.id, profiles.bio
-- profiles.description, users.first_name
-- da tabela users
-- unindo com a tabela profiles
-- quando a condição u.id = p.user_id for satisfeita
-- onde users.first_name terminar com "a"
-- ordena por users.first_name decrescente
-- limita 5 registros

SELECT u.id as uid, p.id as pid,
p.bio, u.first_name
FROM users as u
INNER JOIN profiles p
ON u.id = p.user_id;

SELECT u.id as uid, p.id as pid,
p.bio, u.first_name
FROM users as u
INNER JOIN profiles p
ON u.id = p.user_id
WHERE u.first_name LIKE '%a'
ORDER BY u.first_name DESC
LIMIT 5;

-- Seleciona users.id, profiles.id, profiles.bio
-- profiles.description, users.first_name
-- da tabela users (todos os registros da tabela da esquerda)
-- unindo com a tabela profiles (tabela da direita é opcional)
-- quando a condição u.id = p.user_id for satisfeita
-- onde users.first_name terminar com "a"
-- ordena por users.first_name decrescente
-- limita 5 registros
SELECT u.id as uid, p.id as pid,
p.bio, u.first_name
FROM users as u
LEFT JOIN profiles p
ON u.id = p.user_id;

-- Seleciona users.id, profiles.id, profiles.bio
-- profiles.description, users.first_name
-- da tabela users (tabela da esquerda é opcional)
-- unindo com a tabela profiles (todos os registros da tabela da direita)
-- quando a condição u.id = p.user_id for satisfeita
-- onde users.first_name terminar com "a"
-- ordena por users.first_name decrescente
-- limita 5 registros
SELECT u.id as uid, p.id as pid,
p.bio, u.first_name
FROM users as u
RIGHT JOIN profiles p
ON u.id = p.user_id;