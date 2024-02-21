person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "colors": ["red", "blue"]
}

print(person)

print(person["name"])
print(person["colors"][1])

test = person.get("name2", "No name")
print(test)

person["name"] = "Jane"
print(person["name"])

person["newName"] = "Jan"
print(person)
person.pop("newName")
print(person)

for key, value in person.items():
    print(key, value)