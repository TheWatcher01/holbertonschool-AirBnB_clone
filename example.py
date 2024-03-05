#!/usr/bin/python3
"""Module to test output from Holberton test templates located at ./templates"""


from typing import Callable


choices = []

class Choice:
    """
        Choice class that represent a template choice
        name: Choice name
        callback: callable to use import
    """

    def __init__(self, name: str, template_name: str) -> None:
        self.name = name
        self.callback = lambda: __import__(template_name)
        choices.append(self)

    def select(self) -> None:
        try:
            self.callback()
        except Exception as err:
            print(f"\033[91m[{self.name}] Do you have complete the task ?\nStack: {err}\033[0m")

def on_error() -> None:
    print("\033[91mInvalid choice, please retry\033[0m\n")
    app()

def app() -> None:
    """
        Program entry that is triggered while all Choice are setup and ready.
        Can be recursive on fail.
    """
    try:
        selection = input("Enter test index to select it: ")

        if (selection.isspace() or selection.__len__() == 0):
            print("Operation aborted.")
            exit()

        if (not selection.isdigit()):
            on_error()
            return

        choice = int(selection) - 1

        if (type(choices[choice]) == Choice):
            choices[choice].select()
        else:
            on_error()
    except KeyboardInterrupt:
        print()
        exit()

Choice("BaseModel (Task 3)", "examples.test_base_model")
Choice("BaseModel (Task 4)", "examples.test_base_model_dict")
Choice("BaseModel (Task 5)", "examples.test_save_reload_base_model")

#Create your choices here:
    #Choice("My Choice", my_choice_location)

print("Choose a template to test\n")
print("Choices:")

for i in range(len(choices)):
    print(f"\t\033[96m{i + 1}\033[0m - {choices[i].name}")

print("\n")

#Start the program
app()
