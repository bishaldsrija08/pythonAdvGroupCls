import json

data = {
    "name": "Bishal Rijal",
    "age": 25,
    "city": "Kathmandu",
    "skills": ["Python", "JavaScript", "SQL"]
}

# write JSON data to a file

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
    

# read JSON data from a file

with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)