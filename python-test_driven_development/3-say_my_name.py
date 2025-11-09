#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first name> <last name>'.


    Args:
        first_name (str): THe first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
         raise TypeError("last_name must be a string")

      print(f"My name is {first_name}" + (f" {last_name}" if last_name else ""))
