import sqlite3

# Connect to a database (creates the file if it doesn’t exist)
conn = sqlite3.connect("files/students.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")
conn.commit()

cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
               ("Alice", 20, "A"))
conn.commit()



result = cursor.execute('SELECT * FROM students')
rows = result.fetchall()

for r in rows:
    print(r)


with sqlite3.connect("files/students.db") as conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
                ("Bob", 22, "B"))
