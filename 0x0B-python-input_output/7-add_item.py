import sys
"""Adds the arguments to a python list and then saves them to a file"""
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file.py').load_from_json_file

    the_file = "add_item.json"
    try:
        my_list = load_from_json_file(the_file)
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, the_file)
