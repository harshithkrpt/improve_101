-- 🧩 1. Super Key

-- Definition:
-- A Super Key is any combination of attributes (columns) that can uniquely identify a record (row) in a table.

-- Key idea:
-- Every table must have at least one super key, but a table may have many possible super keys.

-- STUDENTS (student_id, email, phone, name)

-- Here:

-- {student_id} uniquely identifies a student ✅

-- {email} also uniquely identifies a student ✅

-- {student_id, email} also uniquely identifies a student ✅

-- All of the above are Super Keys.
-- But some are redundant — and that’s where the Candidate Key comes in.


-- 🔑 2. Candidate Key

-- Definition:
-- A Candidate Key is a minimal super key — meaning, it uniquely identifies a record, and if you remove any attribute from it, it no longer remains unique.

-- Key idea:
-- A table can have multiple candidate keys, but only one is usually chosen as the Primary Key.

-- Example (continuing previous table):

-- {student_id} ✅ unique, minimal

-- {email} ✅ unique, minimal

-- {student_id, email} ❌ not minimal (because student_id alone is enough)

-- So, Candidate Keys = {student_id, email}

-- 🧠 3. Primary Key

-- Definition:
-- A Primary Key is the chosen candidate key that uniquely identifies records in a table.
-- It cannot be NULL and must contain unique values.

-- Key idea:
-- There’s only one primary key per table (though it can consist of multiple columns — that’s called a composite key).

CREATE TABLE STUDENTS (
  student_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  phone VARCHAR(15)
);

-- 🧭 4. Alternate Key

-- Definition:
-- An Alternate Key is any candidate key that is not chosen as the primary key.

-- Key idea:
-- It’s a backup identifier — still unique, still capable of identifying rows, but not the main one.

-- Example:
-- From our STUDENTS table:

-- Candidate keys = {student_id}, {email}

-- Primary key = {student_id}
-- So, Alternate key = {email}

-- 🧩 5. Composite Key

-- Definition:
-- A Composite Key is a key made up of two or more attributes that together uniquely identify a record — but neither alone can do so.

-- Key idea:
-- Used when no single column is unique, but a combination is.

-- Example:


-- 🌐 6. Foreign Key

-- Definition:
-- A Foreign Key is an attribute (or set of attributes) in one table that refers to the Primary Key in another table.
-- It’s used to maintain referential integrity between tables.

-- Key idea:
-- It links related data — ensuring that relationships are consistent.

-- Example:


