-- like (parecido)
-- % qualquer coisa
-- _ um caractere 
select * from users
where first_name like '%a';

select * from users
where first_name like '%o';

select * from users
where first_name like 'h%';

select * from users
where first_name like 'he%';

select * from users
where first_name like 'he%a';

select * from users
where first_name like '%mo%';

select * from users
where first_name like '%a%b%';

select * from users
where first_name like 'j_cob';

select * from users
where first_name like 'j_co_';

select * from users
where first_name like '__co_';

select * from users
where first_name like '___o_';

select * from users
where first_name like '_____';

select * from users
where first_name like '%ma%_';