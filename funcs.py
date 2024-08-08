import json
import os

dir_path = str( os.path.dirname(os.path.realpath(__file__)) )


# simply loading data to the json file 
def dump_data(filename: str, obj: dict, tosort=False) -> None:

    # dir_path + "/" + filename is getting absolute path to the file
    file_path = dir_path + "/" + filename
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4, sort_keys=tosort)


# this funtion gets data from the json file
def load_data(filename: str) -> dict:

    with open(dir_path + "/" + filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


# changes or adds data to the json file
def change_data(filename: str, 
                key: str, 
                value: str, 
                datatype: str = "None") -> None:


    data = load_data(filename)


    # gets old value if there was another to tell about old value after successful changing
    old_value: str = ""
    if data.get(key):
        old_value = str(data[key])


    # using function that converts value to user's suggested datatype
    conv_value = convert_value(value, datatype)

    # conv_value will be None if there is an error while running the function
    if conv_value is None:
        return

    # updates data in json file
    data.update({key: conv_value})
    dump_data(filename, data)

    success = "data has been changed"
    if old_value != "":
        success = f"{success}\nold value: {old_value}\n"

    print(success)
    

# converts value from the string to the user's suggested datatype
def convert_value(value: str, datatype: str):

    try:
        match datatype:

            case "int":
                value = int(value)
            case "integer":
                value = int(value)

            case "float":
                value = float(value)

            case "bool":

                falses = ("0", "false", "False")
                if value in falses:
                    value = False
                value = bool(value)

            case "string":
                value = str(value)
            case "str":
                value = str(value)

            case _:
                print("unknown datatype")
                raise ValueError

    except ValueError:
        print("\n\n error: got an error when converting value to suggested datatype. stopping the function \n\n")
        return

    return value