CREATE TABLE STUDENTS (
  student_id INT PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE ENROLLMENTS (
  enrollment_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  FOREIGN KEY (student_id) REFERENCES STUDENTS(student_id)
);
 

 -- DQL
 
-- this is a comment
# this is a single line comment

/*
 * 
 * 
 * 	This is a Multi Line Comment
 * 
 */

USE PlanetaryGoods;


SELECT
	p.ProductName,
	p.ProductID,
	p.Description ,
	p.SupplierID,
	p.Category,
	p.SubCategory,
	p.Price 
from
	Products p
WHERE
	p.ProductName = "Space Adventure Puzzle"
	

	
SELECT 
	DISTINCT City
	FROM
	Customers c;


SELECT DISTINCT Country, City FROM Customers c;


SELECT DISTINCT Category , SubCategory FROM Products ORDER BY Category;


SELECT FirstName as "THIS IS A FIRST NAME" FROM Customers c;

 
SELECT Concat(FIRSTNAME, " ", LASTNAME) AS "Full Name" FROM Customers c;




SELECT 12 - 4;

SELECT 10 + 2;

SELECT 10 * 22;

SELECT p.ProductID , p.ProductName  , p.Price  * p.InStockQuantity as TOTAL_WORTH  FROM Products p ;

SELECT * FROM Customers c WHERE c.Address is NULL; -- null values can not be compared with comparision operators

SELECT count(address) FROM Customers c WHERE c.Address is NOT NULL;

-- below is how ww add aplaceholder when adding null value
SELECT c.FirstName ,c.LastName , IFNULL(c.Address, "Address Not Provided") AS Address  FROM Customers c;

-- https://chatgpt.com/share/68f6f71d-547c-8006-9060-23f724df4e9f
SELECT c.FirstName , c.LastName , COALESCE(c.Address, CONCAT("N/A Address", c.City )) AS Address FROM Customers c;


-- ORDER BY CLAUSE FOR SORTING THE ROWS IN AESENDING OR DESCENDING ORDER
SELECT * FROM Orders ORDER BY OrderDate DESC;
SELECT * FROM Orders ORDER BY TotalPaid;

SELECT * FROM Orders ORDER BY ShippingStatus, TotalPaid;

SELECT * FROM Products p WHERE p.SupplierID = 1 ORDER BY Category DESC, ProductName; 

SELECT * FROM Products p ORDER BY p.Price DESC;

-- LIMIT Resuts Only Fetch few records
SELECT * FROM Products p ORDER BY p.Price DESC LIMIT 10;

-- Skipping functionality comes with OFFSET
SELECT * FROM Products p ORDER BY p.Price DESC LIMIT 10 OFFSET 20;


select * FROM Products p ORDER BY p.Price DESC LIMIT 5;


-- WHERE CLAUSE -> IF TRUE OF EACH RECORD IT WILL BE RETURNED TRUE
SELECT * FROM Customers WHERE Country = 'USA';

/*
	Arithmetic Operators
	+
	-
	/
	%
	*

	Comparision 
	=
	<>
	<
	>
	<=
	>=

	LOGICAL OPERATORS
	AND
	OR
	NOT
*/


SELECT
	PRODUCTNAME,
	PRICE AS "Actual Price",
	PRICE * 0.1 AS "DISCOUNT 10%",
	PRICE * 0.9 AS "DISCOUNTED PRICE"
FROM
	Products;


SELECT * FROM PlanetaryGoods.Products p WHERE p.Price - 10 > 10;
SELECT * FROM PlanetaryGoods.Products p WHERE p.Price + 10 > 10;

SELECT
	*
FROM
	M OrderDetails od
WHERE
	od.Tax > od.FinalTotal * 0.05;


	SELECT
	*
FROM
	Products p
WHERE
	p.Price > 20
	AND p.Price < 50
ORDER BY p.Price DESC;

SELECT
	*
FROM
	Products
WHERE
	Category = 'Art'
	AND SubCategory != 'Posters'
	AND Price < 10
	;

SELECT * FROM Products p WHERE p.Category  = 'Accessories' AND p.Price < 30;


SELECT * FROM Products p WHERE p.Category  = 'Accessories' OR p.Price < 30;

SELECT course_name, department FROM courses WHERE department = 'Computer Science' OR department = 'Mathematics';

  SELECT * FROM Products p WHERE (p.Category = 'Accessories' OR p.Category = 'Optics') AND p.InStockQuantity < 20;

-- Not operator for reversing the where condition and reversing it 
  SELECT * FROM Products p WHERE NOT p.Category = "Optics" LIMIT 10;


  -- INSTEAD OF MULTIPLE ORS WE CAN USE "IN" OPERSOT

  SELECT * FROM Customers c WHERE c.Country IN ('USA', 'CANADA')

  -- NOT IN WILL REVERSE

  SELECT * FROM Customers c WHERE c.Country NOT IN ('USA', 'CANADA')


  SELECT PRODUCTNAME, PRICE, CATEGORY FROM Products p WHERE p.Category  IN ('Accessories', 'Optics');

  -- BETWEEN OPERATOR IN SQL (SQL FOR RANGE) TESTING


SELECT p.Price,p.ProductName  FROM Products p WHERE p.Price BETWEEN 10 AND 20 ORDER BY PRICE;

-- between is inclusive
-- most of the time betwwwn is used with data ranges 

SELECT
	p.ProductName ,
	p.Description ,
	p.Price
FROM
	Products p
WHERE
	p.Category = 'Home Decor'
	AND
	p.Price BETWEEN 20 AND 100
ORDER BY
	p.ProductName;


-- Like Operator for Searching the Data or Pattern

-- % (Percent Sign) - zero or multiple chars
-- _ (underscore) - reprs a single chars
SELECT * FROM Customers c WHERE c.FirstName  LIKE 'Jo__'

SELECT * FROM Customers c WHERE c.FirstName  LIKE 'J%'

SELECT * FROM Customers c WHERE c.FirstName  LIKE '%ia';

SELECT * FROM Customers c WHERE c.FirstName  LIKE '_ia';

SELECT * FROM Customers c WHERE c.FirstName  LIKE '_____';

SELECT * FROM Customers c WHERE LENGTH(c.FirstName) = 5;

-- Like Operator is Case Insensitive in case of MYSQL

-- Below is Escape Hatching or ignoring escape hatches
SELECT * FROM Products p WHERE p.ProductName LIKE '%5!%%' ESCAPE '!';

select university_name from universities WHERE university_name LIKE '%Tech%';


SELECT * from Products p WHERE p.ProductName LIKE 'Star%';

-- Null Operator
-- IS NULL 
-- IS NOT NULL 

SELECT * FROM Customers c WHERE c.Address IS NULL;
SELECT * FROM Customers c WHERE c.Address IS NOT NULL;


-- = <> CAN'T be used for selecting the operators of checking null
SELECT account_number, account_holder, account_manager FROM bank_accounts WHERE account_manager IS NULL;

-- aggregate functions
-- count()
-- sum()
-- avg()
-- min()
-- max()
SELECT COUNT(*) FROM Customers c;

SELECT  COUNT(DISTINCT CITY) AS 'Cities' FROM Customers c ;

SELECT SUM(o.TotalPaid) FROM Orders o ;

SELECT AVG(o.TotalPaid) FROM Orders o ;

SELECT MIN(o.TotalPaid) FROM Orders o;

SELECT MAX(o.TotalPaid) FROM Orders o;


-- Aggregate will ignore NULL From Calculations

SELECT SUM(quantity) AS "Total Quantity", SUM(price_per_unit * quantity) AS "Total Value (USD)" FROM grocery_inventory;

-- GROUP BY
-- USE WHERE CLAUSE BEFORE GROUP BY

SELECT count(*), c.city FROM Customers c GROUP BY c.City;

SELECT
	od.ProductID,
	SUM(od.Quantity) AS FinalTotal
FROM
	OrderDetails od
GROUP BY
	od.ProductID
ORDER BY
	FinalTotal DESC
LIMIT 10;


SELECT
	od.ProductID,
	SUM(od.Quantity) AS FinalTotal,
	COUNT(od.OrderID)
FROM
	OrderDetails od
GROUP BY
	od.ProductID
ORDER BY
	FinalTotal DESC
;

SELECT artist_name, SUM(sale_amount) AS "Total Sales (USD)" FROM art_sales GROUP BY artist_name ORDER BY "Total Sales (USD)" DESC

SELECT od.ProductID, SUM(od.Quantity), SUM(od.FinalTotal ) FROM OrderDetails od GROUP BY od.ProductID;


USE PlanetaryGoods;

SHOW TABLES;

-- JOINS
-- COMBINATION COLUMNS FROM DIFFERENT TABLES

-- Customer And Orders Relation Ship

-- INNER JOIN
-- LEFT JOIN
-- RIGHT JOIN 
-- FULL JOIN

-- NULL VALUES ARE ADDED IF NOT INTERSECTING OR A OPTIONAL VALUE IS NOT AVAILABLE
SELECT
	CONCAT(c.FirstName , " " , c.LastName ),
	o.OrderID ,
	o.TotalPaid
FROM
	Customers c
INNER JOIN Orders o
ON
	o.CustomerID = c.CustomerID;





-- Multiple Table Joins 
SELECT c.FirstName ,c.LastName, p.ProductName, SUM(od.Quantity) AS "Total Quantity" FROM Customers c 
INNER JOIN Orders o ON c.CustomerID  = o.CustomerID
INNER JOIN OrderDetails od ON od.OrderID  = o.OrderID
INNER JOIN Products p ON p.ProductID = od.ProductID GROUP BY c.FirstName,c.LastName,p.ProductName;



-- DEFAULT JOIN USED IN MYSQL IS INNER JOIN SO MENTIONING JOIN JEY WILL BE SAME BUT GOOD PRACTICE TO ADD INNER JOIN


SELECT
	p.ProductName,
	p.ProductId,
	SUM(od.FinalTotal)
FROM
	Products p
INNER JOIN OrderDetails od ON
	od.ProductID = p.ProductID
GROUP BY
	p.ProductID,
	p.ProductName ;

SELECT
	CONCAT(c.FirstName , " " , c.LastName ),
	o.OrderID ,
	o.TotalPaid
FROM
	Customers c
LEFT JOIN Orders o
ON
	o.CustomerID = c.CustomerID;


SELECT
	p.ProductName,
	p.ProductId,
	COALESCE(SUM(od.Quantity), 0) as total_orders
FROM
	Products p
LEFT JOIN OrderDetails od 
ON
	p.ProductID = od.ProductID
GROUP BY
	p.ProductID
ORDER BY
	total_orders DESC;

-- Right Join is Complete Oppisite of left join 
-- It will return all the rows from the right table and matched rows from the left 

-- INSTEAD OF "ON" WE CAN USE "USING" if the column name is matching in a bracket notation

/*
	select column_name(s)
	from table1
	inner join table2 
	using (column_name);
*/

SELECT
	CONCAT(c.FirstName , " " , c.LastName ),
	o.OrderID ,
	o.TotalPaid
FROM
	Customers c
INNER JOIN Orders o
USING (CustomerID);


-- SELF JOIN IS JOINING THE SAME TABLE WITH CONDITION


SELECT
	p1.ProductName,
	p2.ProductName,
	p1.Price AS product1_price,
	p2.Price AS Procut2_price
FROM
	Products p1 
JOIN Products p2 ON
	p1.productId != p2.ProductId
	AND ABS(p1.Price - p2.Price) < 1;


SELECT e1.employee_id, e1.employee_name, e2.employee_name as "supervisor_name" 
FROM employees e1 
    JOIN employees e2 
ON e1.supervisor_id = e2.employee_id;


SELECT
	c1.CustomerID,
	c2.CustomerId,
	c1.city
from
	Customers c1
JOIN Customers c2 ON
	c1.city = c2.city
	AND c1.CustomerID <> c2.CustomerID 
ORDER BY
	c1.city ;SELECT
	c1.CustomerID,
	c2.CustomerId,
	c1.city
from
	Customers c1
JOIN Customers c2 ON
	c1.city = c2.city
	AND c1.CustomerID <> c2.CustomerID 
ORDER BY
	c1.city ;

	-- CROSS JOIN produces the Cartesian product of two tables — meaning every row from the first table is paired with every row from the second table.


	SELECT c.FirstName, p.productname FROM Customers c CROSS JOIN Products p LIMIT 12 OFFSET 40;

	SELECT t.team_name AS "team", s.stadium_name AS "stadium"
FROM teams t
CROSS JOIN stadiums s;


-- natural join 

SELECT * FROM Orders NATURAL JOIN OrderDetails od ;



USE QUANTUM_TUTORS;

/*
Create the Instructors, Courses, Enrollments, Lessons, Payments, 
Reviews, and Admins tables for the Quantum Tutors using the 
provided schema.
*/

SHOW TABLES;

DROP TABLE customer;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    contact_number VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255),
    registration_date DATE,
    PRIMARY KEY (customer_id)
);

CREATE TABLE instructors (
    instructor_id INT AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    bio TEXT,
    contact_number VARCHAR(255),
    email VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    country VARCHAR(255),
    PRIMARY KEY (instructor_id)
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT,
    title VARCHAR(255),
    subtitle VARCHAR(255),
    description TEXT,
    price DECIMAL(10,2),
    instructor_id INT,
    category VARCHAR(255),
    sub_category VARCHAR(255),
    url VARCHAR(255),
    publish_date DATE,
    PRIMARY KEY (course_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT,
    customer_id INT,
    course_id INT,
    enrollment_date DATE,
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE lessons (
    lesson_id INT AUTO_INCREMENT,
    course_id INT,
    name VARCHAR(255),
    description TEXT,
    content TEXT,
    duration INT,
    PRIMARY KEY (lesson_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    customer_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    method VARCHAR(255),
    PRIMARY KEY (payment_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT,
    course_id INT,
    customer_id INT,
    rating INT,
    comment TEXT,
    review_date DATE,
    PRIMARY KEY (review_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE admins (
    admin_id INT AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    contact_number VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    PRIMARY KEY (admin_id)
);


