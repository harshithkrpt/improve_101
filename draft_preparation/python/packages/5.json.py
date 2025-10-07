import json

data = {
    "name": "Harshith",
    "languages": ["Python", "Rust"],
    "experience": 4
}

json_string = json.dumps(data)  # Converts dict → JSON string
print(json_string)
print(json.dumps(data, indent=2))

print(json.dumps(data, sort_keys=True, separators=(",", ": ")))



with open("files/newfile.json", 'w') as f:
    f.write(json.dumps(data, sort_keys=True, separators=(",", ": "), indent= 2))


with open("files/newfile.json", 'r') as f:
    data = json.loads(f.read())
    print(data['name'])
