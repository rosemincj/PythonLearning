# empty dictionary
sample_dict = {}

# dictionary with integer keys
sample_dict1 = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
sample_dict2 = {'name': 'John', 1: [2, 4, 3]}
print(sample_dict2)

# using dict()
sample_dict3 = dict({1: 'apple', 2: 'ball'})
print(sample_dict3)

# from sequence having each item as a pair
sample_dict4 = dict([('Name', 'Jack'), ('Age', 25)])
print(sample_dict4)

# Output: Jack
print(sample_dict4['Name'])

# Output: 25
print(sample_dict4.get('Age'))

# update value
sample_dict4['Age'] = 27
print(sample_dict4)

# add item
sample_dict4['Address'] = 'Main Street'
print(sample_dict4)

# Get the .keys() list:
print(sample_dict4.keys())

# Likewise, there's a .values() list of values
print(sample_dict4.values())

# .items() is the dict expressed as (key, value) tuples
print(sample_dict4.items())

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
print(squares.pop(4))
print(squares)

# remove an arbitrary item, return (key,value)
print(squares.popitem())
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
print(squares)
