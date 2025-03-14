-- insert select 
-- insere valores em uma tabela usando outra
select 1;

select 1 as colunas;

select 1 as colunas, 'qualquer coisa' as col2;

insert into profiles
(bio, description, user_id)
select 1, 2, 110;

delete from profiles;

insert into profiles
(bio, description, user_id)
select 'bio', 'description', id from
users;

insert into profiles
(bio, description, user_id)
select concat('Bio de ', first_name), 
concat('Description de', ' ', first_name), id from
users;