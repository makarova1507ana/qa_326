-- use shop;
/*CREATE TABLE salespeople(
  id INT(11) NOT NULL PRIMARY KEY,
  sname VARCHAR(45) NOT NULL,
  city VARCHAR(45) NOT NULL,
  comm FLOAT NOT NULL
); 



CREATE TABLE customers(
  id INT(11) NOT NULL PRIMARY KEY,
  cname VARCHAR(45) NOT NULL,
  city VARCHAR(45) NOT NULL,
  rating FLOAT NOT NULL,
  id_salesPeople INT(11) NOT NULL,
  FOREIGN KEY (id_salesPeople) REFERENCES salespeople(id)
);


CREATE TABLE orders(
  id INT(11) NOT NULL PRIMARY KEY,
  amt DOUBLE NOT NULL,
  odate date NOT NULL,
  id_customer INT(11) NOT NULL,
  id_salesPeople INT(11) NOT NULL,
  FOREIGN KEY (id_customer) REFERENCES customers(id),
  FOREIGN KEY (id_salesPeople) REFERENCES salespeople(id)
);

INSERT INTO salespeople (id, sname, city, comm) VALUES
(1, "Колованов", "Москва", 10),
(2, "Петров", "Тверь", 25),
(3, "Плотников", "Москва", 22),
(4, "Кучеров", "Санкт-Петербург", 28),
(5, "Малкин", "Санкт-Петербург", 18),
(6, "Шипачев", "Челябинск", 30),
(7, "Мозякин", "Одинцово", 25),
(8, "Проворов", "Москва", 25);

INSERT INTO customers (id, cname, city, rating, id_salesPeople) VALUES
(1, "Деснов", "Москва", 90, 6),
(2, "Краснов", "Москва", 95, 7),
(3, "Кириллов", "Тверь", 96, 3),
(4, "Ермолаев", "Обнинск", 98, 3),
(5, "Колесников", "Серпухов", 98, 5),
(6, "Пушкин", "Челябинск", 90, 4),
(7, "Лермонтов", "Одинцово", 85, 1),
(8, "Белый", "Москва", 89, 3),
(9, "Чудинов", "Москва", 96, 2),
(10, "Лосев", "Одинцово", 93, 8);


INSERT INTO orders (id, amt, odate, id_customer, id_salesPeople) VALUES
(1001, 128, '2016-01-01', 9, 4),
(1002, 1800, '2016-04-10', 10, 7),
(1003, 348, '2017-04-08', 2, 1),
(1004, 500, '2016-06-07', 3, 3),
(1005, 499, '2017-12-04', 5, 4),
(1006, 320, '2016-03-03', 5, 4),
(1007, 80, '2017-09-02', 7, 1),
(1008, 780, '2016-03-07', 1, 3),
(1009, 560, '2017-10-07', 3, 7),
(1010, 900, '2016-01-08', 6, 8);

select * from customers;*/

-- ------------------------ соединения таблиц --------------------------
-- -- показать покупателей и их заказы
-- -- select * from customers, orders where orders.id_customer = customers.id;
-- -- вместо такого запроса используют JOIN
-- select * from orders
-- JOIN customers 					# INNER JOIN == JOIN
-- ON id_customer = customers.id; # FK = PK
/*select * from customers;


-- -- показать всех покупателей, в том числе и котороых нет заказов
-- select * from orders
-- Right JOIN customers 					
-- ON id_customer = customers.id; # FK = PK

-- INSERT INTO salespeople (id, sname, city, comm) VALUES
 -- (10, "Колованова", "Алтайск", 10);


-- -- показать всех продавцов и их покупаетелей, в том числе и продавцов у которых нет  покупателей(которые не привязаны)
--  -- ничего не покажет так как у всех покупателей заполнен id_salespeople
-- -- select * from customers, salespeople where id_salespeople = salespeople.id and id_salespeople is NULL;

select * from customers
RIGHT JOIN salespeople 	#  в том и которых нет привязки				
ON id_salesPeople = salespeople.id 
where id_salesPeople is NUll; # FK = PK


-- --------------------------------FULL OUTER JOIN -> UNION ----------------------------------------------------
select * from customers
LEFT JOIN salespeople 	#  в том и которых нет привязки				
ON id_salesPeople = salespeople.id 
UNION 
select * from customers
RIGHT JOIN salespeople 
ON id_salesPeople = salespeople.id;
*/


Create database if not exists university;

