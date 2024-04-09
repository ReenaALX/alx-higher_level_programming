#!/usr/bin/python3
<<<<<<< HEAD
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
=======
safe_print_integer(value):
        try:
                    print("{:d}".format(value))
                            return True
                            except (ValueError, TypeError):
                                        return False
>>>>>>> f7729c8f63347d68781913e10d6405e6c1a41144
