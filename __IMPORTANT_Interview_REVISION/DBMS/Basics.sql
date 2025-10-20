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



