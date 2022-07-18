#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for items in range(x):
        try:
            if my_list[i].isdigit():
                print("{:d}", end="".format(my_list[i]))
                i += 1
        except IndexError:
            break
        except (TypeError, ValueError):
            continue
    print()
    return i
