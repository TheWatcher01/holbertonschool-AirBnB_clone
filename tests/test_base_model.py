#!/usr/bin/python3
"""
This module tests the functionality of the BaseModel class.

It creates an instance of BaseModel, assigns values to its attributes,
prints the instance, saves it, prints it again, and then converts it to a
dictionary. The keys of the dictionary are then printed along with their
types and values.
"""
from models.base_model import BaseModel

# Create an instance of BaseModel
my_model = BaseModel()

# Assign values to the instance attributes
my_model.name = "My First Model"
my_model.my_number = 89

# Print the instance
print(my_model)

# Save the instance
my_model.save()

# Print the instance after saving
print(my_model)

# Convert the instance to a dictionary
my_model_json = my_model.to_dict()

# Print the dictionary
print(my_model_json)

print("JSON of my_model:")

# Iterate over the keys in the dictionary
for key in my_model_json.keys():
    # Print each key and its corresponding value
    print(f"\t{key}: ({type(my_model_json[key])}) - {my_model_json[key]}")
