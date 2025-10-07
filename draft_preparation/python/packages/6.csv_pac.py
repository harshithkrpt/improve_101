import csv

with open("files/app.csv", 'r') as f:
    loop = csv.reader(f)
    for row in loop:
        print(row, type(row))
        

with open("files/app.csv", 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

data = [
    ['name', 'age', 'grade'],
    ['Alice', 14, 'A'],
    ['Bob', 15, 'B']
]

with open('files/students_out.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


fields = ['name', 'age', 'grade']
rows = [
    {'name': 'Alice', 'age': 14, 'grade': 'A'},
    {'name': 'Bob', 'age': 15, 'grade': 'B'}
]

with open('files/students_out2.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()   # Writes the header row
    writer.writerows(rows)
