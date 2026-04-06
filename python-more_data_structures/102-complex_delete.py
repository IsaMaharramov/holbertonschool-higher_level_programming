#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    Deletes all keys in a dictionary that have a specific value.

    Args:
        a_dictionary: The dictionary to modify.
        value: The value to search for and delete.

    Returns:
        The modified dictionary (or the original if value not found).
    """
    # Create a list of keys to delete to avoid "RuntimeError: dictionary 
    # changed size during iteration"
    keys_to_delete = [k for k, v in a_dictionary.items() if v == value]

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
