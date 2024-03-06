#!/usr/bin/python3
"""File storage module for AirBnB clone."""
import json
import os


class FileStorage:
    """
    Serializes instances to JSON file & deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary of instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """
        Adds an object to __objects dictionary with key <obj class name>.id.

        Args:
            obj (BaseModel): The object to add.

        Raises:
            TypeError: If obj is not an instance of BaseModel.
        """
        from models.base_model import BaseModel
        if not isinstance(obj, BaseModel):
            raise TypeError("obj must be an instance of BaseModel")
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to JSON file (__file_path).

        Raises:
            FileNotFoundError: If file path does not exist.
            Exception: If file could not be saved.
        """
        try:
            obj_dict = {obj_id: obj.to_dict()
                        for obj_id, obj in self.__objects.items()}
            with open(self.__file_path, 'w') as file:
                json.dump(obj_dict, file)
        except FileNotFoundError:
            print(f"Error: File not found ({self.__file_path})")
        except Exception as e:
            print(f"Error while saving to file: {e}")

    def reload(self):
        """
        Deserializes JSON file (__file_path) if __file_path exists.

        Raises:
            FileNotFoundError: If file path does not exist.
            Exception: If file could not be reloaded.
        """
        from models.base_model import BaseModel
        if os.path.isfile(self.__class__.__file_path):
            try:
                with open(self.__class__.__file_path, 'r') as file:
                    objs = json.load(file)
                    for obj_id, obj_dict in objs.items():
                        cls_name = obj_dict['__class__']
                        if cls_name == 'BaseModel':
                            self.new(BaseModel(**obj_dict))
            except FileNotFoundError:
                print(f"Error: File not found ({self.__file_path})")
            except Exception as e:
                print(f"Error while reloading from file: {e}")
