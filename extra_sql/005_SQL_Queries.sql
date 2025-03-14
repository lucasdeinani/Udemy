-- between seleciona um range
select * from users
where 
created_at >= '2020-06-12 17:38:52'
and 
created_at <= '2020-09-04 19:06:55';

select * from users
where 
created_at between '2020-06-12 17:38:52'
and '2020-09-04 19:06:55';

select * from users
where 
created_at between 
'2020-06-12 00:00:00'
and '2020-09-04 23:59:59';

select * from users
where 
created_at between 
'2020-06-12 00:00:00'
and '2020-09-04 23:59:59'
and id between 163 and 210;

-- in seleciona elementros entre os valores enviados
select * from users
where 
id in (110, 115, 120, 125, 130, 1000, 12200, 12122545);

select * from users
where 
id in (110, 115, 120, 125, 130, 1000, 12200, 12122545)
and first_name in ('Luiz', 'Keelie');