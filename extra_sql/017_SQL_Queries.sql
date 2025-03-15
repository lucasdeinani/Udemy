INSERT INTO users_roles (user_id, role_id)
VALUES
(518, 4);

SELECT user_id, role_id FROM users_roles WHERE 
user_id = 518 and role_id = 4;

SELECT user_id, role_id FROM users_roles WHERE 
user_id = 518;

SELECT 
id, 
(SELECT id FROM roles ORDER BY RAND() LIMIT 1) AS qualquer 
FROM users;

INSERT INTO users_roles (user_id, role_id)
SELECT 
id, 
(SELECT id FROM roles ORDER BY RAND() LIMIT 1) AS qualquer 
FROM users;