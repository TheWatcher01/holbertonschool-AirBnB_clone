#!/usr/bin/python3
"""This module contains the __init__ file for the AirBnB clone"""
from models.engine.file_storage import FileStorage


storage = FileStorage()  # Create instance of FileStorage
storage.reload()  # Reload data from file
