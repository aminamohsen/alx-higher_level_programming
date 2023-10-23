#!/usr/bin/python3

def safe_print_list_integers(my_list=[], i=0):
    """Print the first i elements of a list that are integers.
    Args:
        my_list (list): The list to print elements from.
        i (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    ret = 0
    for k in range(0, i):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
