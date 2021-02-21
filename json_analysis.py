"""
This module serves for .json files navigation.
It gives the user information about .json file fields and their values.
The user may choose whether to see the whole object or to choose the further values.
"""

import json
import sys

def read_json(path: str) -> dict:
    """
    Returns a dictionary of .json file.
    """
    try:
        with open(path, mode='r', encoding='utf-8') as json_f:
            data = json.load(json_f)
    except FileNotFoundError:
        data = 'Error! Try again.'
    return data


def dict_field(json_data: dict) -> list or dict or str:
    """
    Returns json_data or a list of its keys depending on what the user chooses.
    Returns the error message if the user inputs something wrong.
    """
    print('This field is a dictionary.')
    mode = input('Would you like to see the whole object (1) or only its keys (2)?\n\
Enter a number: ')
    try:
        if mode == '1':
            fields_list = json_data
        elif mode == '2':
            fields_list = list(json_data.keys())
        return fields_list
    except UnboundLocalError:
        return 'Error! Try again.'


def lst_field(json_data: list) -> list:
    """
    Returns json_data or the error massage if user inputs something wrong.
    """
    print('This field is a list.')
    mode = input('Would you like to see the whole object (1) or only its particalar element \
by number (2)?\nEnter a number: ')
    if mode == '1':
        print(json_data)
    elif mode != '2':
        json_data = 'Error! Try again.'
        print(json_data)
    return json_data


def fields(json_data: list or dict or str) -> list or dict or str:
    """
    Calls additional functions and returns json_data, its keys if it is a dictionary
    or the error message if user inputs something wrong.
    """
    if isinstance(json_data, dict):
        fields_list = dict_field(json_data)
    elif isinstance(json_data, list):
        fields_list = lst_field(json_data)
    else:
        fields_list = json_data
    return fields_list


def main() -> None:
    """
    The main function. It interacts with the user and is responsible for the .json file navigation.
    """
    path = input('Please enter the name of the .json file you would like to navigate in: ')
    json_data = read_json(path) if read_json(path) != "Error! Try again." else sys.exit()
    while True:
        upper_fields = fields(json_data)
        if upper_fields == "Error! Try again.":
            break
        if len(json_data) < 1:
            print("The object is empty. The navigation is finished.")
            break
        if isinstance(json_data, dict):
            print(upper_fields)
            user_key = input("Please enter the field you would like to see \
further information about: ")
            try:
                json_data = json_data[user_key]
            except KeyError:
                print('Error! Try again.')
                break
        elif isinstance(json_data, list):
            num_elements = len(json_data)
            user_el = int(input(f'Please enter the number (lower than {num_elements}) \
of the list element you would like to see:\n'))
            try:
                json_data = json_data[user_el]
            except IndexError:
                print('Error! Try again.')
                break
        else:
            print(upper_fields)
            print("The navigation is finished.")
            break

if __name__ == "__main__":
    main()
