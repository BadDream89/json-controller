import funcs
import usermethods
import sys
import os
import time


def main(filename):


    if not filename in os.listdir(funcs.dir_path):

        #print(filename, os.listdir(funcs.dir_path))
        print("cannot find the file. Creating new.")

        funcs.dump_data(filename, {})


    
    cmd = input("\ncommands:\n  print data(pd)\n  change data(chda) [key] [value] [datatype]\n  removes(rm) [key]\n  sort keys(soke)\n  clear data(cld) (y/n)\n  add list(al) [key]\n  add value to list(avl) [key] [value] [datatype] (quantity)\n\n  quit(q)\n>>>")


    # initalizing commands tuples
    pd = ["print data", "pd"]
    chda = ["change data", "chda"]
    rm = ["remove", "rm"]
    soke = ["sort keys", "soke"]
    avl = ["add value to list", "avl"]
    al = ["add list", "al"]
    cld = ["clear data", "cld"]
    q = ["quit", "q"]



    # splits command to get arguments later
    words = cmd.split(" ")

    # first checking commands that dont need arguments

    # print data
    if words[0] in pd:

        usermethods.print_data(filename)
        time.sleep(0.7)

    elif " ".join(words[:2]) in pd and len(words) > 1:

        usermethods.print_data(filename)
        time.sleep(0.6)

    # sort keys command
    elif words[0] in soke:

        usermethods.sort(filename)

    elif " ".join(words[:2]) in soke:

        usermethods.sort(filename)

    # quit command
    elif words[0] in q:

        sys.exit()


    # ... and now commands which need arguments

    #########################

    # 'change data' command
    elif " ".join(words[:2]) in chda and len(words) > 1:

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
    elif " ".join(words[:2]) in cld and len(words) > 1:
        
        words[0] = words[0] + words.pop(1)
        usermethods.clear_data(filename, words)

    # 'cld' command
    elif words[0] in cld:

        usermethods.clear_data(filename, words)
        
    #########################

    # 'add list' command
    elif " ".join(words[:2]) in al and len(words) > 1:

        words[0] = words[0] + words.pop[1]
        usermethods.add_list(filename, words)

    # 'at" command
    elif words[0] in al:

        usermethods.add_list(filename, words)

    #########################

    # 'add value to list' command
    elif " ".join(words[:4]) in avl and len(words) > 1:

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