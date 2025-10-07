import pickle

# A Python object
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Machine Learning", "FastAPI"]
}

# Serialize (save) to a binary file
with open("files/data.pkl", "wb") as file:
    pickle.dump(data, file)

# Deserialize (load) back
with open("files/data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
