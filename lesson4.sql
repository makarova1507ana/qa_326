
-- CREATE SCHEMA IF NOT EXISTS `book_shop` DEFAULT CHARACTER SET utf8 ;
-- USE `book_shop` ;


-- CREATE TABLE IF NOT EXISTS `autors` (
--   `id` INT NOT NULL AUTO_INCREMENT,
--   `name_autor` VARCHAR(45) NULL,
--   PRIMARY KEY (`id`));


-- CREATE TABLE IF NOT EXISTS `books` (
--   `id` INT NOT NULL AUTO_INCREMENT,
--   `name_book` VARCHAR(45) NULL,
--   PRIMARY KEY (`id`));


-- CREATE TABLE IF NOT EXISTS `autors_books` (
--   `autors_id` INT NOT NULL,
--   `books_id` INT NOT NULL,
--     FOREIGN KEY (`autors_id`)
--     REFERENCES `autors` (`id`),

--     FOREIGN KEY (`books_id`)
--     REFERENCES `books` (`id`)
--  );









-- -- INSERT INTO autors(name_autor) VALUES('York Roger');
-- -- INSERT INTO autors(name_autor) VALUES('Parker Nicholas');
-- -- INSERT INTO autors(name_autor) VALUES('White Hank');
-- -- INSERT INTO autors(name_autor) VALUES('Welsch Barry');
-- -- INSERT INTO autors(name_autor) VALUES('Quinn Makena');
-- -- INSERT INTO autors(name_autor) VALUES('Wade Michael');
-- -- INSERT INTO autors(name_autor) VALUES('Gray Nicholas');
-- -- INSERT INTO autors(name_autor) VALUES('Dowson Anthony');
-- -- INSERT INTO autors(name_autor) VALUES('Wright Emma');
-- -- INSERT INTO autors(name_autor) VALUES('Kaur Hadley');



-- -- INSERT INTO books(name_book) VALUES('Physical Education');
-- -- INSERT INTO books(name_book) VALUES('Language Arts');
-- -- INSERT INTO books(name_book) VALUES('Modern Literature');
-- -- INSERT INTO books(name_book) VALUES('Sociology');
-- -- INSERT INTO books(name_book) VALUES('Instrumental Music');
-- -- INSERT INTO books(name_book) VALUES('Language Arts');
-- -- INSERT INTO books(name_book) VALUES('Language Arts');
-- -- INSERT INTO books(name_book) VALUES('Spanish');
-- -- INSERT INTO books(name_book) VALUES('Science');
-- -- INSERT INTO books(name_book) VALUES('Spanish');



-- -- INSERT INTO autors_books VALUES 
-- -- (1, 1),
-- -- (1, 2),
-- -- (1, 3);

-- -- select * from books;
-- -- select* from autors;
-- -- select* from autors_books;


-- -- INSERT INTO autors_books VALUES 
-- -- (2, 1),
-- -- (2, 4),
-- -- (3, 1),
-- -- (3, 3),
-- -- (4, 5),
-- -- (5, 6),
-- -- (6, 7),
-- -- (7, 8),
-- -- (8, 9);

-- select name_autor, name_book from autors_books, autors, books  -- можно добавить в select books_id, books.id
-- where 
-- autors.id = autors_books.autors_id 
-- and  
-- books.id = autors_books.books_id;



-- -- Показать автора York Roger, его книги 

-- select name_autor, name_book from autors_books, autors, books
-- where 
-- autors.id = autors_books.autors_id 
-- and  books.id = autors_books.books_id
-- and  name_autor = "York Roger";


-- -- показать книгу Physical Education и ее авторов

-- select name_autor, name_book from autors_books, autors, books
-- where 
-- autors.id = autors_books.autors_id 
-- and  books.id = autors_books.books_id
-- and  name_book = "Physical Education";


-- -- показать книгу Physical Education или книгу Modern Literature и ее авторов

-- select name_autor, name_book from autors_books, autors, books
-- where 
-- autors.id = autors_books.autors_id 
-- and  books.id = autors_books.books_id
-- and  (name_book = "Physical Education" or name_book = "Modern Literature");




create database if not exists best_aero;


use best_aero;
create table if not exists passengers (
	id INT PRIMARY KEY auto_increment,
    name_passenger VARCHAR(30) );
    

create table if not exists companies(
	company_name varchar (255),
    id int primary key AUTO_INCREMENT
);


-- INSERT INTO companies(id, company_name) VALUES('1','Facebook');
-- INSERT INTO companies(id, company_name)  VALUES('2','Areon Impex');
-- INSERT INTO companies(id, company_name)  VALUES('3','Team Guard SRL');
-- INSERT INTO companies(id, company_name) VALUES('4','ExxonMobil');
-- INSERT INTO companies(id, company_name)  VALUES('5','Carrefour');
-- INSERT INTO companies (id, company_name)  VALUES('6','Biolife Grup');
-- INSERT INTO companies(id, company_name)  VALUES('7','Demaco');
-- INSERT INTO companies(id, company_name)VALUES('8','ENEL');
-- INSERT INTO companies(id, company_name) VALUES('9','Amazon.com');
-- INSERT INTO companies(id, company_name) VALUES('10','Comodo');


