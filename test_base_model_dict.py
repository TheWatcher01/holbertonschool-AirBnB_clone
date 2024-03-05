#!/usr/bin/python3
"""
This module tests the BaseModel class.
"""
from models.base_model import BaseModel

# Create a new instance of BaseModel
my_model = BaseModel()

# Set the attributes of the instance
my_model.name = "My_First_Model"
my_model.my_number = 89

# Print the id of the instance
print(my_model.id)

# Print the string representation of the instance
print(my_model)

# Print the type of the created_at attribute
print(type(my_model.created_at))

print("--")

# Convert the instance to a dictionary and print it
my_model_json = my_model.to_dict()
print(my_model_json)

# Print the keys and values of the dictionary
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key,
          type(my_model_json[key]), my_model_json[key]))

print("--")

# Create a new instance using the dictionary
my_new_model = BaseModel(**my_model_json)

# Print the id of the new instance
print(my_new_model.id)

# Print the string representation of the new instance
print(my_new_model)

# Print the type of the created_at attribute of the new instance
print(type(my_new_model.created_at))

print("--")

# Check if the two instances are the same and print the result
print(my_model is my_new_model)
