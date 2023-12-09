CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    description TEXT,
    category_id INT,
    countp INT DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE customers (
    id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE order_details (
    id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Добавление записей в таблицу "categories"
INSERT INTO categories (id, name) VALUES
    (1, 'Электроника'),
    (2, 'Компьютеры'),
    (3, 'Аудио'),
    (4, 'Фото и видео'),
    (5, 'Аксессуары');
-- Добавление записей в таблицу "products"
INSERT INTO products (id, name, price, description, category_id, countp) VALUES
    (1, 'Смартфон', 59999.99, 'Высококачественный смартфон с передовыми функциями', 1, 100),
    (2, 'Ноутбук', 129999.99, 'Мощный ноутбук для профессионального использования', 2, 57),
    (3, 'Наушники', 14999.99, 'Шумоподавляющие беспроводные наушники', 3, 568),
    (4, 'Умные часы', 24999.99, 'Фитнес-трекер и умные часы', 1, 22222),
    (5, 'Фотоаппарат', 79999.99, 'Профессиональный зеркальный фотоаппарат с несколькими объективами', 4, 3213),
    (6, 'Планшет', 49999.99, 'Портативный планшет для развлечений и работы', 2, 3123),
    (7, 'Колонка', 19999.99, 'Беспроводная колонка высокого качества', 3, 89),
    (8, 'Монитор', 39999.99, 'Монитор с высоким разрешением', 4, 1),
    (9, 'Принтер', 29999.99, 'Многофункциональный принтер для домашнего офиса', 5, 31212),
    (10, 'Роутер', 12999.99, 'Высокоскоростной беспроводной роутер для домашней сети', 5, 31792);


-- Добавление записей в таблицу "customers"
INSERT INTO customers (id, first_name, last_name, email) VALUES
    (1, 'Иван', 'Иванов', 'ivan@example.com'),
    (2, 'Анна', 'Петрова', 'anna@example.com'),
    (3, 'Сергей', 'Сидоров', 'sergei@example.com'),
    (4, 'Елена', 'Козлова', 'elena@example.com'),
    (5, 'Дмитрий', 'Васильев', 'dmitriy@example.com');

-- Добавление записей в таблицу "orders"
INSERT INTO orders (id, order_date, customer_id) VALUES
    (1, '2023-01-01', 1),
    (2, '2023-01-02', 2),
    (3, '2023-01-03', 3),
    (4, '2023-01-04', 4),
    (5, '2023-01-05', 5),
    (6, '2023-01-06', 1),
    (7, '2023-01-07', 2),
    (8, '2023-01-08', 3),
    (9, '2023-01-09', 4),
    (10, '2023-01-10', 5);



-- Добавление записей в таблицу "order_details"
INSERT INTO order_details (id, order_id, product_id, quantity, price) VALUES
    (1, 1, 1, 2, 119999.98),
    (2, 2, 3, 1, 14999.99),
    (3, 3, 5, 1, 79999.99),
    (4, 4, 2, 1, 129999.99),
    (5, 5, 4, 1, 24999.99),
    (6, 6, 6, 1, 49999.99),
    (7, 7, 7, 1, 19999.99),
    (8, 8, 8, 1, 39999.99),
    (9, 9, 9, 1, 29999.99),
    (10, 10, 10, 1333333.11);