-- INSERT INTO passengers VALUES('1','Norris Monica');
-- INSERT INTO passengers VALUES('2','Hill Alex');
-- INSERT INTO passengers VALUES('3','Roscoe Liv');
-- INSERT INTO passengers VALUES('4','Vollans Angelica');
-- INSERT INTO passengers VALUES('5','Howard Abbey');
-- INSERT INTO passengers VALUES('6','Hall Elly');
-- INSERT INTO passengers VALUES('7','Notman Isla');
-- INSERT INTO passengers VALUES('8','Snow Monica');
-- INSERT INTO passengers VALUES('9','Exton Allison');
-- INSERT INTO passengers VALUES('10','Slater Ryan');

create table if not exists trips(
    plane varchar(255),
    town_from varchar (255),
    town_to varchar (255),
    time_out datetime,
    time_in datetime,
    id int primary key AUTO_INCREMENT,
    company int,
    foreign key (company) REFERENCES companies(id)
    );

-- INSERT INTO trips(id,plane,company,town_from,town_to, time_out, time_in) VALUES('1','Audi V8','3','Innsbruck','Berlin','2035-03-23 14:05:28','4638-07-29 01:29:38');
-- INSERT INTO trips(id,plane,company,town_from,town_to, time_out, time_in) VALUES('2','Mazda 6','4','Sacramento','Las Vegas','8170-07-08 11:38:12','8169-08-02 13:04:00');
-- INSERT INTO trips(id,plane,company,town_from,town_to, time_out, time_in) VALUES('3','BMW M6','3','Milano','San Francisco','5055-09-28 12:47:38','4599-04-04 11:26:05');
-- INSERT INTO trips(id,plane,company,town_from,town_to, time_out, time_in) VALUES('4','Kia Sorento','4','Houston','San Francisco','6733-09-07 03:03:22','6518-08-04 17:46:58');
-- INSERT INTO trips(id,plane,company,town_from,town_to, time_out, time_in) VALUES('5','Mazda 6','5','Minneapolis','Tulsa','4419-03-19 15:11:18','0397-09-18 13:29:24');
-- INSERT INTO trips(id,plane,company,town_from,town_to, time_out, time_in) VALUES('6','Kia Soul','6','Lisbon','Springfield','6651-06-25 02:31:40','8045-08-19 13:01:12');
-- INSERT INTO trips(id,plane,company,town_from,town_to, time_out, time_in) VALUES('7','Audi V8','7','Lakewood','Boston','4542-01-01 18:29:08','4397-01-15 21:20:13');
-- INSERT INTO trips(id,plane,company,town_from,town_to, time_out, time_in) VALUES('8','Audi A4','8','Prague','Lyon','9618-03-31 02:06:27','1531-07-30 10:51:35');
-- INSERT INTO trips (id,plane,company,town_from,town_to, time_out, time_in) VALUES('9','BMW M3','9','Henderson','Minneapolis','2464-05-15 11:56:50','9678-10-08 21:10:56');
-- INSERT INTO trips(id,plane,company,town_from,town_to, time_out, time_in) VALUES('10','Hyundai Tucson','10','Pittsburgh','Irving','2321-08-15 05:21:47','9027-04-21 03:33:04');


    
create table if not exists Pass_in_trip(
	id INT PRIMARY KEY auto_increment,
	trip INT,
     FOREIGN KEY (trip) REFERENCES trips (id),
    passenger INT,
     FOREIGN KEY (passenger) REFERENCES passengers (id),
     place VARCHAR(3));
     
-- insert into Pass_in_trip(trip, passenger, place) VALUES
-- (1, 1, "A23"),
-- (1, 2, "A22"),
-- (1, 3, "B24"),
-- (1, 4, "B25"),
-- (2, 1, "B23"),
-- (2, 5, "B24"),
-- (2, 6, "B02"),
-- (3, 2, "A23"),
-- (4, 7, "C07");

select * from companies;
select * from trips;
select * from passengers;
select * from Pass_in_trip;

-- посмотреть рейсы для первого пассажира
-- select name_passenger, plane, place from Pass_in_trip, passengers, trips
-- where Pass_in_trip.passenger = passengers.id
-- and Pass_in_trip.trip = trips.id
-- and passengers.id = 1;

-- Вывести имена всех людей, которые есть в базе данных авиакомпаний
-- select * from Pass_in_trip, passengers, trips, companies
-- where Pass_in_trip.passenger = passengers.id
-- and Pass_in_trip.trip = trips.id
-- and trips.company = companies.id;


-- Вывести все рейсы  и их пассажиров, совершенные из Innsbruck

select * from Pass_in_trip, passengers, trips
where Pass_in_trip.passenger = passengers.id
and Pass_in_trip.trip = trips.id
and trips.town_from = "Innsbruck";


