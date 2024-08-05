import funcs
import usermethods
import sys


def main(filename):

    
    cmd = input("\ncommands:\n  print data (pd)\n  change data(chda) [key] [value] [datatype]\n  remove (rm) [key]\n  sort keys(soke)\n  clear data(cld) (y/n)\n  add list (at) [key]\n  add value to list (avt) [key] [value] [datatype] (quantity)\n\n  quit(q)\n>>>")


    # initalizing commands tuples
    pfd = ["print data", "pd"]
    chda = ["change data", "chda"]
    rm = ["remove", "rm"]
    soke = ["sort keys", "soke"]
    avl = ["add value to list", "avl"]
    al = ["add list", "al"]
    cld = ["clear data", "cld"]
    q = ["quit", "q"]


    # splits command to get arguments later
    words = cmd.split()

    # first checking commands that dont need arguments

    # print data
    if cmd in pd:

        usermethods.print_data(filename)

    # sort keys command
    elif cmd in soke:

        usermethods.sort(filename)

    # quit command
    elif cmd in q:

        sys.exit()


    # ... and now commands which need arguments

    #########################

    # 'change data' command
    elif " ".join(words[:2]) in chda:

        words[0] = words[0] + words.pop(1)
        usermethods.change_data(filename, words)

    # now it is 'chda' command
    elif words[0] in chda:
        
        usermethods.change_data(filename, words)

    #########################

    # 'remove' or 'rm' command
    elif words[0] in rm:

        usermethods.remove(filename, words)

    #########################

    # 'clear data' command
    if " ".join(words[:2]) in cld:
        
        words[0] = words[0] + words.pop(1)
        usermethods.clear_data(filename, words)

    # 'cld' command
    elif words[0] in cld:

        usermethods.clear_data(filename, words)
        
    #########################

    # 'add list' command
    elif " ".join(words[:2]) in av:

        words[0] = words[0] + words.pop[1]
        usermethods.add_list(filename, words)

    # 'at" command
    elif words[0] in av:

        usermethods.add_list(filename, words)

    #########################

    # 'add value to list' command
    elif " ".join(words[:4]) in avl:

        words[0] = words[0] + ''.join([words.pop(i) for i in range(1, 4)])
        usermethods.add_value_to_list(filename, words)

    # 'avl' command
    elif words[0] in avl:
        
        usermethods.add_value_to_list(filename, words)

    #########################

    else:

        print("unknown command")

if __name__ == "__main__":

    filename = input("enter filename: ")
    if ".json" != filename[-5:]:
        filename = filename + ".json"

    while True:

        main(filename)