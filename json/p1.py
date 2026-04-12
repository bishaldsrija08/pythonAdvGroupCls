import json


user_data = {
    "name": input("Enter your name: "),
    "age": int(input("Enter your age: ")),
    "city": input("Enter your city: ")
}


with open("p1.json", "w") as file:
    json.dump(user_data, file, indent=4)
    
with open("p1.json", "r") as file:
    data = json.load(file)
    print(data)