use university;/*
-- Создание таблицы "Professors"
CREATE TABLE Professors (
    professor_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    department VARCHAR(100)
);

-- Добавление записей в таблицу "Professors"
INSERT INTO Professors (first_name, last_name, email, department) VALUES
    ('Иван', 'Петров', 'ivan_petrov@example.com', 'Информатика'),
    ('Елена', 'Сидорова', 'elena_sidorova@example.com', 'Математика'),
    ('Алексей', 'Иванов', 'alex_ivanov@example.com', 'Физика'),
    ('Ольга', 'Смирнова', 'olga_smirnova@example.com', 'Иностранные языки');
    


-- Создание таблицы "groups_students"
CREATE TABLE if not exists groups_students (
    group_id INT PRIMARY KEY AUTO_INCREMENT,
    group_name VARCHAR(100),
    professor_id INT,
	FOREIGN KEY(professor_id) REFERENCES Professors(professor_id)

);

-- Добавление записей в таблицу "Groups"
INSERT INTO groups_students (group_name, professor_id) VALUES
    ('Группа 1', 1),
    ('Группа 2', 2),
    ('Группа 3', 3),
    ('Группа 4', 1),
    ('Группа 5', 2),
    ('Группа 6', 3),
    ('Группа 7', 1),
    ('Группа 8', 2),
    ('Группа 9', 3),
    ('Группа 10', 1);
    

-- Создание таблицы "Courses"
CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    professor_id INT,
	FOREIGN KEY(professor_id) REFERENCES Professors(professor_id)

);

-- Добавление записей в таблицу "Courses"
INSERT INTO Courses (course_name, professor_id) VALUES
    ('Программирование', 1),
    ('Математический анализ', 2),
    ('Физика', 3),
    ('Английский язык', 4),
    ('История', 1),
    ('Литература', 2),
    ('Экономика', 3),
    ('Биология', 4),
    ('Химия', 1),
    ('География', 2);
    
    -- Создание таблицы "Students"
CREATE TABLE if not exists Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    course INT,
    group_id INT,
	FOREIGN KEY(course) REFERENCES courses(course_id),
    FOREIGN KEY(group_id) REFERENCES groups_students(group_id)
);

-- Добавление записей в таблицу "Students"
INSERT INTO Students (first_name, last_name, email, course, group_id) VALUES
    ('Иван', 'Иванов', 'ivan@example.com', 2, 1),
    ('Елена', 'Петрова', 'elena@example.com', 3, 1),
    ('Алексей', 'Сидоров', 'alex@example.com', 2, 2),
    ('Ольга', 'Смирнова', 'olga@example.com', 1, 2),
    ('Дмитрий', 'Козлов', 'dmitriy@example.com', 3, 1),
    ('Татьяна', 'Федорова', 'tanya@example.com', 2, 2),
    ('Павел', 'Морозов', 'pavel@example.com', 1, 1),
    ('Мария', 'Васильева', 'maria@example.com', 3, 2),
    ('Александра', 'Павлова', 'sasha@example.com', 1, 1),
    ('Сергей', 'Кузнецов', 'sergei@example.com', 2, 2);







-- Создание таблицы "Schedule"
CREATE TABLE Schedule (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,
    day_of_week VARCHAR(20),
    time TIME,
    course INT,
    group_id INT,
	FOREIGN KEY(course) REFERENCES courses(course_id),
    FOREIGN KEY(group_id) REFERENCES groups_students(group_id)
);

-- Добавление записей в таблицу "Schedule"
INSERT INTO Schedule (day_of_week, time, course, group_id) VALUES
    ('Понедельник', '09:00:00', 1, 1),
    ('Вторник', '10:30:00', 2, 2),
    ('Среда', '11:45:00', 3, 1),
    ('Четверг', '08:15:00', 4, 2),
    ('Пятница', '13:00:00', 5, 1),
    ('Суббота', '09:30:00', 6, 2),
    ('Воскресенье', '12:00:00', 7, 1),
    ('Понедельник', '14:15:00', 8, 2),
    ('Вторник', '15:45:00', 9, 1),
    ('Среда', '16:30:00', 10, 2);

*/


-- -- Выбрать студентов и их курсы:
-- select * from students 
-- JOIN courses
-- ON courses.course_id = students.course;

-- -- Получить информацию о преподавателях и курсах, веденных ими:
-- select * from courses
-- join professors
-- ON courses.professor_id = professors.professor_id;

-- Получить список всех групп и соответствующих преподавателей:

-- -- Получить информацию о студентах, их группах и дате их занятий:
-- select * from schedule 
-- join groups_students 
-- on groups_students.group_id = schedule.group_id
-- join students 
-- on students.group_id = groups_students.group_id;

-- Получить список всех курсов и соответствующих преподавателей и их расписание
select * from courses
join  professors 
On courses.professor_id = professors.professor_id
join schedule
on schedule.course = courses.course_id;


-- Получить информацию о студентах, их курсах и дате их занятий:
-- Получить все уникальные курсы, в которых зарегистрированы студенты:

-- Получить список всех курсов и соответствующих преподавателей, включая информацию о студентах, изучающих эти курсы:


-- select * from schedule ;


/*
select * from schedule 
join courses 
on courses.course_id = schedule.course;

select day_of_week, time, course_name, group_name from schedule 
join courses 
on courses.course_id = schedule.course
join groups_students 
on groups_students.group_id = schedule.group_id;
*/
--  примеры с UNION 





