CREATE DATABASE IF NOT EXISTS ecommerce;

USE ecommerce;

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL, 
    email VARCHAR(255) UNIQUE NOT NULL,
    registration_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);


CREATE TABLE IF NOT EXISTS categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    ordered_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2) NOT NULL,
    payment_status ENUM('processing', 'paid', 'failed', 'refunded') NOT NULL DEFAULT 'processing',
    FOREIGN KEY (user_id) REFERENCES users(id)
);


CREATE TABLE IF NOT EXISTS order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    order_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (order_id) REFERENCES orders(id) 
);

CREATE TABLE IF NOT EXISTS payments(
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    method ENUM('card', 'upi', 'wallet', 'cod') NOT NULL,
    status ENUM('success', 'failed', 'pending') NOT NULL,
    paid_at DATETIME,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);


CREATE TABLE IF NOT EXISTS deliveries (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    status ENUM('pending', 'shipped', 'in_transit', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
    delivery_address VARCHAR(255) NOT NULL,
    courier_name VARCHAR(100),
    expected_delivery DATETIME,
    delivered_at DATETIME,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);


CREATE TABLE IF NOT EXISTS product_reviews (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    user_id INT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    reviews VARCHAR(300) NOT NULL,
    review_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


-- TODO: LEARN ABOUT INDEXING LATER FOR BETTER PERFORMANCE
CREATE INDEX idx_order_user ON orders(user_id);
CREATE INDEX idx_item_order ON order_items(order_id);
CREATE INDEX idx_item_product ON order_items(product_id);



INSERT INTO users (name, email) VALUES
    ('Harshith Kurapati', 'harshith.krpt@gmail.com'),
    ('Aarav Mehta', 'aarav.mehta@example.com'),
    ('Vihaan Iyer', 'vihaan.iyer@example.com'),
    ('Anaya Reddy', 'anaya.reddy@example.com'),
    ('Ishaan Shah', 'ishaan.shah@example.com'),
    ('Diya Verma', 'diya.verma@example.com'),
    ('Kabir Patel', 'kabir.patel@example.com'),
    ('Myra Singh', 'myra.singh@example.com'),
    ('Aditya Rao', 'aditya.rao@example.com'),
    ('Saanvi Nair', 'saanvi.nair@example.com'),
    ('Arjun Gupta', 'arjun.gupta@example.com'),
    ('Tanya Das', 'tanya.das@example.com'),
    ('Yuvraj Sinha', 'yuvraj.sinha@example.com'),
    ('Kiara Bansal', 'kiara.bansal@example.com'),
    ('Reyansh Joshi', 'reyansh.joshi@example.com'),
    ('Aadhya Malhotra', 'aadhya.malhotra@example.com'),
    ('Neil Dey', 'neil.dey@example.com'),
    ('Ira Kapoor', 'ira.kapoor@example.com'),
    ('Rudra Khanna', 'rudra.khanna@example.com'),
    ('Avni Desai', 'avni.desai@example.com'),
    ('Vivaan Bhatt', 'vivaan.bhatt@example.com'),
    ('Navya Kulkarni', 'navya.kulkarni@example.com'),
    ('Aryan Chatterjee', 'aryan.chatterjee@example.com'),
    ('Meera Ghosh', 'meera.ghosh@example.com'),
    ('Shaurya Jain', 'shaurya.jain@example.com'),
    ('Pari Srivastava', 'pari.srivastava@example.com'),
    ('Krishna Agrawal', 'krishna.agrawal@example.com'),
    ('Riya Tomar', 'riya.tomar@example.com'),
    ('Devansh Rathi', 'devansh.rathi@example.com'),
    ('Aisha Sehgal', 'aisha.sehgal@example.com');


INSERT INTO categories (name) VALUES 
('Electronics'), 
('Appliances'),
('Kitchen'),
('Clothing'),
('Footwear'),
('Beauty & Personal Care'),
('Books'),
('Toys & Games'),
('Fitness & Sports'),
('Home Decor'),
('Furniture'),
('Stationery'),
('Automotive'),
('Grocery'),
('Pet Supplies'),
('Mobile Accessories'),
('Watches'),
('Jewellery'),
('Luggage & Bags'),
('Gaming'),
('Health & Wellness'),
('Baby Products'),
('Office Supplies'),
('Music Instruments'),
('Lighting');


INSERT INTO products (name, category_id, price, stock) VALUES
-- Electronics
('iPhone 14', 1, 799.99, 500),
('Samsung Galaxy S23', 1, 699.99, 450),
('Sony WH-1000XM5 Headphones', 1, 299.99, 150),
('Canon DSLR Camera', 1, 549.99, 80),

-- Appliances
('LG Washing Machine', 2, 349.00, 100),
('Samsung Refrigerator', 2, 499.00, 90),
('Dyson Vacuum Cleaner', 2, 599.00, 120),
('Philips Air Fryer', 2, 199.00, 200),

-- Kitchen
('Non-stick Frying Pan Set', 3, 59.99, 300),
('Electric Kettle', 3, 39.99, 220),
('Rice Cooker', 3, 79.99, 180),
('Knife Set', 3, 29.99, 150),

-- Clothing
('Mens Leather Jacket', 4, 129.99, 60),
('Womens Summer Dress', 4, 49.99, 100),
('Unisex Hoodie', 4, 39.99, 120),
('Formal Trousers', 4, 34.99, 80),

-- Footwear
('Running Shoes', 5, 69.99, 150),
('Leather Loafers', 5, 89.99, 90),
('Womens Heels', 5, 59.99, 70),
('Casual Sneakers', 5, 44.99, 140),

-- Beauty & Personal Care
('Face Moisturizer', 6, 19.99, 300),
('Beard Trimmer', 6, 29.99, 200),
('Shampoo - Herbal', 6, 12.49, 250),
('Makeup Kit', 6, 39.99, 130),

-- Books
('The Alchemist', 7, 9.99, 500),
('Atomic Habits', 7, 11.99, 400),
('Sapiens: A Brief History', 7, 14.99, 300),
('Clean Code', 7, 29.99, 100),

-- Toys & Games
('Lego City Set', 8, 49.99, 120),
('Remote Control Car', 8, 39.99, 140),
('Board Game - Catan', 8, 34.99, 80),
('Barbie Doll Set', 8, 29.99, 200),

-- Fitness & Sports
('Yoga Mat', 9, 24.99, 150),
('Dumbbell Set', 9, 79.99, 100),
('Treadmill', 9, 499.00, 50),
('Resistance Bands', 9, 19.99, 160),

-- Home Decor
('Wall Painting', 10, 59.99, 60),
('Scented Candles Pack', 10, 24.99, 200),
('LED Fairy Lights', 10, 14.99, 180),
('Indoor Plant Pot Set', 10, 39.99, 90);



-- Sample E-Commerce SQL Insert Script

INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (1, 21, '2024-04-01 00:00:00', 2965.17, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (2, 5, '2024-03-26 00:00:00', 3990.87, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (3, 16, '2024-01-04 00:00:00', 4886.15, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (4, 17, '2024-02-27 00:00:00', 2354.74, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (5, 3, '2024-03-19 00:00:00', 1614.46, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (6, 6, '2024-03-04 00:00:00', 753.68, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (7, 12, '2024-04-24 00:00:00', 114.05, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (8, 7, '2024-04-02 00:00:00', 5335.22, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (9, 10, '2024-01-13 00:00:00', 1399.73, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (10, 25, '2024-02-29 00:00:00', 1889.56, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (11, 28, '2024-02-01 00:00:00', 1936.05, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (12, 26, '2024-02-06 00:00:00', 1171.74, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (13, 27, '2024-02-16 00:00:00', 5047.59, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (14, 20, '2024-03-24 00:00:00', 3856.81, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (15, 2, '2024-03-11 00:00:00', 2018.04, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (16, 1, '2024-03-14 00:00:00', 1369.66, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (17, 7, '2024-02-28 00:00:00', 2762.93, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (18, 2, '2024-01-05 00:00:00', 5684.45, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (19, 11, '2024-01-07 00:00:00', 3077.58, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (20, 2, '2024-03-29 00:00:00', 4700.43, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (21, 15, '2024-02-10 00:00:00', 3753.08, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (22, 2, '2024-01-31 00:00:00', 4644.05, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (23, 19, '2024-01-02 00:00:00', 1239.21, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (24, 13, '2024-01-26 00:00:00', 4900.77, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (25, 16, '2024-03-24 00:00:00', 621.94, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (26, 16, '2024-04-18 00:00:00', 2658.39, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (27, 23, '2024-03-18 00:00:00', 2216.83, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (28, 8, '2024-01-28 00:00:00', 659.46, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (29, 16, '2024-03-12 00:00:00', 1919.94, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (30, 7, '2024-02-15 00:00:00', 1732.41, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (31, 9, '2024-04-04 00:00:00', 4732.35, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (32, 1, '2024-04-21 00:00:00', 4539.71, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (33, 28, '2024-02-29 00:00:00', 3891.1, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (34, 10, '2024-03-15 00:00:00', 2545.85, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (35, 24, '2024-03-19 00:00:00', 3674.56, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (36, 19, '2024-04-04 00:00:00', 2007.72, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (37, 10, '2024-04-10 00:00:00', 951.19, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (38, 8, '2024-02-07 00:00:00', 1193.97, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (39, 16, '2024-03-18 00:00:00', 3988.32, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (40, 10, '2024-03-03 00:00:00', 813.93, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (41, 8, '2024-04-29 00:00:00', 4708.14, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (42, 30, '2024-01-27 00:00:00', 974.83, 'refunded');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (43, 22, '2024-03-17 00:00:00', 5960.21, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (44, 5, '2024-01-18 00:00:00', 6116.36, 'paid');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (45, 27, '2024-04-23 00:00:00', 963.51, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (46, 13, '2024-03-15 00:00:00', 1626.32, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (47, 21, '2024-03-13 00:00:00', 539.45, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (48, 13, '2024-04-21 00:00:00', 5571.1, 'failed');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (49, 6, '2024-01-18 00:00:00', 1742.89, 'processing');
INSERT INTO orders (id, user_id, ordered_at, total_amount, payment_status) VALUES (50, 20, '2024-02-10 00:00:00', 1539.14, 'processing');
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (7, 1, 2, 722.91);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (15, 1, 3, 397.35);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (29, 1, 1, 181.93);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (33, 1, 1, 145.37);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (25, 2, 2, 128.18);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (4, 2, 2, 189.36);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (28, 2, 3, 981.22);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (24, 2, 1, 412.13);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (36, 3, 3, 942.19);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (20, 3, 1, 804.6);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (2, 3, 2, 512.33);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (1, 3, 2, 115.16);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (27, 4, 1, 594.04);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (4, 4, 3, 586.9);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (22, 5, 1, 460.1);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (12, 5, 2, 577.18);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (14, 6, 2, 376.84);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (39, 7, 1, 114.05);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (23, 8, 1, 688.69);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (31, 8, 1, 604.51);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (9, 8, 3, 668.12);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (20, 8, 3, 679.22);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (7, 9, 1, 416.57);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (20, 9, 1, 983.16);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (12, 10, 2, 69.67);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (32, 10, 1, 205.96);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (36, 10, 1, 667.39);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (26, 10, 1, 876.87);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (36, 11, 3, 645.35);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (5, 12, 2, 585.87);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (36, 13, 1, 209.53);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (41, 13, 3, 765.57);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (37, 13, 2, 992.47);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (23, 13, 3, 185.47);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (32, 14, 3, 880.48);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (9, 14, 2, 189.5);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (24, 14, 1, 836.37);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (33, 15, 3, 382.97);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (26, 15, 3, 289.71);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (1, 16, 2, 562.46);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (40, 16, 1, 244.74);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (38, 17, 3, 423.56);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (10, 17, 1, 152.75);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (14, 17, 2, 526.23);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (36, 17, 3, 95.68);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (21, 18, 2, 947.23);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (22, 18, 2, 558.65);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (3, 18, 3, 579.97);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (10, 18, 1, 932.78);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (23, 19, 1, 227.89);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (16, 19, 1, 606.95);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (8, 19, 3, 685.49);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (40, 19, 3, 62.09);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (12, 20, 2, 282.51);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (25, 20, 3, 420.64);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (4, 20, 2, 263.01);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (13, 20, 3, 130.57);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (17, 20, 2, 977.88);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (7, 21, 2, 122.66);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (20, 21, 2, 212.2);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (31, 21, 3, 232.36);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (2, 21, 2, 590.77);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (24, 21, 3, 401.58);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (3, 22, 1, 434.5);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (24, 22, 3, 218.54);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (23, 22, 1, 863.05);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (39, 22, 3, 896.96);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (12, 23, 1, 527.13);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (28, 23, 1, 712.08);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (39, 24, 1, 453.17);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (1, 24, 2, 195.14);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (9, 24, 3, 878.68);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (25, 24, 3, 473.76);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (4, 25, 2, 310.97);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (15, 26, 1, 450.5);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (14, 26, 1, 807.51);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (4, 26, 2, 341.53);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (24, 26, 1, 717.32);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (21, 27, 1, 354.31);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (27, 27, 3, 620.84);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (28, 28, 2, 46.4);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (12, 28, 1, 566.66);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (23, 29, 3, 241.86);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (40, 29, 3, 398.12);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (13, 30, 3, 171.71);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (10, 30, 1, 129.77);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (1, 30, 3, 58.41);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (35, 30, 2, 320.78);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (36, 30, 3, 90.24);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (22, 31, 2, 812.29);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (7, 31, 2, 401.36);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (29, 31, 3, 768.35);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (25, 32, 1, 17.01);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (5, 32, 3, 364.86);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (7, 32, 1, 303.38);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (23, 32, 3, 730.93);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (12, 32, 1, 931.95);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (17, 33, 3, 289.89);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (16, 33, 2, 756.41);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (14, 33, 3, 272.11);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (36, 33, 2, 346.14);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (9, 34, 1, 971.87);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (30, 34, 1, 580.7);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (35, 34, 2, 419.72);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (13, 34, 3, 51.28);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (36, 35, 2, 426.3);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (39, 35, 3, 177.08);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (1, 35, 2, 991.08);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (40, 35, 2, 154.28);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (15, 36, 2, 620.65);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (38, 36, 1, 766.42);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (34, 37, 2, 135.93);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (27, 37, 1, 318.63);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (38, 37, 2, 180.35);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (24, 38, 3, 397.99);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (5, 39, 2, 638.06);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (15, 39, 2, 981.93);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (18, 39, 1, 314.02);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (8, 39, 2, 217.16);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (4, 40, 1, 813.93);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (41, 41, 3, 659.9);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (29, 41, 3, 547.16);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (36, 41, 1, 883.07);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (11, 41, 1, 203.89);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (40, 42, 1, 888.23);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (1, 42, 2, 43.3);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (29, 43, 3, 749.63);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (40, 43, 3, 782.35);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (30, 43, 2, 61.36);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (33, 43, 2, 235.74);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (20, 43, 1, 770.07);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (29, 44, 3, 495.02);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (37, 44, 3, 734.64);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (32, 44, 1, 137.21);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (40, 44, 3, 763.39);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (6, 45, 3, 111.93);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (32, 45, 1, 627.72);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (3, 46, 1, 630.22);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (16, 46, 1, 81.96);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (21, 46, 1, 914.14);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (35, 47, 1, 77.18);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (7, 47, 3, 154.09);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (13, 48, 2, 327.08);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (8, 48, 3, 792.87);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (9, 48, 3, 686.72);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (37, 48, 3, 159.39);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (3, 49, 1, 965.02);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (4, 49, 3, 259.29);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (29, 50, 3, 77.56);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (32, 50, 1, 438.86);
INSERT INTO order_items (product_id, order_id, quantity, price) VALUES (38, 50, 1, 867.6);
INSERT INTO payments (order_id, method, status, paid_at) VALUES (1, 'wallet', 'success', '2024-04-02 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (2, 'upi', 'failed', '2024-03-27 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (3, 'card', 'pending', '2024-01-05 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (4, 'card', 'success', '2024-02-28 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (5, 'wallet', 'success', '2024-03-20 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (6, 'card', 'pending', '2024-03-05 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (7, 'upi', 'success', '2024-04-25 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (8, 'card', 'success', '2024-04-03 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (9, 'card', 'failed', '2024-01-14 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (10, 'card', 'success', '2024-03-01 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (11, 'wallet', 'pending', '2024-02-02 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (12, 'upi', 'failed', '2024-02-07 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (13, 'card', 'success', '2024-02-17 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (14, 'card', 'success', '2024-03-25 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (15, 'wallet', 'pending', '2024-03-12 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (16, 'card', 'failed', '2024-03-15 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (17, 'upi', 'pending', '2024-02-29 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (18, 'card', 'success', '2024-01-06 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (19, 'upi', 'failed', '2024-01-08 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (20, 'cod', 'failed', '2024-03-30 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (21, 'cod', 'success', '2024-02-11 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (22, 'cod', 'failed', '2024-02-01 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (23, 'cod', 'pending', '2024-01-03 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (24, 'upi', 'success', '2024-01-27 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (25, 'cod', 'failed', '2024-03-25 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (26, 'wallet', 'failed', '2024-04-19 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (27, 'card', 'pending', '2024-03-19 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (28, 'upi', 'success', '2024-01-29 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (29, 'card', 'success', '2024-03-13 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (30, 'card', 'success', '2024-02-16 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (31, 'wallet', 'pending', '2024-04-05 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (32, 'wallet', 'success', '2024-04-22 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (33, 'card', 'pending', '2024-03-01 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (34, 'cod', 'failed', '2024-03-16 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (35, 'wallet', 'pending', '2024-03-20 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (36, 'cod', 'pending', '2024-04-05 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (37, 'cod', 'pending', '2024-04-11 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (38, 'cod', 'failed', '2024-02-08 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (39, 'upi', 'pending', '2024-03-19 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (40, 'card', 'pending', '2024-03-04 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (41, 'upi', 'success', '2024-04-30 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (42, 'wallet', 'success', '2024-01-28 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (43, 'wallet', 'pending', '2024-03-18 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (44, 'wallet', 'success', '2024-01-19 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (45, 'wallet', 'success', '2024-04-24 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (46, 'wallet', 'success', '2024-03-16 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (47, 'wallet', 'failed', '2024-03-14 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (48, 'upi', 'pending', '2024-04-22 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (49, 'card', 'failed', '2024-01-19 00:00:00');
INSERT INTO payments (order_id, method, status, paid_at) VALUES (50, 'card', 'success', '2024-02-11 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (1, 'in_transit', 'Flat 12, Street 37', 'EcomExpress', '2024-04-04 00:00:00', '2024-04-06 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (2, 'shipped', 'Flat 38, Street 27', 'EcomExpress', '2024-03-29 00:00:00', '2024-03-31 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (3, 'shipped', 'Flat 66, Street 9', 'EcomExpress', '2024-01-07 00:00:00', '2024-01-09 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (4, 'shipped', 'Flat 67, Street 3', 'EcomExpress', '2024-03-01 00:00:00', '2024-03-03 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (5, 'pending', 'Flat 68, Street 1', 'BlueDart', '2024-03-22 00:00:00', '2024-03-24 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (6, 'pending', 'Flat 32, Street 14', 'Delhivery', '2024-03-07 00:00:00', '2024-03-09 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (7, 'in_transit', 'Flat 62, Street 20', 'Delhivery', '2024-04-27 00:00:00', '2024-04-29 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (8, 'pending', 'Flat 4, Street 48', 'EcomExpress', '2024-04-05 00:00:00', '2024-04-07 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (9, 'shipped', 'Flat 57, Street 37', 'EcomExpress', '2024-01-16 00:00:00', '2024-01-18 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (10, 'shipped', 'Flat 33, Street 18', 'EcomExpress', '2024-03-03 00:00:00', '2024-03-05 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (11, 'pending', 'Flat 32, Street 33', 'Delhivery', '2024-02-04 00:00:00', '2024-02-06 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (12, 'shipped', 'Flat 63, Street 46', 'Delhivery', '2024-02-09 00:00:00', '2024-02-11 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (13, 'pending', 'Flat 21, Street 44', 'BlueDart', '2024-02-19 00:00:00', '2024-02-21 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (14, 'in_transit', 'Flat 90, Street 1', 'BlueDart', '2024-03-27 00:00:00', '2024-03-29 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (15, 'shipped', 'Flat 58, Street 17', 'EcomExpress', '2024-03-14 00:00:00', '2024-03-16 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (16, 'shipped', 'Flat 36, Street 11', 'BlueDart', '2024-03-17 00:00:00', '2024-03-19 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (17, 'cancelled', 'Flat 53, Street 43', 'EcomExpress', '2024-03-02 00:00:00', '2024-03-04 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (18, 'in_transit', 'Flat 51, Street 28', 'BlueDart', '2024-01-08 00:00:00', '2024-01-10 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (19, 'shipped', 'Flat 52, Street 43', 'EcomExpress', '2024-01-10 00:00:00', '2024-01-12 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (20, 'pending', 'Flat 67, Street 43', 'Delhivery', '2024-04-01 00:00:00', '2024-04-03 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (21, 'pending', 'Flat 37, Street 30', 'Delhivery', '2024-02-13 00:00:00', '2024-02-15 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (22, 'pending', 'Flat 86, Street 33', 'BlueDart', '2024-02-03 00:00:00', '2024-02-05 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (23, 'shipped', 'Flat 68, Street 13', 'EcomExpress', '2024-01-05 00:00:00', '2024-01-07 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (24, 'in_transit', 'Flat 96, Street 26', 'BlueDart', '2024-01-29 00:00:00', '2024-01-31 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (25, 'in_transit', 'Flat 12, Street 42', 'BlueDart', '2024-03-27 00:00:00', '2024-03-29 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (26, 'cancelled', 'Flat 15, Street 49', 'Delhivery', '2024-04-21 00:00:00', '2024-04-23 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (27, 'shipped', 'Flat 31, Street 27', 'Delhivery', '2024-03-21 00:00:00', '2024-03-23 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (28, 'pending', 'Flat 96, Street 26', 'BlueDart', '2024-01-31 00:00:00', '2024-02-02 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (29, 'in_transit', 'Flat 20, Street 38', 'Delhivery', '2024-03-15 00:00:00', '2024-03-17 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (30, 'in_transit', 'Flat 86, Street 18', 'BlueDart', '2024-02-18 00:00:00', '2024-02-20 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (31, 'delivered', 'Flat 85, Street 20', 'Delhivery', '2024-04-07 00:00:00', '2024-04-09 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (32, 'in_transit', 'Flat 27, Street 14', 'Delhivery', '2024-04-24 00:00:00', '2024-04-26 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (33, 'cancelled', 'Flat 45, Street 24', 'BlueDart', '2024-03-03 00:00:00', '2024-03-05 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (34, 'pending', 'Flat 62, Street 12', 'EcomExpress', '2024-03-18 00:00:00', '2024-03-20 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (35, 'cancelled', 'Flat 45, Street 9', 'Delhivery', '2024-03-22 00:00:00', '2024-03-24 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (36, 'in_transit', 'Flat 49, Street 28', 'Delhivery', '2024-04-07 00:00:00', '2024-04-09 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (37, 'cancelled', 'Flat 30, Street 22', 'BlueDart', '2024-04-13 00:00:00', '2024-04-15 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (38, 'in_transit', 'Flat 47, Street 39', 'Delhivery', '2024-02-10 00:00:00', '2024-02-12 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (39, 'delivered', 'Flat 47, Street 19', 'EcomExpress', '2024-03-21 00:00:00', '2024-03-23 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (40, 'in_transit', 'Flat 18, Street 17', 'EcomExpress', '2024-03-06 00:00:00', '2024-03-08 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (41, 'pending', 'Flat 69, Street 17', 'BlueDart', '2024-05-02 00:00:00', '2024-05-04 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (42, 'pending', 'Flat 11, Street 7', 'BlueDart', '2024-01-30 00:00:00', '2024-02-01 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (43, 'shipped', 'Flat 34, Street 11', 'EcomExpress', '2024-03-20 00:00:00', '2024-03-22 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (44, 'pending', 'Flat 20, Street 43', 'Delhivery', '2024-01-21 00:00:00', '2024-01-23 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (45, 'pending', 'Flat 11, Street 21', 'EcomExpress', '2024-04-26 00:00:00', '2024-04-28 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (46, 'in_transit', 'Flat 74, Street 10', 'Delhivery', '2024-03-18 00:00:00', '2024-03-20 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (47, 'pending', 'Flat 19, Street 40', 'EcomExpress', '2024-03-16 00:00:00', '2024-03-18 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (48, 'delivered', 'Flat 79, Street 4', 'BlueDart', '2024-04-24 00:00:00', '2024-04-26 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (49, 'cancelled', 'Flat 81, Street 8', 'BlueDart', '2024-01-21 00:00:00', '2024-01-23 00:00:00');
INSERT INTO deliveries (order_id, status, delivery_address, courier_name, expected_delivery, delivered_at) VALUES (50, 'in_transit', 'Flat 54, Street 35', 'BlueDart', '2024-02-13 00:00:00', '2024-02-15 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (7, 21, 4, 'Good product 7', '2024-04-07 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (15, 21, 5, 'Good product 15', '2024-04-07 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (29, 21, 5, 'Good product 29', '2024-04-07 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (33, 21, 5, 'Good product 33', '2024-04-07 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (25, 5, 3, 'Good product 25', '2024-04-01 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (4, 5, 5, 'Good product 4', '2024-04-01 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (28, 5, 3, 'Good product 28', '2024-04-01 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (24, 5, 5, 'Good product 24', '2024-04-01 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (27, 17, 5, 'Good product 27', '2024-03-04 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (4, 17, 3, 'Good product 4', '2024-03-04 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (39, 12, 5, 'Good product 39', '2024-04-30 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (23, 7, 4, 'Good product 23', '2024-04-08 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (31, 7, 4, 'Good product 31', '2024-04-08 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (9, 7, 5, 'Good product 9', '2024-04-08 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (20, 7, 4, 'Good product 20', '2024-04-08 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (36, 27, 3, 'Good product 36', '2024-02-22 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (41, 27, 3, 'Good product 41', '2024-02-22 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (37, 27, 5, 'Good product 37', '2024-02-22 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (23, 27, 3, 'Good product 23', '2024-02-22 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (32, 20, 5, 'Good product 32', '2024-03-30 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (9, 20, 5, 'Good product 9', '2024-03-30 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (24, 20, 5, 'Good product 24', '2024-03-30 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (33, 2, 5, 'Good product 33', '2024-03-17 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (26, 2, 5, 'Good product 26', '2024-03-17 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (21, 2, 4, 'Good product 21', '2024-01-11 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (22, 2, 5, 'Good product 22', '2024-01-11 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (3, 2, 3, 'Good product 3', '2024-01-11 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (10, 2, 5, 'Good product 10', '2024-01-11 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (23, 11, 5, 'Good product 23', '2024-01-13 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (16, 11, 5, 'Good product 16', '2024-01-13 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (8, 11, 3, 'Good product 8', '2024-01-13 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (40, 11, 5, 'Good product 40', '2024-01-13 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (3, 2, 3, 'Good product 3', '2024-02-06 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (24, 2, 4, 'Good product 24', '2024-02-06 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (23, 2, 5, 'Good product 23', '2024-02-06 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (39, 2, 3, 'Good product 39', '2024-02-06 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (4, 16, 5, 'Good product 4', '2024-03-30 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (15, 16, 4, 'Good product 15', '2024-04-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (14, 16, 4, 'Good product 14', '2024-04-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (4, 16, 3, 'Good product 4', '2024-04-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (24, 16, 4, 'Good product 24', '2024-04-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (21, 23, 5, 'Good product 21', '2024-03-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (27, 23, 3, 'Good product 27', '2024-03-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (25, 1, 3, 'Good product 25', '2024-04-27 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (5, 1, 5, 'Good product 5', '2024-04-27 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (7, 1, 3, 'Good product 7', '2024-04-27 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (23, 1, 5, 'Good product 23', '2024-04-27 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (12, 1, 5, 'Good product 12', '2024-04-27 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (36, 24, 5, 'Good product 36', '2024-03-25 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (39, 24, 4, 'Good product 39', '2024-03-25 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (1, 24, 5, 'Good product 1', '2024-03-25 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (40, 24, 5, 'Good product 40', '2024-03-25 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (34, 10, 4, 'Good product 34', '2024-04-16 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (27, 10, 4, 'Good product 27', '2024-04-16 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (38, 10, 4, 'Good product 38', '2024-04-16 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (5, 16, 4, 'Good product 5', '2024-03-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (15, 16, 3, 'Good product 15', '2024-03-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (18, 16, 3, 'Good product 18', '2024-03-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (8, 16, 5, 'Good product 8', '2024-03-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (40, 30, 3, 'Good product 40', '2024-02-02 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (1, 30, 5, 'Good product 1', '2024-02-02 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (29, 5, 5, 'Good product 29', '2024-01-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (37, 5, 4, 'Good product 37', '2024-01-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (32, 5, 5, 'Good product 32', '2024-01-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (40, 5, 4, 'Good product 40', '2024-01-24 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (3, 13, 4, 'Good product 3', '2024-03-21 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (16, 13, 5, 'Good product 16', '2024-03-21 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (21, 13, 3, 'Good product 21', '2024-03-21 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (13, 13, 4, 'Good product 13', '2024-04-27 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (8, 13, 4, 'Good product 8', '2024-04-27 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (9, 13, 3, 'Good product 9', '2024-04-27 00:00:00');
INSERT INTO product_reviews (product_id, user_id, rating, reviews, review_date) VALUES (37, 13, 3, 'Good product 37', '2024-04-27 00:00:00');


SELECT DISTINCT u.id, u.name FROM users u INNER JOIN orders o ON o.user_id = u.id;


SELECT * FROM products p WHERE p.stock <= 0;
SELECT u.name, u.id, o.total_amount FROM users u INNER JOIN  orders o ON u.id = o.user_id;

SELECT 
    oi.product_id, p.name as product_name 
    FROM order_items oi 
    INNER JOIN products p ON p.id = oi.product_id
      WHERE oi.order_id = 5; 

SELECT p.name,  pr.reviews, pr.rating, pr.review_date, u.name FROM product_reviews pr INNER JOIN products p ON pr.product_id= p.id INNER JOIN users u ON u.id = pr.user_id;


SELECT oi.product_id, p.name, oi.price FROM order_items oi INNER JOIN products p ON p.id = oi.product_id  ORDER BY price DESC LIMIT 10;

SELECT  u.name, sum(total_amount)  FROM orders o INNER JOIN users u ON u.id = o.user_id  GROUP BY o.user_id;

SELECT d.order_id, o.payment_status, u.name FROM deliveries d INNER JOIN orders o ON o.id = d.order_id INNER JOIN users u ON
u.id = o.user_id WHERE d.courier_name = 'BlueDart';

SELECT DISTINCT u.name FROM users u INNER JOIN product_reviews pr ON pr.user_id = u.id WHERE pr.rating < 4;


SELECT p.id, p.name 
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
WHERE oi.product_id IS NULL;

SELECT AVG(pr.rating) as avg_rating, p.name FROM product_reviews pr INNER JOIN products p ON pr.product_id = p.id GROUP BY p.
id ORDER BY avg_rating DESC;

SELECT COUNT(o.id), d.status FROM orders o INNER JOIN deliveries d ON d.order_id = o.id GROUP BY d.status;

SELECT u.name, u.id, COUNT(o.id) as order_count FROM users u INNER JOIN orders o ON o.user_id = u.id GROUP BY u.id HAVING count(o.id) > 3;

SELECT SUM(oi.quantity) quantity_sold, p.name, p.stock FROM order_items oi INNER JOIN products p ON p.id = oi.product_id GROUP BY oi.product_id;

SELECT SUM(oi.quantity) as quantity_sold, p.name, p.stock FROM order_items oi  INNER JOIN products p ON p.id = oi.product_id GROUP BY oi.product_id ORDER BY quantity_sold DESC LIMIT 5;



SELECT 
    u.id,
    u.name, 
    SUM(o.total_amount) AS total_spent
FROM orders o 
INNER JOIN users u ON u.id = o.user_id 
GROUP BY u.id, u.name
HAVING total_spent = (
    SELECT MAX(user_total)
    FROM (
        SELECT user_id, SUM(total_amount) AS user_total
        FROM orders 
        GROUP BY user_id
    ) AS totals
);
