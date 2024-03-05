#!/usr/bin/python3
"""
Module tests save and reload functionalities of BaseModel class.

It first retrieves all objects from storage, prints them, then creates
new BaseModel instance, modifies its attributes, saves it to storage,
and prints it.
"""

from models import storage
from models.base_model import BaseModel

# Retrieve all objects from storage
all_objs = storage.all()

print("-- Reloaded objects --")
# Iterate over all object IDs in storage
for obj_id in all_objs.keys():
    # Get object associated with current object ID
    obj = all_objs[obj_id]
    # Print object
    print(obj)

print("-- Create a new object --")
# Create a new BaseModel instance
my_model = BaseModel()
# Set name attribute of instance
my_model.name = "My_First_Model"
# Set my_number attribute of instance
my_model.my_number = 89
# Save instance to storage
my_model.save()
# Print instance
print(my_model)
