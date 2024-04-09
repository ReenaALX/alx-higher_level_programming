#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
<<<<<<< HEAD
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

=======
        print("{} is not an integer".format(value))

        value = -89
        has_been_print = safe_print_integer(value)
        if not has_been_print:
                print("{} is not an integer".format(value))

                value = "School"
                has_been_print = safe_print_integer(value)
                if not has_been_print:
                        print("{} is not an integer".format(value))

                        guillaume@ubuntu:~/0x05$ ./1-main.py
                        89
                        -89
                        School is not an integer
>>>>>>> f7729c8f63347d68781913e10d6405e6c1a41144
