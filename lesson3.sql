use best_shop;
create table if not exists clients(
	name_client varchar (255),
    birthday date,
    id_client int primary key AUTO_INCREMENT
);

create table if not exists orders(
	counts_products bigint,
    cost bigint,
    ID_client int,
    FOREIGN KEY (ID_client) REFERENCES clients(id_client)
);

/*

insert into clients(name_client, birthday)
values ("Ivanov Ivan", "2000-05-11"),
("Ivanov Vasya", "1980-05-11"),
("Ivanova Natasha", "1980-06-21"), 
("Petrova Natasha", "1984-06-11");



insert into orders(counts_products, cost, ID_client)
values (100, 15050, 1),
(10, 2000, 1),
(45, 3200, 2),
(3, 5500, 3),
(1, 3000, 3),
(2, 6400, 3);*/


-- select * from orders;


-- -- найти всех клиентов с именем  Natasha
-- Select name_client from clients 
-- where name_client like "% Natasha";


-- -- найти всех клиентов с фамилией на букву “I”
-- Select name_client from clients 
-- where name_client like "I%";

-- найти всех клиентов с фамилией на букву “I”

-- найти все заказы 
-- select * from orders;



-- -- найти заказы, стоимость которых более 10000
-- select cost from orders where cost > 10000;


-- select * from clients;

-- -- найти  заказы и показать клиентов, сделавших заказ
--  select * from orders, clients
-- where  orders.ID_client = clients.id_client;

-- найти  заказы, стоимость которых более 1000,  но менее 5000 и 
-- показать клиентов, сделавших заказ
-- select * from clients;
-- select * from orders, clients
-- where cost > 1000 and cost < 5000







-- and orders.ID_client = clients.id_client;





-- найти  клиента у которого день рождение в 2000-05-11
-- select * from clients where birthday = "2000-05-11";

-- insert into clients(name_client, birthday)
-- values ("Ivanov Ivan", "2000-11-05

-- найти  клиентов, у которых день рождение в мае
-- select * from clients where birthday like "%-05-%"


-- найти  клиентов, у которых день рождение летом
-- select * from clients where 8 >= month(birthday) and month(birthday) >= 6;



-- найти  клиентов, у которых день рождение 11 числа любого месяца
-- select * from clients where day(birthday) = 11;













-- practika best_aero

use best_aero;
/*
create table if not exists companies(
	company_name varchar (255),
    id int primary key AUTO_INCREMENT
);
create table if not exists trips(
    plane int,
    town_from varchar (255),
    town_to varchar (255),
    time_out datetime,
    time_in datetime,
    id int primary key AUTO_INCREMENT,
    company int,
    foreign key (company) REFERENCES companies(id)
    );
    */
    