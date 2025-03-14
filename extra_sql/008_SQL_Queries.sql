-- limit limita a qtd de valores
-- offset desloca o cursor para exibir os resultados
select id, first_name, email as uemail
from users
where id between 100 and 150
order by first_name desc
limit 2;

-- offset ponteiro/cursor pegar apartir do registro dentro do array
select id, first_name, email as uemail
from users
where id between 100 and 150
order by first_name desc
limit 2 offset 0;

-- Primeiro o offset / depois o limit
select id, first_name, email as uemail
from users
where id between 100 and 150
order by first_name desc
limit 6,3;