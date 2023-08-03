my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)
print(my_dict["name"])
print(my_dict["age"])
print(my_dict.get("city"))
print(my_dict.get("country", "N/A"))  # Use a default value for the key "country"

my_dict["age"] = 40
print(my_dict)
print(len(my_dict))
