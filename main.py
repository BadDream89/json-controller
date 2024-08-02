import funcs
import sys

arguments = sys.argv[1:]

def main(filename):

    
    cmd = input("\ncommands:\n  print file data (pfd)\n  change data(chda) [key] [value] [datatype]\n  sort keys(soke)\n  clear data(cld) (y/n)\n\n  quit(q)\n>>>")

    pfd = ("print file data", "pfd")
    chda = ("change data", "chda")
    soke = ("sort keys", "soke")
    cld = ("clear data", "cld")
    q = ("quit", "q")

    words = cmd.split()

    if cmd in pfd:

        print("\ndata: \n", funcs.load_data(filename))

    elif cmd in soke:

        funcs.sort(filename)

    elif cmd in q:

        raise KeyboardInterrupt

    elif words[0] in chda or f'{words[0]} {words[1]}' in chda:

        if "change" == words[0]:
            words[0] = words[0] + words[1]

        if len(words) != 4:
            print("got less or more arguments than needed. stopping the function")
            return

        key, value, datatype = words[-3], words[-2], words[-1]


        funcs.change_data(filename, key, value, datatype)

        
    elif words[0] in cld or f'{words[0]} {words[1]}' in cld:
        
        if "clear" in words:
            words[0] = words[0] + words[1]

        if len(words) == 2:
            areyousure = words[1]
        else:
            areyousure = input("are you sure? (y/n)")

        if areyousure.lower() == "y":

            funcs.dump_data(filename, {})

        print("data successfully cleared!")


    else:

        print("unknown command")

if __name__ == "__main__":

    filename = input("enter filename: ")
    if ".json" != filename[-5:]:
        filename = filename + ".json"

    #print(arguments)
    if arguments != []:
        if arguments[0] == "-c" or arguments[0] == "--cmdline":

            main = cmdline_mode.main_cmdline_mode

    while True:

        main(filename)