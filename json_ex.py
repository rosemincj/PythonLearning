import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
# You can parse a JSON string using json.loads() method. The method returns a dictionary.
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])

# Converting dictionary to JSON
person_dict = {'name': 'Marley',
               'age': 15,
               'children': None}
person_json = json.dumps(person_dict)

# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)


# Writing JSON to a file

person_dict = {"name": "Bob Marley",
               "languages": ["English", "French"],
               "married": True, "age": 32}

with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)

# Indent and sort_keys to make it more readable

person_string = '{"name": "Bob Marley", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent=4, sort_keys=True))
