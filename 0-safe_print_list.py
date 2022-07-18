#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
# TRY
# WHILE i <= x
# FOR i in my_list
# PRINT i
# increment i by 1
# EXCEPT 
# there are no more values to print
    i = 0
    for items in range(x):
        try:
                    print(my_list[i], end="")
                    i += 1
        except IndexError:
            print("No more items in the list")

