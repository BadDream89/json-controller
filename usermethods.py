
import funcs


# it sorts dictionary by keys
def sort(filename: str) -> None:

    data: dict = funcs.load_data(filename)
    funcs.dump_data(filename, data, True)
    
    print("sort function has been completed")


# prints data from file
def print_data(filename: str) -> None:

    print("\ndata: \n", funcs.load_data(filename))


# changing data with user's arguments
def change_data(filename: str, words: list) -> None:

    if len(words) != 4:
            print("got less or more arguments than needed. stopping the function")
            return

    #key, value, datatype = words[-3], words[-2], words[-1]
    key, value, datatype = words[-3:]

    funcs.change_data(filename, key, value, datatype)


# remove data function
def remove(filename: str, words: list) -> None:

    key: str = words[1]
    data: dict = funcs.load_data(filename)

    data.pop(key)
    funcs.dump_data(filename, data)
    print(f" key {key} successfully deleted!")


# clear data command function
def clear_data(filename: str, words: list) -> None:

    if len(words) == 2:
            areyousure: str = words[1]
    else:
        areyousure = input("are you sure? (y/n)")

    if areyousure.lower() == "y":

        funcs.dump_data(filename, {})

    print("data successfully cleared!")


# adds list to the .json file
def add_list(filename: str, words: list) -> None:

    key: str = words[1]
    data: dict = funcs.load_data(filename)

    if key in data.keys():
        to_replace = input("there is key in the file. Replace it? (y/n): ")
        if to_replace.lower() == "n":
            return

    data.update({key: tuple()})

    funcs.dump_data(filename, data)


# add value to the list in the .json file
def add_value_to_list(filename: str, words: list) -> None:

    key: str = words[1]
    value: str = words[2]
    datatype: str = words[3]

    try:
        quantity: int = int( words[4] )
    except TypeError:
        print("failed to convert 'quantity' argument into integer")
        return
    except IndexError:
        print("no quantity given. Standart value is 1")
        quantity: int = 1
    
    data: dict = funcs.load_data(filename)

    typeofkey = type(data[key])
    if typeofkey != type(list()):

        print("error: value of the key that was given isn't a list")
        return

    converted_value = funcs.convert_value(value, datatype)
    final_value = [converted_value] * quantity
    data[key] = data[key] + final_value

    funcs.dump_data(filename, data)
