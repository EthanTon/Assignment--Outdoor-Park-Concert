# manages seats.json and user.json
import json

import jsonpickle


def pretty_json(json_string):
    """
    turns json into pretty printed json
    """

    parsed = json.loads(json_string)
    result = json.dumps(parsed, indent=4, sort_keys=True)

    return result


def open_json(file_name):
    """
    Open a json file.
    """
    try:
        file_name = open(file_name, "r")
    except FileNotFoundError:
        print("File, " + file_name + " not found.")
        return None

    json_data = file_name.read()

    file_name.close()

    data = jsonpickle.decode(json_data)

    return data


def save_json(file_name, data):
    """
    Save a json file.
    """
    file_name = open(file_name, "w")
    file_name.write(pretty_json(jsonpickle.encode(data)))
    file_name.close()
