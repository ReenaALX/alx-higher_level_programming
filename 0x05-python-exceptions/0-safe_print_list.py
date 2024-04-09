#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
<<<<<<< HEAD
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
=======
        count = 0
            try:
                for i in my_list[:x]:
                    print("{}".format(i), end="")
                    count += 1
            except:
                pass
            print()
            return count
>>>>>>> f7729c8f63347d68781913e10d6405e6c1a41144
