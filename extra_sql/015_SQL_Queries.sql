-- Configura um salário aleatório para users
select round(rand() * 10000, 2);

UPDATE users SET salary = round(rand() * 10000, 2);

SELECT salary FROM users WHERE 
salary BETWEEN 1000 AND 1500
ORDER BY salary ASC;