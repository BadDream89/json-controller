import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))



def dump_data(filename: str, obj: dict, tosort=False) -> None:

    with open(dir_path + "/" + filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4, sort_keys=tosort)
    

def load_data(filename: str) -> dict:

    with open(dir_path + "/" + filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data

def change_data(filename: str, 
                key: str, 
                value: str, 
                datatype: str = "None") -> None:

    data = load_data(filename)

    old_value = ""
    if data.get(key):
        old_value = str(data[key])

    try:
        match datatype:

            case "int":
                value = int(value)
            case "float":
                value = float(value)
            case "bool":

                if value == "0":
                    value = False
                value = bool(value)

            case "string":
                value = str(value)
            case _:
                print("unknown datatype")
                raise ValueError

    except ValueError:
        print("\n\n error: got an error when converting value to suggested datatype. stopping the function \n\n")
        return


    data.update({key: value})
    dump_data(filename, data)

    success = "data has been changed"
    if old_value != "":
        success = f"{success}\nold value: {old_value}\n"

    print(success)


def sort(filename: str) -> None:

    data = load_data(filename)
    dump_data(filename, data, True)
    
    print("sort function has been completed")
    

