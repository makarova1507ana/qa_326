

Create database if not exists university;

use university;
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

    FOREIGN KEY(group_id) REFERENCES groups_students(groups_id)
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
	FOREIGN KEY(course) REFERENCES courses(course_id),
    FOREIGN KEY(group_id) REFERENCES groups_students(groups_id)
);

-- Добавление записей в таблицу "Schedule"
INSERT INTO Schedule (day_of_week, time, course_id, group_id) VALUES
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


-- Выбрать студентов и их курсы:
-- Получить информацию о преподавателях и курсах, веденных ими:
-- Получить список всех групп и соответствующих преподавателей:
-- Получить информацию о студентах, их группах и дате их занятий:
-- Получить информацию о студентах, их курсах и дате их занятий:
-- Получить все уникальные курсы, в которых зарегистрированы студенты:
-- Получить список всех курсов и соответствующих преподавателей, включая информацию о студентах, изучающих эти курсы:



--  примеры с UNION 





