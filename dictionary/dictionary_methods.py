# Using curly braces
my_dict = {"name": "John", "age": 25, "city": "New York"}

# Using the dict() constructor
my_dict2 = dict(name="shivanshu", age=18, city="ghaziabad")
print(my_dict)
print(my_dict2)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
my_dict.update({"name":"monu"})
print(my_dict)
print(my_dict.get("name"))