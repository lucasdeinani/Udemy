-- where filtra registros
-- operadores de comparação = < <= > >= <> !=
-- operadores logicos and e or
select * from users;

select * from users
where id = 110;

select * from users
where first_name = 'Luiz';

select * from users
where id > 100;

select * from users
where id >= 100;

select * from users
where created_at < '2020-12-15 23:33:41';

select * from users
where 
created_at < '2020-12-15 23:33:41'
and first_name = 'Luiz';

select * from users
where 
created_at < '2020-12-15 23:33:41'
or first_name = 'Luiz';

select * from users
where 
created_at < '2020-12-15 23:33:41'
and first_name = 'Luiz' and password_hash = 'a_hash';