with open('./9.files.py') as file:
    print(file.read())
    file.close()

from pathlib import Path

home = Path.home()


with open(f'{home}/bacon.txt', 'w') as file:
    file.write("Hello World")
    file.close()

# read the file
with open(f'{home}/bacon.txt') as file:
    print(file.read())
    file.close()


import json


dictionary = {"name": 1, "key": 2}
with open('testing.json', "w") as file:
    json.dump(dictionary, file)

with open('testing.json') as file:
    print(json.load(file))