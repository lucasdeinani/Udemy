SELECT 
max(salary) AS max_salary,
min(salary) AS min_salary,
avg(salary) AS avg_salary,
sum(salary) AS sum_salary,
count(users.salary) AS count_salary
FROM users;

SELECT 
max(salary) AS max_salary,
min(salary) AS min_salary,
avg(salary) AS avg_salary,
sum(salary) AS sum_salary,
count(users.salary) AS count_salary
FROM users
WHERE first_name = 'Carly';

SELECT 
u.first_name,
max(u.salary) AS max_salary,
min(u.salary) AS min_salary,
avg(u.salary) AS avg_salary,
sum(u.salary) AS sum_salary,
count(u.salary) AS count_salary
FROM users u
LEFT JOIN profiles p 
ON p.user_id = u.id
WHERE u.id IN (310, 132, 130, 128)
GROUP BY first_name
LIMIT 5;

SELECT 
u.first_name,
max(u.salary) AS max_salary,
min(u.salary) AS min_salary,
avg(u.salary) AS avg_salary,
sum(u.salary) AS sum_salary,
COUNT(u.id) AS total
FROM users u
LEFT JOIN profiles p 
ON p.user_id = u.id
GROUP BY first_name
ORDER BY total DESC;