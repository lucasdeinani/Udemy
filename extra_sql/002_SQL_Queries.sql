-- Seleciona colunas
select * from users;

select email, id from users u;

select 
email as e, id as i, first_name as fn
from users as u;

select 
email e, id i, first_name "eu posso colocar isso"
from users u;

select 
u.email uemail, u.id uid, u.first_name ufirst_name
from users u;